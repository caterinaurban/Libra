"""
Bias Analysis
=============

:Author: Caterina Urban
"""
import ast
import ctypes
import itertools
import os
import sys
import time
from abc import ABCMeta
from collections import defaultdict
from copy import deepcopy
from itertools import product
from queue import Queue
from typing import Optional, Tuple, Set, Dict, List, FrozenSet

from apronpy.coeff import PyMPQScalarCoeff
from apronpy.environment import PyEnvironment
from apronpy.interval import PyInterval
from apronpy.lincons0 import ConsTyp
from apronpy.manager import FunId
from apronpy.polka import PyPolkaMPQstrict
from apronpy.t1p import PyT1pMPQ
from apronpy.tcons1 import PyTcons1, PyTcons1Array
from apronpy.texpr0 import TexprOp, TexprRtype, TexprRdir
from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar
from pip._vendor.colorama import Fore, Style

from libra.abstract_domains.bias.bias_domain import BiasState
from libra.abstract_domains.numerical.interval_domain import BoxState, IntEnum
from libra.abstract_domains.numerical.octagon_domain import OctagonState
from libra.abstract_domains.numerical.polyhedra_domain import PolyhedraState
from libra.abstract_domains.numerical.taylor1p_domain import Taylor1pState, Taylor1pMPQState
from libra.abstract_domains.state import State
from libra.core.cfg import Node, Function, Activation
from libra.core.expressions import BinaryComparisonOperation, Literal, VariableIdentifier, BinaryBooleanOperation
from libra.core.statements import Call, VariableAccess, Assignment, Lyra2APRON
from libra.engine.backward import BackwardInterpreter
from libra.engine.forward import ForwardInterpreter
from libra.engine.result import AnalysisResult
from libra.engine.runner import Runner
from libra.frontend.cfg_generator import ast_to_cfg
from libra.semantics.backward import DefaultBackwardSemantics
from libra.semantics.forward import DefaultForwardSemantics
from libra.visualization.graph_renderer import CFGRenderer


rtype = TexprRtype.AP_RTYPE_REAL
rdir = TexprRdir.AP_RDIR_RND


class ActivationPatternInterpreter(ForwardInterpreter):

    def __init__(self, cfg, semantics, widening, precursory=None):
        super().__init__(cfg, semantics, widening, precursory)
        self.symbolic = False

    def analyze(self, initial: BoxState, forced_active=None, forced_inactive=None):
        """Forward analysis extracting abstract activation patterns.

        :param initial: initial state of the analysis
        :return: three sets: all activation nodes, always active nodes, always inactive nodes
        """
        worklist = Queue()
        worklist.put(self.cfg.in_node)
        state = deepcopy(initial)
        activations, activated, deactivated = set(), set(), set()
        symbols: Dict[str, Tuple[PyVar, PyTexpr1]] = dict()

        while not worklist.empty():
            current: Node = worklist.get()  # retrieve the current node
            # execute block
            if isinstance(current, Function):
                if self.symbolic:
                    array = list()
                    assignments = dict()
                    for lhs, expr in zip(*current.stmts):
                        rhs = expr
                        for sym, val in symbols.values():
                            rhs = rhs.substitute(sym, val)
                        assignments[str(lhs)] = (lhs, rhs)
                        var = PyTexpr1.var(state.environment, lhs)
                        binop = PyTexpr1.binop(TexprOp.AP_TEXPR_SUB, var, rhs, rtype, rdir)
                        cond = PyTcons1.make(binop, ConsTyp.AP_CONS_EQ)
                        array.append(cond)
                    symbols = assignments
                    state.state = state.state.meet(PyTcons1Array(array))
                # if self.symbolic:
                #     lhss = list()
                #     rhss = list()
                #     assignments = dict()
                #     for lhs, expr in zip(*current.stmts):
                #         rhs = expr
                #         for sym, val in symbols.values():
                #             rhs = rhs.substitute(sym, val)
                #         lhss.append(lhs)
                #         rhss.append(rhs)
                #         assignments[str(lhs)] = (lhs, rhs)
                #     symbols = assignments
                #     state = self.semantics.list_semantics((lhss, rhss), state)
                # if self.symbolic:
                #     array = list()
                #     for lhs, rhs in symbols.values():
                #         var = PyTexpr1.var(state.environment, lhs)
                #         binop = PyTexpr1.binop(TexprOp.AP_TEXPR_SUB, var, rhs, rtype, rdir)
                #         cond = PyTcons1.make(binop, ConsTyp.AP_CONS_EQ)
                #         array.append(cond)
                #     if array:
                #         state.state = state.state.meet(PyTcons1Array(array))
                #
                #     assignments = dict()
                #     for lhs, expr in zip(*current.stmts):
                #         rhs = expr
                #         for sym, val in symbols.values():
                #             rhs = rhs.substitute(sym, val)
                #         assignments[str(lhs)] = (lhs, rhs)
                #     symbols = assignments
                #
                #     state = self.semantics.list_semantics(current.stmts, state)
                else:
                    state = self.semantics.list_semantics(current.stmts, state)
            elif isinstance(current, Activation):
                activations.add(current)
                if forced_active and current in forced_active:
                    active = deepcopy(state)
                    state = self.semantics.ReLU_call_semantics(current.stmts, active, True)
                    activated.add(current)
                elif forced_inactive and current in forced_inactive:
                    if self.symbolic:
                        zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
                        symbols[str(current.stmts)] = (current.stmts, zero)
                    inactive = deepcopy(state)
                    state = self.semantics.ReLU_call_semantics(current.stmts, inactive, False)
                    deactivated.add(current)
                else:
                    active, inactive = deepcopy(state), deepcopy(state)
                    # active path
                    state1 = self.semantics.ReLU_call_semantics(current.stmts, active, True)
                    # inactive path
                    state2 = self.semantics.ReLU_call_semantics(current.stmts, inactive, False)
                    if state1.is_bottom():
                        if self.symbolic:
                            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
                            symbols[str(current.stmts)] = (current.stmts, zero)
                        deactivated.add(current)
                    elif state2.is_bottom():
                        activated.add(current)
                    elif self.symbolic:
                        del symbols[str(current.stmts)]
                    state = state1.join(state2)
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(self.cfg.nodes[node.identifier])
        return activations, activated, deactivated


