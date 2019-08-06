"""
Backward Analysis Engine
========================

:Author: Caterina Urban
"""

from collections import deque
from copy import deepcopy
from queue import Queue
from typing import List, Optional

from apronpy.manager import PyManager

from libra.engine.interpreter import Interpreter
from libra.engine.result import AnalysisResult
from libra.semantics.backward import BackwardSemantics

from libra.abstract_domains.state import State
from libra.core.cfg import Basic, Loop, Conditional, Edge, Node, Function, Activation


import ast
import ctypes
import itertools
import multiprocessing
import os
import sys
import time
from abc import ABCMeta
from collections import defaultdict
from copy import deepcopy
from itertools import product
from queue import Queue, Empty
from typing import Optional, Tuple, Set, Dict, List, FrozenSet

from apronpy.coeff import PyMPQScalarCoeff
from apronpy.environment import PyEnvironment
from apronpy.interval import PyInterval
from apronpy.lincons0 import ConsTyp
from apronpy.manager import FunId, PyBoxMPQManager, PyPolkaMPQstrictManager, PyManager
from apronpy.polka import PyPolka
from apronpy.tcons1 import PyTcons1, PyTcons1Array
from apronpy.texpr0 import TexprOp, TexprRtype, TexprRdir
from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar
from pip._vendor.colorama import Fore, Style, Back

from libra.abstract_domains.bias.bias_domain import BiasState
from libra.abstract_domains.numerical.interval_domain import BoxState, IntEnum
from libra.abstract_domains.numerical.octagon_domain import OctagonState
from libra.abstract_domains.numerical.polyhedra_domain import PolyhedraState
from libra.abstract_domains.state import State
from libra.core.cfg import Node, Function, Activation
from libra.core.expressions import BinaryComparisonOperation, Literal, VariableIdentifier, BinaryBooleanOperation
from libra.core.statements import Call, VariableAccess, Assignment, Lyra2APRON
from libra.engine.forward import ForwardInterpreter, ActivationPatternForwardSemantics
from libra.engine.result import AnalysisResult
from libra.engine.runner import Runner
from libra.frontend.cfg_generator import ast_to_cfg
from libra.semantics.backward import DefaultBackwardSemantics
from libra.semantics.forward import DefaultForwardSemantics
from libra.visualization.graph_renderer import CFGRenderer


rtype = TexprRtype.AP_RTYPE_REAL
rdir = TexprRdir.AP_RDIR_RND
OneHot1 = Tuple[VariableIdentifier, BinaryBooleanOperation]      # one-hot value for 1 feature
OneHotN = Tuple[OneHot1, ...]                                    # one-hot values for n features


class BackwardInterpreter(Interpreter):
    """Backward control flow graph interpreter."""

    def __init__(self, cfg, manager, semantics, specification, widening=2, difference=0.25, precursory=None):
        super().__init__(cfg, semantics, widening=widening, precursory=precursory)
        self.manager: PyManager = manager

        self._initial: BiasState = None                                 # initial analysis state

        self.specification = specification                              # input specification file
        self.sensitive: List[VariableIdentifier] = None                 # sensitive feature
        self.values: List[OneHot1] = None                               # all one-hot sensitive values
        self.uncontroversial1: List[List[VariableIdentifier]] = None    # uncontroversial features / one-hot encoded
        self.uncontroversial2: List[VariableIdentifier] = None          # uncontroversial features / custom encoded
        self.bounds: BinaryBooleanOperation = None      # bound between 0 and 1 of sensitive and one-hot encoded

        self.outputs: Set[VariableIdentifier] = None                    # output classes

        self.activations = None         # activation nodes
        self.active = None              # always active activations
        self.inactive = None            # always inactive activations
        self.count = multiprocessing.Value('i', 0)                  # 1-hot split count
        self.packs = multiprocessing.Manager().dict()               # packing of 1-hot splits
        Key: Tuple[Tuple[Set[Node], Set[Node]], ...]
        self.patterns = multiprocessing.Manager().dict()            # packing of abstract activation patterns
        self.partitions = multiprocessing.Value('i', 0)

        self.difference = difference    # minimum range (default: 0.25)
        self.size = 2                   # minimum pack size

        self.feasible = multiprocessing.Value('d', 0.0)                # percentage that could be analyzed
        self.biased = multiprocessing.Value('d', 0.0)                  # percentage that is biased
        self.unfeasible = multiprocessing.Value('d', 0.0)              # percentage that was ignored
        self.analyzed = multiprocessing.Value('i', 0)                  # analyzed patterns

    @property
    def initial(self):
        """Initial analysis state

        :return: a deep copy of the initial analysis state
        """
        return deepcopy(self._initial)

    @property
    def explored(self):
        """Explored percentage

        :return: percentage that was explored
        """
        return self.feasible.value + self.unfeasible.value

    def one_hots(self, variables: List[VariableIdentifier]) -> Set[OneHot1]:
        """Compute all possible one-hots for a given list of variables

        :param variables: list of variables one-hot encoding a categorical input feature
        :return: set of Libra expressions corresponding to each possible value of the one-hot encoding
        (paired with the variable being one in the encoded value for convenience ---
        the variable is the first element of the tuple)
        """
        values: Set[OneHot1] = set()
        arity = len(variables)
        for i in range(arity):
            # the current variable has value one
            one = Literal('1')
            lower = BinaryComparisonOperation(one, BinaryComparisonOperation.Operator.LtE, variables[i])
            upper = BinaryComparisonOperation(variables[i], BinaryComparisonOperation.Operator.LtE, one)
            value = BinaryBooleanOperation(lower, BinaryBooleanOperation.Operator.And, upper)
            # everything else has value zero
            zero = Literal('0')
            for j in range(0, i):
                lower = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, variables[j])
                upper = BinaryComparisonOperation(variables[j], BinaryComparisonOperation.Operator.LtE, zero)
                conj = BinaryBooleanOperation(lower, BinaryBooleanOperation.Operator.And, upper)
                value = BinaryBooleanOperation(conj, BinaryBooleanOperation.Operator.And, value)
            for j in range(i+1, arity):
                lower = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, variables[j])
                upper = BinaryComparisonOperation(variables[j], BinaryComparisonOperation.Operator.LtE, zero)
                conj = BinaryBooleanOperation(lower, BinaryBooleanOperation.Operator.And, upper)
                value = BinaryBooleanOperation(value, BinaryBooleanOperation.Operator.And, conj)
            values.add((variables[i], value))
        return values

    def feasibility(self, state, manager, key=None, do=False):
        """Determine feasibility (and activation patterns) for a partition of the input space

        :param state: state representing the partition of the input space
        :param manager: manager to be used for the (forward) analysis
        :param key: pre-determined activations
        :param do: whether to compute the activation patterns even if the analysis is not feasible
        :return: feasibility, patterns, last computed number of disjunctions
        """
        feasible = True
        patterns: List[Tuple[OneHot1, FrozenSet[Node], FrozenSet[Node]]] = list()
        disjunctions = len(self.activations)
        for idx, value in enumerate(self.values):
            result = deepcopy(state).assume({value[1]}, manager=manager)
            f_active = key[idx][0] if key else None
            f_inactive = key[idx][1] if key else None
            active, inactive = self.precursory.analyze(result, forced_active=f_active, forced_inactive=f_inactive)
            disjunctions = len(self.activations) - len(active) - len(inactive)
            if disjunctions > self.widening:
                feasible = False
                if not do:
                    break
            patterns.append((value, frozenset(active), frozenset(inactive)))
        return feasible, patterns, disjunctions

    def producer(self, queue3):
        one_hots = itertools.product(*(self.one_hots(encoding) for encoding in self.uncontroversial1))
        count = 0
        for count, one_hot in enumerate(one_hots):
            queue3.put(one_hot)
        self.count.value = count+1
        queue3.put(None)

    def consumer(self, queue3, entry, manager):
        while True:
            one_hot = queue3.get(block=True)
            if one_hot is None:
                queue3.put(None)
                break
            result1 = deepcopy(entry)
            for item in one_hot:
                result1 = result1.assume({item[1]}, manager=manager)
            key = list()
            for value in self.values:
                result2 = deepcopy(result1).assume({value[1]}, manager=manager)
                active, inactive = self.precursory.analyze(result2)
                key.append((frozenset(active), frozenset(inactive)))
            _key = tuple(key)
            if _key not in self.packs:
                self.packs[_key] = {one_hot}
            else:
                curr = self.packs[_key]
                curr.add(one_hot)
                self.packs[_key] = curr

    def packing(self, entry):
        print('1-hot splitting for: {}'.format(
            ' | '.join(
                ', '.join('{}'.format(var) for var in encoding) for encoding in self.uncontroversial1)
        ))

        # prepare the queue
        queue3 = multiprocessing.Queue()
        # do the 1-hot splitting
        start3 = time.time()
        processes = list()
        process = multiprocessing.Process(target=self.producer, args=(queue3,))
        processes.append(process)
        process.start()
        for _ in range(multiprocessing.cpu_count() - 1):
            process = multiprocessing.Process(target=self.consumer, args=(queue3, entry, PyBoxMPQManager()))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        end3 = time.time()

        print(Fore.YELLOW + '\nFound {} Packs:'.format(self.count.value))
        score = lambda k: sum(len(s[0]) + len(s[1]) for s in k)
        for key, pack in sorted(self.packs.items(), key=lambda v: score(v[0]) + len(v[1]), reverse=True):
            sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
            skey = ' | '.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
            sscore = '(score: {})'.format(score(key) + len(pack))
            spack = ' | '.join('{}'.format(','.join('{}'.format(item[0]) for item in one_hot)) for one_hot in pack)
            print(Fore.YELLOW, skey, '->', spack, sscore, Style.RESET_ALL)
        print(Fore.YELLOW + '1-Hot Splitting Time: {}s'.format(end3 - start3), Style.RESET_ALL)

    def worker1(self, queue1, manager):
        while True:
            assumptions, pivot1, ranges, pivot2, splittable, percent, key = queue1.get(block=True)
            if assumptions is None:
                queue1.put((None, None, None, None, None, None, None))
                break
            print(Fore.LIGHTMAGENTA_EX + '\n---------------------------')
            print('1-Hot: {}'.format(
                ', '.join('{}'.format('|'.join('{}'.format(var) for var in case)) for (case, _) in assumptions)
            ))
            print('Ranges: {}'.format(
                ', '.join(
                    '{} ∈ [{}, {}]'.format(feature, lower, upper) for feature, (lower, upper) in ranges)
            ))
            print('---------------------------\n', Style.RESET_ALL)

            # bound the custom encoded uncontroversial features between their current lower and upper bounds
            bounds = self.bounds
            for feature, (lower, upper) in ranges:
                left = BinaryComparisonOperation(Literal(str(lower)), BinaryComparisonOperation.Operator.LtE, feature)
                right = BinaryComparisonOperation(feature, BinaryComparisonOperation.Operator.LtE, Literal(str(upper)))
                conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
                bounds = BinaryBooleanOperation(bounds, BinaryBooleanOperation.Operator.And, conj)

            entry = self.initial.precursory.assume({bounds}, manager=manager)
            # take into account the accumulated assumptions on the one-hot encoded uncontroversial features
            for (_, assumption) in assumptions:
                entry = entry.assume({assumption}, manager=manager)
            # find the (abstract) activation patterns corresponding to each possible value of the sensitive feature
            feasibility = self.feasibility(entry, manager, key=key)
            feasible: bool = feasibility[0]
            # perform the analysis, if feasible, or partition the space of values of all the uncontroversial features
            if feasible:
                with self.partitions.get_lock():
                    self.partitions.value += 1
                with self.feasible.get_lock():
                    self.feasible.value += percent
                patterns: List[Tuple[OneHot1, Set[Node], Set[Node]]] = feasibility[1]
                key = list()
                for _, active, inactive in patterns:
                    key.append((frozenset(active), frozenset(inactive)))

                value = (frozenset(assumptions), frozenset(ranges), percent)
                _key = tuple(key)
                if _key not in self.patterns:
                    self.patterns[_key] = {value}
                else:
                    curr = self.patterns[_key]
                    curr.add(value)
                    self.patterns[_key] = curr
                print(Fore.YELLOW + 'Progress: {}% of {}%'.format(self.feasible.value, self.explored), Style.RESET_ALL)
            else:  # too many disjunctions, we need to split further
                print('Too many disjunctions ({})!'.format(feasibility[2]))
                if pivot1 < len(self.uncontroversial1):  # we still have to split the one-hot encoded
                    self.packing(entry)
                    # run the analysis on the ranked packs
                    score = lambda k: sum(len(s[0]) + len(s[1]) for s in k)
                    for key, pack in sorted(self.packs.items(), key=lambda v: score(v[0]) + len(v[1]), reverse=True):
                        _assumptions = list(assumptions)
                        items: List[OneHotN] = list(pack)  # multiple one-hot values for n features
                        for i in range(len(items[0])):  # for each feature...
                            vars: Set[VariableIdentifier] = set()
                            var, case = items[0][i]
                            vars.add(var)
                            for item in items[1:]:
                                var, nxt = item[i]
                                vars.add(var)
                                case = BinaryBooleanOperation(case, BinaryBooleanOperation.Operator.Or, nxt)
                            _assumptions.append((frozenset(vars), case))
                        newpercent = percent * len(pack) / self.count.value
                        queue1.put((_assumptions, len(self.uncontroversial1), ranges, pivot2, splittable, newpercent, key))
                else:  # we can split the rest
                    if self.uncontroversial2 and splittable:
                        rangesdict = dict(ranges)
                        (lower, upper) = rangesdict[self.uncontroversial2[pivot2]]
                        if upper - lower <= self.difference:
                            print('Cannot range split for {} anymore!'.format(self.uncontroversial2[pivot2]))
                            remained = list(splittable)
                            remained.remove(self.uncontroversial2[pivot2])
                            queue1.put((assumptions, pivot1, ranges, (pivot2 + 1) % len(self.uncontroversial2), list(remained), percent, None))
                        else:
                            middle = lower + (upper - lower) / 2
                            print('Range split for {} at: {}'.format(self.uncontroversial2[pivot2], middle))
                            left = deepcopy(rangesdict)
                            left[self.uncontroversial2[pivot2]] = (lower, middle)
                            right = deepcopy(rangesdict)
                            right[self.uncontroversial2[pivot2]] = (middle, upper)
                            newpercent = percent / 2
                            queue1.put((assumptions, pivot1, list(left.items()), (pivot2 + 1) % len(self.uncontroversial2), splittable, newpercent, None))
                            queue1.put((assumptions, pivot1, list(right.items()), (pivot2 + 1) % len(self.uncontroversial2), splittable, newpercent, None))
                    else:
                        with self.unfeasible.get_lock():
                            self.unfeasible.value += percent
                        print(Fore.LIGHTRED_EX + 'Stopping here!', Style.RESET_ALL)
                        print(Fore.YELLOW + 'Progress: {}% of {}%'.format(self.feasible.value, self.explored), Style.RESET_ALL)
                        # self.pick(assumptions, pivot1, ranges, pivot2, splittable, percent, do=True)
            if self.explored >= 100.0:
                queue1.put((None, None, None, None, None, None, None))

    def bias_check(self, color, check: Dict[Tuple[VariableIdentifier, VariableIdentifier], Set[BiasState]],
                   # assumptions0,
                   ranges: Dict[VariableIdentifier, Tuple[int, int]],
                   percent: float):
        print('Checking for Bias...')
        nobias = True
        biases = set()
        for (outcome1, sensitive1), value1 in check.items():
            for (outcome2, sensitive2), value2 in check.items():
                if outcome1 != outcome2 and sensitive1 != sensitive2:
                    for val1 in value1:
                        for val2 in value2:
                            intersection = deepcopy(val1).meet(val2)
                            for encoding in self.uncontroversial1:
                                intersection = intersection.forget(encoding)
                            for feature, (lower, upper) in ranges:
                                lte = BinaryComparisonOperation.Operator.LtE
                                left = BinaryComparisonOperation(Literal(str(lower)), lte, feature)
                                right = BinaryComparisonOperation(feature, lte, Literal(str(upper)))
                                conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
                                intersection = intersection.assume({conj}, manager=self.manager)
                            # for assumption in assumptions0:
                            #     intersection = intersection.assume(assumption)
                            representation = repr(intersection.polka)
                            if not representation.startswith('-1.0 >= 0') and not representation == '⊥':
                                nobias = False
                                if representation not in biases:
                                    biases.add(representation)
                                    print(color + Fore.RED + '✘ Bias Found! : {}'.format(representation), Style.RESET_ALL)
        if nobias:
            print(color + Fore.GREEN + '✔︎ No Bias', Style.RESET_ALL)
        else:
            with self.biased.get_lock():
                self.biased.value += percent

    def from_node(self, node, initial, join):
        """Analyze the CFG

        :param node: node from which to start the analysis
        :param initial: state from which to start the analysis
        :param join: whether joins should be performed
        :return: the result of the analysis (at the beginning of the CFG)
        """
        state = initial
        if isinstance(node, Function):
            state = self.semantics.list_semantics(node.stmts, state)
            if state.is_bottom():
                yield None
            else:
                if self.cfg.predecessors(node):
                    yield from self.from_node(self.cfg.nodes[self.cfg.predecessors(node).pop()], state, join)
                else:
                    yield state
        elif isinstance(node, Activation):
            if node in self.active:  # only the active path is viable
                state = self.semantics.ReLU_call_semantics(node.stmts, state, self.manager, True)
                if state.is_bottom():
                    yield None
                else:
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    yield from self.from_node(predecessor, state, join)
            elif node in self.inactive:  # only the inactive path is viable
                state = self.semantics.ReLU_call_semantics(node.stmts, state, self.manager, False)
                if state.is_bottom():
                    yield None
                else:
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    yield from self.from_node(predecessor, state, join)
            else:  # both paths are viable
                active, inactive = deepcopy(state), deepcopy(state)
                state1 = self.semantics.ReLU_call_semantics(node.stmts, active, self.manager, True)
                state2 = self.semantics.ReLU_call_semantics(node.stmts, inactive, self.manager, False)
                if join:
                    state = state1.join(state2)
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    yield from self.from_node(predecessor, state, join)
                else:
                    if state1.is_bottom():
                        if state2.is_bottom():
                            yield None
                        else:
                            predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                            yield from self.from_node(predecessor, state2, join)
                    else:
                        predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                        yield from self.from_node(predecessor, state1, join)
                        if state2.is_bottom():
                            yield None
                        else:
                            yield from self.from_node(predecessor, state2, join)
        else:
            if self.cfg.predecessors(node):
                yield from self.from_node(self.cfg.nodes[self.cfg.predecessors(node).pop()], state, join)
            else:
                yield state

    def doit(self, color, key, pack, manager, do=False):
        check: Dict[Tuple[VariableIdentifier, VariableIdentifier], Set[BiasState]] = dict()
        for idx, (case, value) in enumerate(self.values):
            self.active, self.inactive = key[idx]
            print(color + '--------- {} --------- '.format(case).replace('x014', 'male').replace('x015', 'female').replace('y0', 'male').replace('y1', 'female'), Style.RESET_ALL)
            # print('activations: {{{}}}'.format(
            #     ', '.join('{}'.format(activation) for activation in self.activations)
            # ))
            print(color + 'active: {{{}}}'.format(', '.join('{}'.format(active) for active in self.active)), Style.RESET_ALL)
            print(color + 'inactive: {{{}}}'.format(', '.join('{}'.format(inactive) for inactive in self.inactive)), Style.RESET_ALL)
            disjunctions = len(self.activations) - len(self.active) - len(self.inactive)
            paths = 2 ** disjunctions
            print(color + 'Paths: {}'.format(paths), Style.RESET_ALL)
            for chosen in self.outputs:
                remaining = self.outputs - {chosen}
                discarded = remaining.pop()
                outcome = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
                for discarded in remaining:
                    cond = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
                    outcome = BinaryBooleanOperation(outcome, BinaryBooleanOperation.Operator.And, cond)
                result = self.initial.assume({outcome}, manager=manager, bwd=True)
                check[(chosen, case)] = set()
                for state in self.from_node(self.cfg.out_node, deepcopy(result), do):
                    if state:
                        state = state.assume({value}, manager=manager)
                        check[(chosen, case)].add(state)
        print(color + '===========================', Style.RESET_ALL)

        # check for bias
        for assumptions, ranges, percent in pack:
            print()
            print(color + '---------------------------', Style.RESET_ALL)
            print(color + '1-Hot: {}'.format(
                ', '.join('{}'.format('|'.join('{}'.format(var) for var in case)) for (case, _) in assumptions)
            ), Style.RESET_ALL)
            print(color + 'Ranges: {}'.format(
                ', '.join('{} ∈ [{}, {}]'.format(feature, lower, upper) for feature, (lower, upper) in ranges)
            ), Style.RESET_ALL)
            print(color + '---------------------------', Style.RESET_ALL)
            print()
            partition = deepcopy(check)
            for states in partition.values():
                for state in states:
                    for (_, assumption) in assumptions:
                        state = state.assume({assumption}, manager=manager)
                    # forget the sensitive variables
                    state = state.forget(self.sensitive)
            self.bias_check(color, partition, ranges, percent)

    def worker2(self, p, color, queue2, manager, pattnum):
        while True:
            idx, (key, pack) = queue2.get(block=True)
            if idx is None:
                queue2.put((None, (None, None)))
                break
            print()
            print(color + '===========================', Style.RESET_ALL)
            print(color + 'Pattern #{} of {} [{}]'.format(idx, pattnum, len(pack)), Style.RESET_ALL)
            self.doit(color, key, pack, manager=manager)
            with self.analyzed.get_lock():
                self.analyzed.value += len(pack)
            print(Fore.YELLOW + 'Progress for #{}: {} of {} partitions ({}% biased)'.format(p, self.analyzed.value, self.partitions.value, self.biased.value), Style.RESET_ALL)

    def analyze(self, initial, inputs=None, outputs=None, activations=None):
        """Backward analysis checking for algorithmic bias

        :param initial: (BiasState) state from which to start the analysis
        :param inputs: (Set[VariableIdentifier]) input variables
        :param outputs: (Set[VariableIdentifier]) output variables
        :param activations: (Set[Node]) CFG nodes corresponding to activation functions
        """
        print(Fore.BLUE + '\n||=================||')
        print('|| symbolic1: {}'.format(self.precursory.symbolic1))
        print('|| symbolic2: {}'.format(self.precursory.symbolic2))
        print('|| difference: {}'.format(self.difference))
        print('|| widening: {}'.format(self.widening))
        print('||=================||', Style.RESET_ALL)
        self._initial = initial
        with open(self.specification, 'r') as specification:
            """
            pick sensitive feature and fix its bounds / we assume one-hot encoding
            """
            arity = int(specification.readline().strip())
            self.sensitive = list()
            for i in range(arity):
                self.sensitive.append(VariableIdentifier(specification.readline().strip()))
            self.values: List[OneHot1] = list(self.one_hots(self.sensitive))
            # bound the sensitive feature between 0 and 1
            zero = Literal('0')
            one = Literal('1')
            left = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, self.sensitive[0])
            right = BinaryComparisonOperation(self.sensitive[0], BinaryComparisonOperation.Operator.LtE, one)
            self.bounds = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
            for sensitive in self.sensitive[1:]:
                left = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, sensitive)
                right = BinaryComparisonOperation(sensitive, BinaryComparisonOperation.Operator.LtE, one)
                conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
                self.bounds = BinaryBooleanOperation(self.bounds, BinaryBooleanOperation.Operator.And, conj)
            """
            determine the one-hot encoded uncontroversial features and fix their bounds
            """
            self.uncontroversial1 = list()
            while True:
                try:
                    arity = specification.readline().strip()
                    uncontroversial = list()
                    for i in range(int(arity)):
                        uncontroversial.append(VariableIdentifier(specification.readline().strip()))
                    self.uncontroversial1.append(uncontroversial)
                except ValueError:
                    break
            # bound the one-hot encoded uncontroversial features between 0 and 1
            for encoding in self.uncontroversial1:
                for uncontroversial in encoding:
                    left = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, uncontroversial)
                    right = BinaryComparisonOperation(uncontroversial, BinaryComparisonOperation.Operator.LtE, one)
                    conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
                    self.bounds = BinaryBooleanOperation(self.bounds, BinaryBooleanOperation.Operator.And, conj)
            """
            determine the custom encoded uncontroversial features
            """
            self.uncontroversial2 = list(inputs - set(self.sensitive) - set(itertools.chain(*self.uncontroversial1)))
            ranges: Dict[VariableIdentifier, Tuple[int, int]] = dict()
            for uncontroversial in self.uncontroversial2:
                ranges[uncontroversial] = (0, 1)
            # for uncontroversial in self.uncontroversial2:
            #     left = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, uncontroversial)
            #     right = BinaryComparisonOperation(uncontroversial, BinaryComparisonOperation.Operator.LtE, one)
            #     conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
            #     self.bounds = BinaryBooleanOperation(self.bounds, BinaryBooleanOperation.Operator.And, conj)
        self.outputs = outputs
        self.activations = activations
        cpu = multiprocessing.cpu_count()
        print('\nAvailable CPUs: {}'.format(cpu))
        colors = [
            Style.RESET_ALL,
            Back.BLACK + Fore.WHITE,
            Back.LIGHTRED_EX + Fore.BLACK,
            Back.MAGENTA + Fore.BLACK,
            Back.BLUE + Fore.BLACK,
            Back.CYAN + Fore.BLACK,
            Back.LIGHTGREEN_EX + Fore.BLACK,
            Back.YELLOW + Fore.BLACK,
        ]
        """
        do the pre-analysis
        """
        print(Fore.BLUE + '\n||==============||')
        print('|| Pre-Analysis ||')
        print('||==============||', Style.RESET_ALL)
        # prepare the queue
        queue1 = multiprocessing.Queue()
        queue1.put((list(), 0, list(ranges.items()), 0, list(self.uncontroversial2), 100, None))
        # run the pre-analysis
        start1 = time.time()
        processes = list()
        for _ in range(cpu):
            process = multiprocessing.Process(target=self.worker1, args=(queue1, PyBoxMPQManager()))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        end1 = time.time()
        #
        print(Fore.BLUE + '\nFound: {} patterns for {} partitions'.format(len(self.patterns), self.partitions.value))
        prioritized = sorted(self.patterns.items(), key=lambda v: len(v[1]), reverse=True)
        for key, pack in prioritized:
            sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
            skey = ' | '.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
            print(skey, '->', len(pack))
        #
        compressed = dict()
        for key1 in self.patterns:
            unmerged = True
            for key2 in compressed:
                mergeable1, mergeable2 = True, True
                for s1, s2 in key1:
                    for s3, s4 in key2:
                        if (not s3.issubset(s1)) or (not s4.issubset(s2)):
                            mergeable1 = False
                        if (not s1.issubset(s3)) or (not s2.issubset(s4)):
                            mergeable2 = False
                if mergeable1:
                    unmerged = False
                    compressed[key2] = compressed[key2].union(self.patterns[key1])
                    break
                if mergeable2:
                    unmerged = False
                    compressed[key1] = compressed[key2].union(self.patterns[key1])
                    del compressed[key2]
                    break
            if unmerged:
                compressed[key1] = self.patterns[key1]
        prioritized = sorted(compressed.items(), key=lambda v: len(v[1]), reverse=True)
        if len(compressed) < len(self.patterns):
            print('Compressed to: {} patterns'.format(len(compressed)))
            for key, pack in prioritized:
                sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
                skey = ' | '.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
                print(skey, '->', len(pack))
        #
        print('Pre-Analysis Time: {}s'.format(end1 - start1), Style.RESET_ALL)

        """
        do the analysis
        """
        print(Fore.BLUE + '\n||==========||')
        print('|| Analysis ||')
        print('||==========||\n', Style.RESET_ALL)
        # prepare the queue
        queue2 = multiprocessing.Queue()
        for idx, (key, pack) in enumerate(prioritized):
            queue2.put((idx+1, (key, pack)))
        queue2.put((None, (None, None)))
        # run the analysis
        start2 = time.time()
        processes = list()
        for i in range(cpu):
            color = colors[i % len(colors)]
            man = PyPolkaMPQstrictManager()
            process = multiprocessing.Process(target=self.worker2, args=(i, color, queue2, man, len(compressed)))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        end2 = time.time()
        #
        print(Fore.BLUE + '\nResult: {}% of {}% ({}% biased)'.format(self.feasible.value, self.explored, self.biased.value))
        print('Pre-Analysis Time: {}s'.format(end1 - start1))
        print('Analysis Time: {}s'.format(end2 - start2), Style.RESET_ALL)
        print('\nDone!')


class BiasBackwardSemantics(DefaultBackwardSemantics):

    def list_semantics(self, stmt, state) -> State:
        state.polka = state.polka.substitute(stmt[0], stmt[1])
        return state

    def ReLU_call_semantics(self, stmt, state, manager: PyManager = None, active: bool = True) -> State:
        assert manager is not None
        if active:  # assume h >= 0
            expr = PyTexpr1.var(state.environment, stmt)
            cond = PyTcons1.make(expr, ConsTyp.AP_CONS_SUPEQ)
            abstract1 = PyPolka(manager, state.environment, array=PyTcons1Array([cond]))
            state.polka = state.polka.meet(abstract1)
            return state
        else:  # assign h = 0, assume h < 0
            expr = PyTexpr1.var(state.environment, stmt)
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            neg = PyTexpr1.binop(TexprOp.AP_TEXPR_SUB, zero, expr, rtype, rdir)
            cond = PyTcons1.make(neg, ConsTyp.AP_CONS_SUP)
            abstract1 = PyPolka(manager, state.environment, array=PyTcons1Array([cond]))
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            state.polka = state.polka.substitute(stmt, zero).meet(abstract1)
            return state