class ActivationPatternForwardSemantics(DefaultForwardSemantics):

    def list_semantics(self, stmt, state) -> State:
        # lhss = [self.semantics(assignment.left, state).result for assignment in stmt]
        # rhss = [self.semantics(assignment.right, state).result for assignment in stmt]
        # return state.assign(lhss, rhss)
        state.state = state.state.assign(stmt[0], stmt[1])
        return state

    def ReLU_call_semantics(self, stmt, state, active: bool = True) -> State:
        # assert len(stmt.arguments) == 1  # exactly one argument is expected
        # argument = stmt.arguments[0]
        # assert isinstance(argument, VariableAccess)
        # left = argument.variable
        # right = Literal('0')
        if active:  # assume h >= 0
            # cond = {BinaryComparisonOperation(left, BinaryComparisonOperation.Operator.GtE, right)}
            # return state.assume(cond)
            expr = PyTexpr1.var(state.environment, stmt)
            cond = PyTcons1.make(expr, ConsTyp.AP_CONS_SUPEQ)
            abstract1 = state.domain(state.environment, array=PyTcons1Array([cond]))
            state.state = state.state.meet(abstract1)
            return state
        else:  # assume h < 0, assign h = 0
            # cond = {BinaryComparisonOperation(left, BinaryComparisonOperation.Operator.Lt, right)}
            # return state.assume(cond).assign({left}, {right})
            expr = PyTexpr1.var(state.environment, stmt)
            neg = PyTexpr1.unop(TexprOp.AP_TEXPR_NEG, expr, rtype, rdir)
            cond = PyTcons1.make(neg, ConsTyp.AP_CONS_SUP)
            abstract1 = state.domain(state.environment, array=PyTcons1Array([cond]))
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            state.state = state.state.meet(abstract1).assign(stmt, zero)
            return state


class JoinHeuristics(IntEnum):
    NotTop = 0


debug = False


class BiasInterpreter(BackwardInterpreter):

    def __init__(self, cfg, semantics, widening, precursory=None):
        super().__init__(cfg, semantics, widening, precursory)
        self._initial: BiasState = None                                 # initial analysis state

        self.sensitive: List[VariableIdentifier] = None                 # sensitive feature
        self.values: List[Tuple[VariableIdentifier, BinaryBooleanOperation]] = None     # all one-hot sensitive values
        self.uncontroversial1: List[List[VariableIdentifier]] = None    # uncontroversial features / one-hot encoded
        self.uncontroversial2: List[VariableIdentifier] = None          # uncontroversial features / custom encoded
        self.bounds: BinaryBooleanOperation = None      # bound between 0 and 1 of sensitive and one-hot encoded

        self.outputs: Set[VariableIdentifier] = None                    # output classes

        self.activations = None         # number of activation nodes
        self.active = None              # always active activations
        self.inactive = None            # always inactive activations
        Key: Tuple[Tuple[Set[Node], Set[Node]], ...]
        self.patterns = defaultdict(set)    # packing of abstract activation patterns
        self.partitions = 0

        self.difference = 0.25          # minimum range (default: 0.25)
        self.size = 2                   # minimum pack size
        # relu splitting
        self.splits: Dict[int, Dict[VariableIdentifier, PyTexpr1]] = None       # splitting information
        self.layer = 1
        self.affines: List[VariableIdentifier]                                  # relus for splitting
        self.relus = Dict[VariableIdentifier, Node]                             # relu information

        self.feasible = 0               # percentage that could be analyzed
        self.epaths = 0
        self.biased = 0                 # percentage that is biased
        self.unbiased = 0               # percentage that is unbiased
        self.unfeasible = 0             # percentage that was ignored
        self.ipaths = 0

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
        return self.feasible + self.unfeasible

    def feasibility_and_patterns(self, state, key=None, do=False):
        feasible = True
        patterns: List[Tuple[Tuple[VariableIdentifier, BinaryBooleanOperation], Set[Node], Set[Node], Set[Node]]] = list()
        paths = 0
        for idx, value in enumerate(self.values):
            # print(Fore.YELLOW + '--------- {} --------- '.format(value[0]).replace('x042', 'male').replace('x043', 'female'))
            result = deepcopy(state).assume({value[1]})
            forced_active = key[idx][0] if key else None
            forced_inactive = key[idx][1] if key else None
            activations, active, inactive = self.precursory.analyze(result, forced_active=forced_active, forced_inactive=forced_inactive)
            # print('active: {{{}}}'.format(', '.join('{}'.format(active) for active in active)))
            # print('inactive: {{{}}}'.format(', '.join('{}'.format(inactive) for inactive in inactive)))
            disjunctions = len(activations) - len(active) - len(inactive)
            paths = paths + 2 ** disjunctions
            # print('paths: {}\n'.format(2 ** disjunctions), Style.RESET_ALL)
            if disjunctions > self.widening:
                feasible = False
                # if not do:
                #     break
            patterns.append((value, frozenset(activations), frozenset(active), frozenset(inactive)))
        return feasible, patterns, paths

    def doit(self, key, pack, do=False):
        check: Dict[Tuple[VariableIdentifier, VariableIdentifier], Set[BiasState]] = dict()
        for idx, (case, value) in enumerate(self.values):
            self.active, self.inactive = key[idx]
            print('--------- {} --------- '.format(case).replace('x014', 'male').replace('x015', 'female').replace('y0', 'male').replace('y1', 'female'))
            # print('activations: {{{}}}'.format(
            #     ', '.join('{}'.format(activation) for activation in self.activations)
            # ))
            print('active: {{{}}}'.format(', '.join('{}'.format(active) for active in self.active)))
            print('inactive: {{{}}}'.format(', '.join('{}'.format(inactive) for inactive in self.inactive)))
            disjunctions = len(self.activations) - len(self.active) - len(self.inactive)
            paths = 2 ** disjunctions
            print('Paths: {}'.format(paths))
            for chosen in self.outputs:
                remaining = self.outputs - {chosen}
                discarded = remaining.pop()
                outcome = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
                for discarded in remaining:
                    cond = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
                    outcome = BinaryBooleanOperation(outcome, BinaryBooleanOperation.Operator.And, cond)
                result = self.initial.assume({outcome}, bwd=True)
                check[(chosen, case)] = set()
                for state in self.proceed(self.cfg.out_node, deepcopy(result), list(), do):
                    if state:
                        state = state.assume({value})
                        check[(chosen, case)].add(state)
        print('===========================', Style.RESET_ALL)

        # check for bias
        for assumptions, ranges, percent in pack:
            print('\n---------------------------')
            print('1-Hot: {}'.format(
                ', '.join('{}'.format('|'.join('{}'.format(var) for var in case)) for (case, _) in assumptions)
            ))
            print('Ranges: {}'.format(
                ', '.join('{} ∈ [{}, {}]'.format(feature, lower, upper) for feature, (lower, upper) in ranges)
            ))
            print('---------------------------\n')
            partition = deepcopy(check)
            for states in partition.values():
                for state in states:
                    for (_, assumption) in assumptions:
                        state = state.assume({assumption})
                    # forget the sensitive variables
                    state = state.forget(self.sensitive)
            self.bias_check(partition, ranges, percent)

    def bias_check(self, check: Dict[Tuple[VariableIdentifier, VariableIdentifier], Set[BiasState]],
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
                                intersection = intersection.assume({conj})
                            # for assumption in assumptions0:
                            #     intersection = intersection.assume(assumption)
                            representation = repr(intersection.polka)
                            if not representation.startswith('-1.0 >= 0') and not representation == '⊥':
                                nobias = False
                                if representation not in biases:
                                    biases.add(representation)
                                    print(Fore.RED + '✘ Bias Found! : {}'.format(representation), Style.RESET_ALL)
        if nobias:
            self.unbiased += percent
            print(Fore.GREEN + '✔︎ No Bias', Style.RESET_ALL)
        else:
            self.biased += percent

    def pick(self,
             assumptions,                                           # (initially empty)
             pivot1: int,                                           # (initially 0)
             ranges: Dict[VariableIdentifier, Tuple[float, float]],     #
             pivot2: int,                                           # (initially 0)
             splittable: Set[VariableIdentifier],                   # (initially containing all custom encoded features)
             percent: float,                                        # percentage being analyzed (initially 100)
             key=None,
             do=False):
        print(Fore.LIGHTMAGENTA_EX + '\n---------------------------')
        print('1-Hot: {}'.format(
            ', '.join('{}'.format('|'.join('{}'.format(var) for var in case)) for (case, _) in assumptions)
        ))
        print('Ranges: {}'.format(
            ', '.join('{} ∈ [{}, {}]'.format(feature, lower, upper) for feature, (lower, upper) in ranges.items())
        ))
        print('---------------------------\n', Style.RESET_ALL)

        # bound the custom encoded uncontroversial features between their current lower and upper bounds
        bounds = self.bounds
        for feature, (lower, upper) in ranges.items():
            left = BinaryComparisonOperation(Literal(str(lower)), BinaryComparisonOperation.Operator.LtE, feature)
            right = BinaryComparisonOperation(feature, BinaryComparisonOperation.Operator.LtE, Literal(str(upper)))
            conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
            bounds = BinaryBooleanOperation(bounds, BinaryBooleanOperation.Operator.And, conj)

        entry = self.initial.precursory.assume({bounds})
        # take into account the accumulated assumptions on the one-hot encoded uncontroversial features
        for (_, assumption) in assumptions:
            entry = entry.assume({assumption})
        # find the (abstract) activation patterns corresponding to each possible value of the sensitive feature
        feasibility_and_patterns = self.feasibility_and_patterns(entry, key=key, do=do)
        feasible: bool = feasibility_and_patterns[0]
        # perform the analysis, if feasible, or partition the space of values of all the uncontroversial features
        if feasible or do:
            if feasible:
                self.partitions += 1
                self.feasible += percent
                self.epaths += feasibility_and_patterns[2]
            patterns: List[Tuple[Tuple[VariableIdentifier, BinaryBooleanOperation], Set[Node], Set[Node], Set[Node]]] = feasibility_and_patterns[1]
            key = list()
            for _, self.activations, active, inactive in patterns:
                key.append((frozenset(active), frozenset(inactive)))

            value = (frozenset(assumptions), frozenset(ranges.items()), percent)
            self.patterns[tuple(key)].add(value)    # self.partitions

            # # pick outcome
            # check: Dict[Tuple[VariableIdentifier, VariableIdentifier], Set[BiasState]] = dict()
            # for chosen in self.outputs:
            #     print(Fore.BLUE + 'Outcome: {}\n'.format(chosen), Style.RESET_ALL)
            #     remaining = self.outputs - {chosen}
            #     discarded = remaining.pop()
            #     outcome = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
            #     for discarded in remaining:
            #         cond = BinaryComparisonOperation(discarded, BinaryComparisonOperation.Operator.Lt, chosen)
            #         outcome = BinaryBooleanOperation(outcome, BinaryBooleanOperation.Operator.And, cond)
            #     result = self.initial.assume({outcome}, bwd=True)
            #     # pick value of the sensitive feature
            #     for ((case, value), self.activations, self.active, self.inactive) in patterns:
            #         check[(chosen, case)] = set()
            #         print('--------- {} --------- '.format(case).replace('x014', 'male').replace('x015', 'female'))
            #         print('activations: {{{}}}'.format(
            #             ', '.join('{}'.format(activation) for activation in self.activations)
            #         ))
            #         print('active: {{{}}}'.format(', '.join('{}'.format(active) for active in self.active)))
            #         print('inactive: {{{}}}'.format(', '.join('{}'.format(inactive) for inactive in self.inactive)))
            #         disjunctions = len(self.activations) - len(self.active) - len(self.inactive)
            #         paths = 2 ** disjunctions
            #         print('Paths: {}\n'.format(paths))
            #         # run the bias analysis
            #         start = time.time()
            #         progress = 0
            #         joined = deepcopy(result).bottom()
            #         for state in self.proceed(self.cfg.out_node, deepcopy(result), list(), do):
            #             progress += 1
            #             # if progress % 500 == 0:
            #             #     print('\nProgress: {}/{}'.format(progress, paths), 'Time: {}s'.format(time.time() - start))
            #             if state:
            #                 state = state.assume({value})
            #                 # state = state.assume({bounds}).assume({value})
            #                 for (_, assumption) in assumptions:
            #                     state = state.assume({assumption})
            #
            #                 # for feature, (lower, upper) in ranges.items():
            #                 #     lte = BinaryComparisonOperation.Operator.LtE
            #                 #     left = BinaryComparisonOperation(Literal(str(lower)), lte, feature)
            #                 #     right = BinaryComparisonOperation(feature, lte, Literal(str(upper)))
            #                 #     conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
            #                 #     state = state.assume({conj})
            #
            #                 # forget the sensitive variables
            #                 state = state.forget(self.sensitive)
            #                 # for encoding in self.uncontroversial1:
            #                 #     state = state.forget(encoding)
            #
            #                 if debug:
            #                     representation = repr(state.polka)
            #                 # if not representation.startswith('-1.0 >= 0'):
            #                 check[(chosen, case)].add(state)
            #                 joined = joined.join(state)
            #                 if debug:
            #                     print(representation)
            #                     print('Time: {}s\n'.format(time.time() - start))
            #         print('Joined: {}\n'.format(joined))
            #         # check[(chosen, case)] = joined
            #     print('---------\n')
            # # check for bias
            # self.bias_check(check, ranges, percent)
            print(Fore.YELLOW + 'Progress: {}% of {}%'.format(self.feasible, self.explored), Style.RESET_ALL)
        else:       # too many disjunctions, we need to split further
            print('Too many disjunctions!')

            if pivot1 < len(self.uncontroversial1):     # we still have to split the one-hot encoded
                print('1-hot splitting for: {}'.format(
                    ' | '.join(', '.join('{}'.format(var) for var in encoding) for encoding in self.uncontroversial1)
                ))

                OneHot1: Tuple[VariableIdentifier, BinaryBooleanOperation]          # one-hot value for 1 feature
                OneHotN: Tuple[OneHot1, ...]                                        # one-hot values for n features
                one_hots: List[OneHotN] = list(itertools.product(*(self.one_hots(encoding) for encoding in self.uncontroversial1)))

                # pack one_hots
                Key: Tuple[Tuple[Set[Node], Set[Node]], ...]
                packs: Dict[Key, Set[OneHotN]] = defaultdict(set)
                entry = self.initial.precursory.assume({bounds})
                for (_, assumption) in assumptions:
                    entry = entry.assume({assumption})
                for one_hot in one_hots:
                    result1 = deepcopy(entry)
                    for item in one_hot:
                        result1 = result1.assume({item[1]})

                    key = list()
                    for value in self.values:
                        result2 = deepcopy(result1).assume({value[1]})
                        _, active, inactive = self.precursory.analyze(result2)
                        # print(Fore.YELLOW + '--------- {}, {} --------- '.format(', '.join('{}'.format(item[0]) for item in one_hot), value[0]).replace('x014', 'male').replace('x015', 'female'))
                        # print('active: {{{}}}'.format(', '.join('{}'.format(active) for active in active)))
                        # print('inactive: {{{}}}'.format(', '.join('{}'.format(inactive) for inactive in inactive)))
                        # print('score: {}'.format(len(active) + len(inactive)))
                        key.append((frozenset(active), frozenset(inactive)))
                    packs[tuple(key)].add(one_hot)
                print(Fore.YELLOW + '\nPacks:')
                score = lambda k: sum(len(s[0]) + len(s[1]) for s in k)
                for key, pack in sorted(packs.items(), key=lambda v: score(v[0]) + len(v[1]), reverse=True):
                    sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
                    skey = ' | '.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
                    sscore = '(score: {})'.format(score(key) + len(pack))
                    spack = ' | '.join('{}'.format(','.join('{}'.format(item[0]) for item in one_hot)) for one_hot in pack)
                    print(Fore.YELLOW, skey, '->', spack, sscore, Style.RESET_ALL)

                # # run the analysis on each one_hot combination at the time
                # for one_hot in one_hots:
                #     _assumptions = assumptions.copy()
                #     for item in one_hot:
                #         _assumptions.add((frozenset({item[0]}), item[1]))
                #     self.pick(_assumptions, len(self.uncontroversial1), ranges, pivot2, splittable, percent / len(one_hots))

                # run the analysis on the ranked packs
                score = lambda k: sum(len(s[0]) + len(s[1]) for s in k)
                for key, pack in sorted(packs.items(), key=lambda v: score(v[0]) + len(v[1]), reverse=True):
                    _assumptions = assumptions.copy()
                    items: List[OneHotN] = list(pack)       # multiple one-hot values for n features
                    for i in range(len(items[0])):          # for each feature...
                        vars: Set[VariableIdentifier] = set()
                        var, case = items[0][i]
                        vars.add(var)
                        for item in items[1:]:
                            var, nxt = item[i]
                            vars.add(var)
                            case = BinaryBooleanOperation(case, BinaryBooleanOperation.Operator.Or, nxt)
                        _assumptions.add((frozenset(vars), case))
                    newpercent = percent * len(pack) / len(one_hots)
                    self.pick(_assumptions, len(self.uncontroversial1), ranges, pivot2, splittable, newpercent, key=key)

            else:       # we can split the rest
                if self.uncontroversial2 and splittable:
                    (lower, upper) = ranges[self.uncontroversial2[pivot2]]
                    if upper - lower <= self.difference:
                        print('Cannot range split for {} anymore!'.format(self.uncontroversial2[pivot2]))
                        remained = splittable.copy()
                        remained.remove(self.uncontroversial2[pivot2])
                        self.pick(assumptions, pivot1, ranges, (pivot2 + 1) % len(self.uncontroversial2), remained, percent)
                    else:
                        middle = lower + (upper - lower) / 2
                        print('Range split for {} at: {}'.format(self.uncontroversial2[pivot2], middle))
                        left = deepcopy(ranges)
                        left[self.uncontroversial2[pivot2]] = (lower, middle)
                        right = deepcopy(ranges)
                        right[self.uncontroversial2[pivot2]] = (middle, upper)
                        newpercent = percent / 2
                        self.pick(assumptions, pivot1, left, (pivot2 + 1) % len(self.uncontroversial2), splittable, newpercent)
                        self.pick(assumptions, pivot1, right, (pivot2 + 1) % len(self.uncontroversial2), splittable, newpercent)
                else:
                    self.unfeasible += percent
                    self.ipaths += feasibility_and_patterns[2]
                    print(Fore.LIGHTRED_EX + 'Stopping here!', Style.RESET_ALL)
                    print(Fore.YELLOW + 'Progress: {}% of {}%'.format(self.feasible, self.feasible + self.unfeasible), Style.RESET_ALL)
                    # self.pick(assumptions, pivot1, ranges, pivot2, splittable, percent, do=True)

    def proceed(self, node, initial, path, join):
        if debug:
            print('node: ', node)
        state = initial

        if isinstance(node, Function):
            state = self.semantics.list_semantics(node.stmts, state)
            if debug:
                print(state)
            if state.is_bottom():
                yield None
            else:
                predecessors = self.cfg.predecessors(node)
                if predecessors:
                    yield from self.proceed(self.cfg.nodes[self.cfg.predecessors(node).pop()], state, path, join)
                else:
                    yield state
        elif isinstance(node, Activation):
            if node in self.active:  # only the active path is viable
                if debug:
                    print('active')
                state = self.semantics.ReLU_call_semantics(node.stmts, state, True)
                if state.is_bottom():
                    yield None
                else:
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    active_path = path + ['{}+{}'.format(node, predecessor)]
                    if debug:
                        print('/active')
                    yield from self.proceed(predecessor, state, active_path, join)
            elif node in self.inactive:  # only the inactive path is viable
                if debug:
                    print('inactive')
                state = self.semantics.ReLU_call_semantics(node.stmts, state, False)
                # left = node.stmts[0].arguments[0].variable
                # right = Literal('0')
                # state = state.substitute({left}, {right})
                if debug:
                    print(state)
                if state.is_bottom():
                    yield None
                else:
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    inactive_path = path + ['{}-{}'.format(node, predecessor)]
                    if debug:
                        print('/inactive')
                    yield from self.proceed(predecessor, state, inactive_path, join)
            else:  # both paths are viable
                if debug:
                    print('both')
                active, inactive = deepcopy(state), deepcopy(state)
                # state1 = deepcopy(state)
                # left = node.stmts[0].arguments[0].variable
                # right = Literal('0')
                # state2 = deepcopy(state).substitute({left}, {right})
                state1 = self.semantics.ReLU_call_semantics(node.stmts, active, True)
                if debug:
                    print(state1)
                state2 = self.semantics.ReLU_call_semantics(node.stmts, inactive, False)
                if debug:
                    print(state2)
                if join:
                    if debug:
                        print('join')
                    state = state1.join(state2)
                    predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                    join_path = path + ['{}*{}'.format(node, predecessor)]
                    if debug:
                        print('/join')
                    yield from self.proceed(predecessor, state, join_path, join)
                else:
                    if state1.is_bottom():
                        if state2.is_bottom():
                            yield None
                        else:
                            predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                            inactive_path = path + ['{}-{}'.format(node, predecessor)]
                            yield from self.proceed(predecessor, state2, inactive_path, join)
                    else:
                        predecessor = self.cfg.nodes[self.cfg.predecessors(node).pop()]
                        active_path = path + ['{}+{}'.format(node, predecessor)]
                        yield from self.proceed(predecessor, state1, active_path, join)
                        if state2.is_bottom():
                            yield None
                        else:
                            inactive_path = path + ['{}-{}'.format(node, predecessor)]
                            yield from self.proceed(predecessor, state2, inactive_path, join)
        else:
            # stop = False
            # for stmt in reversed(node.stmts):
            #     state = self.semantics.semantics(stmt, state)
            #     if state.is_bottom():
            #         stop = True
            #         break
            # if stop:
            #     yield None
            # else:
            predecessors = self.cfg.predecessors(node)
            if predecessors:
                yield from self.proceed(self.cfg.nodes[self.cfg.predecessors(node).pop()], state, path, join)
            else:
                yield state

    def one_hots(self, variables: List[VariableIdentifier]) -> Set[Tuple[VariableIdentifier, BinaryBooleanOperation]]:
        """Compute all possible one-hots for a given list of variables.

        :param variables: list of variables one-hot encoding a categorical input feature
        :return: set of Libra expressions corresponding to each possible value of the one-hot encoding
        (paired with the variable being one in the encoded value for convenience ---
        the variable is the first element of the tuple)
        """
        values: Set[Tuple[VariableIdentifier, BinaryBooleanOperation]] = set()
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

    def analyze(self, initial: BiasState,
                inputs: Set[VariableIdentifier] = None,                             # input variables
                outputs: Set[VariableIdentifier] = None,                            # output variables
                splits: Dict[int, Dict[VariableIdentifier, PyTexpr1]] = None,       # partitioning information
                relus: Dict[VariableIdentifier, Node] = Node):                      # relus information
        self._initial = initial
        """
        pick sensitive feature and fix its bounds / we assume one-hot encoding
        """
        arity = int(input('Arity of the sensitive feature?\n'))
        self.sensitive = list()
        for i in range(arity):
            self.sensitive.append(VariableIdentifier(input('Sensitive input:\n')))
        self.values: List[Tuple[VariableIdentifier, BinaryBooleanOperation]] = list(self.one_hots(self.sensitive))
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
                arity = input('Arity of the feature?\n')
                uncontroversial = list()
                for i in range(int(arity)):
                    uncontroversial.append(VariableIdentifier(input('Input:\n')))
                self.uncontroversial1.append(uncontroversial)
            except EOFError:
                break
        # bound the one-hot encoded uncontroversial features between 0 and 1
        for encoding in self.uncontroversial1:
            for uncontroversial in encoding:
                left = BinaryComparisonOperation(zero, BinaryComparisonOperation.Operator.LtE, uncontroversial)
                right = BinaryComparisonOperation(uncontroversial, BinaryComparisonOperation.Operator.LtE, one)
                conj = BinaryBooleanOperation(left, BinaryBooleanOperation.Operator.And, right)
                self.bounds = BinaryBooleanOperation(self.bounds, BinaryBooleanOperation.Operator.And, conj)
        """
        determine the custom encoded uncontroversial features and fix their bounds  # (initial) ranges
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
        """
        determine the output classes
        """
        self.outputs = outputs
        """
        do the analysis
        """
        self.splits = splits
        self.affines = list(splits[self.layer].keys())
        self.relus = relus

        print(Fore.BLUE + '\n||==============||')
        print('|| Pre-Analysis ||')
        print('||==============||', Style.RESET_ALL)

        self.pick(set(), 0, ranges, 0, set(self.uncontroversial2), 100)
        # self.pick2(1, 0, set(), set(), set(), set(), set(), 0, set(), 0, set(self.uncontroversial2), ranges, 100)

        pattnum = len(self.patterns)
        print(Fore.BLUE + '\nFound: {} patterns for {} partitions'.format(pattnum, self.partitions), Style.RESET_ALL)
        # for key, pack in self.patterns.items():
        #     sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
        #     skey = ' | '.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
        #     print(Fore.YELLOW, skey, '->', sset(pack), Style.RESET_ALL)

        print(Fore.BLUE + '\n||==========||')
        print('|| Analysis ||')
        print('||==========||', Style.RESET_ALL)

        for idx, (key, pack) in enumerate(self.patterns.items()):
            sset = lambda s: '{{{}}}'.format(', '.join('{}'.format(e) for e in s))
            skey = '\n'.join('{}, {}'.format(sset(pair[0]), sset(pair[1])) for pair in key)
            print(Fore.LIGHTMAGENTA_EX + '\n===========================')
            print('Pack #{} of {} [{}]'.format(idx+1, len(self.patterns), len(pack)))

            self.doit(key, pack)
            print(Fore.YELLOW + 'Progress: {} of {} patterns ({}% biased)'.format(idx+1, pattnum, self.biased), Style.RESET_ALL)

        print(Fore.BLUE + '\nResult: {}% of {}% ({}% biased)'.format(self.feasible, self.explored, self.biased))
        print('Done!')


class BiasBackwardSemantics(DefaultBackwardSemantics):

    def list_semantics(self, stmt, state) -> State:
        # lhss = [self.semantics(assignment.left, state).result for assignment in stmt]
        # rhss = [self.semantics(assignment.right, state).result for assignment in stmt]
        # return state.substitute(lhss, rhss)
        state.polka = state.polka.substitute(stmt[0], stmt[1])
        # state.mirror = state.mirror.substitute(stmt[0], stmt[1])
        return state

    def ReLU_call_semantics(self, stmt, state, active: bool = True) -> State:
        # assert len(stmt.arguments) == 1  # exactly one argument is expected
        # argument = stmt.arguments[0]
        # assert isinstance(argument, VariableAccess)
        # left = argument.variable
        # right = Literal('0')
        if active:  # assume h >= 0
            # cond = {BinaryComparisonOperation(left, BinaryComparisonOperation.Operator.GtE, right)}
            # return state.assume(cond)
            expr = PyTexpr1.var(state.environment, stmt)
            cond = PyTcons1.make(expr, ConsTyp.AP_CONS_SUPEQ)
            abstract1 = PyPolkaMPQstrict(state.environment, array=PyTcons1Array([cond]))
            state.polka = state.polka.meet(abstract1)
            # state.mirror = state.mirror.meet(abstract1)
            return state
        else:  # assign h = 0, assume h < 0
            # cond = {BinaryComparisonOperation(left, BinaryComparisonOperation.Operator.Lt, right)}
            # return state.substitute({left}, {right}).assume(cond)
            expr = PyTexpr1.var(state.environment, stmt)
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            neg = PyTexpr1.binop(TexprOp.AP_TEXPR_SUB, zero, expr, rtype, rdir)
            cond = PyTcons1.make(neg, ConsTyp.AP_CONS_SUP)
            abstract1 = PyPolkaMPQstrict(state.environment, array=PyTcons1Array([cond]))
            zero = PyTexpr1.cst(state.environment, PyMPQScalarCoeff(0.0))
            state.polka = state.polka.substitute(stmt, zero).meet(abstract1)
            # state.mirror = state.mirror.substitute(stmt, zero).meet(abstract1)
            return state


class BiasAnalysis(Runner):

    def __init__(self):
        super().__init__()
        self.inputs: Set[VariableIdentifier] = None                             # input variables
        self.outputs: Set[VariableIdentifier] = None                            # output variables
        self.splits: Dict[int, Dict[VariableIdentifier, PyTexpr1]] = None       # partitioning information
        self.relus: Dict[VariableIdentifier, Node] = None                       # relus information

    def interpreter(self):
        precursory = ActivationPatternInterpreter(self.cfg, ActivationPatternForwardSemantics(), 3)
        return BiasInterpreter(self.cfg, BiasBackwardSemantics(), 2, precursory=precursory)

    def state(self):
        self.inputs, variables, self.outputs = self.variables
        precursory = BoxState(variables)
        # precursory = OctagonState(variables)
        # precursory = PolyhedraState(variables)
        # precursory = Taylor1pMPQState(variables)
        min_int = (-ctypes.c_uint(-1).value) // 2
        PyPolkaMPQstrict.manager.contents.option.funopt[FunId.AP_FUNID_IS_BOTTOM].algorithm = min_int
        PyPolkaMPQstrict.manager.contents.option.funopt[FunId.AP_FUNID_IS_TOP].algorithm = min_int
        PyPolkaMPQstrict.manager.contents.option.funopt[FunId.AP_FUNID_MEET].algorithm = min_int
        PyPolkaMPQstrict.manager.contents.option.funopt[FunId.AP_FUNID_JOIN].algorithm = min_int
        PyPolkaMPQstrict.manager.contents.option.funopt[FunId.AP_FUNID_FORGET_ARRAY].algorithm = min_int
        return BiasState(variables, precursory=precursory)

    @property
    def variables(self):
        variables, assigned, outputs = set(), set(), set()
        worklist = Queue()
        worklist.put(self.cfg.in_node)
        while not worklist.empty():
            current = worklist.get()
            for stmt in current.stmts:
                variables = variables.union(stmt.ids())
                if isinstance(stmt, Assignment):
                    assigned = assigned.union(stmt.left.ids())
                    outputs = outputs.union(stmt.left.ids())
            if isinstance(current, Activation):  # there is another layer
                outputs = set()
            for node in self.cfg.successors(current):
                worklist.put(node)
        return variables.difference(assigned), variables, outputs

    _lyra2apron = Lyra2APRON()

    def lyra2apron(self, environment):
        splits: Dict[int, Dict[VariableIdentifier, PyTexpr1]] = dict()
        relus: Dict[VariableIdentifier, Node] = dict()
        layer: int = 1
        worklist = Queue()
        worklist.put(self.cfg.in_node)
        while not worklist.empty():
            current: Node = worklist.get()  # retrieve the current node
            # execute block
            if isinstance(current, Function):
                affine: Dict[VariableIdentifier, PyTexpr1] = dict()
                vars = list()
                exprs = list()
                for assignment in current.stmts:
                    variable, expression = self._lyra2apron.visit(assignment, environment)
                    affine[assignment.left.variable] = expression
                    vars.append(variable)
                    exprs.append(expression)
                splits[layer] = affine
                layer += 1
                newnode = Function(current.identifier, (vars, exprs))
                self.cfg.nodes[current.identifier] = newnode
            elif isinstance(current, Activation):
                relus[current.stmts[0].arguments[0].variable] = current
                variable = self._lyra2apron.visit(current.stmts[0], environment)
                newnode = Activation(current.identifier, variable)
                self.cfg.nodes[current.identifier] = newnode
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(node)
        # delete last added layer because there are no ReLUs there
        del splits[layer - 1]
        return splits, relus

    def main(self, path):
        self.path = path
        with open(self.path, 'r') as source:
            self.source = source.read()
            self.tree = ast.parse(self.source)
            self.cfg = ast_to_cfg(self.tree)
            # # rendering of the original CFG
            # renderer = CFGRenderer()
            # data = self.cfg
            # name = os.path.splitext(os.path.basename(self.path))[0]
            # label = f"CFG for {name}"
            # directory = os.path.dirname(self.path)
            # renderer.render(data, filename=name, label=label, directory=directory, view=True)
            # walking over the CFG to convert statements to APRON and to collect partitioning information
            _, variables, _ = self.variables
            r_vars = list()
            for variable in variables:
                r_vars.append(PyVar(variable.name))
            environment = PyEnvironment([], r_vars)
            self.splits, self.relus = self.lyra2apron(environment)
        self.run()

    def run(self):
        start = time.time()
        self.interpreter().analyze(self.state(), inputs=self.inputs, outputs=self.outputs, splits=self.splits, relus=self.relus)
        end = time.time()
        print('Total: {}s'.format(end - start), Style.RESET_ALL)
