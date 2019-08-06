"""
Bias Analysis
=============

:Author: Caterina Urban
"""
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
from libra.engine.backward import BackwardInterpreter, BiasBackwardSemantics
from libra.engine.forward import ForwardInterpreter, ActivationPatternForwardSemantics
from libra.engine.result import AnalysisResult
from libra.engine.runner import Runner
from libra.frontend.cfg_generator import ast_to_cfg
from libra.semantics.backward import DefaultBackwardSemantics
from libra.semantics.forward import DefaultForwardSemantics
from libra.visualization.graph_renderer import CFGRenderer



# debug = False


class BiasAnalysis(Runner):

    def __init__(self, spec, symbolic1=False, symbolic2=False, difference=0.25, widening=2):
        super().__init__()
        self.spec = spec
        self.symbolic1 = symbolic1
        self.symbolic2 = symbolic2
        self.difference = difference
        self.widening = widening

        self.inputs: Set[VariableIdentifier] = None                             # input variables
        self.outputs: Set[VariableIdentifier] = None                            # output variables
        self.activations: Set[Node] = None                                      # activations
        self.splits: Dict[int, Dict[VariableIdentifier, PyTexpr1]] = None       # partitioning information
        self.relus: Dict[VariableIdentifier, Node] = None                       # relus information
        self.man1: PyManager = PyBoxMPQManager()
        self.man2: PyManager = PyPolkaMPQstrictManager()
        min_int = (-ctypes.c_uint(-1).value) // 2
        self.man2.manager.contents.option.funopt[FunId.AP_FUNID_IS_BOTTOM].algorithm = min_int
        self.man2.manager.contents.option.funopt[FunId.AP_FUNID_IS_TOP].algorithm = min_int
        self.man2.manager.contents.option.funopt[FunId.AP_FUNID_MEET].algorithm = min_int
        self.man2.manager.contents.option.funopt[FunId.AP_FUNID_JOIN].algorithm = min_int
        self.man2.manager.contents.option.funopt[FunId.AP_FUNID_FORGET_ARRAY].algorithm = min_int

    def interpreter(self):
        precursory = ForwardInterpreter(self.cfg, self.man1, ActivationPatternForwardSemantics(), symbolic1=self.symbolic1, symbolic2=self.symbolic2)
        return BackwardInterpreter(self.cfg, self.man2, BiasBackwardSemantics(), self.spec, widening=self.widening, difference=self.difference, precursory=precursory)

    def state(self):
        self.inputs, variables, self.outputs = self.variables
        precursory = BoxState(self.man1, variables)
        # precursory = OctagonState(variables)
        # precursory = PolyhedraState(variables)
        # precursory = Taylor1pMPQState(variables)
        return BiasState(self.man2, variables, precursory=precursory)

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
        activations = set()
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
                activations.add(current)
                relus[current.stmts[0].arguments[0].variable] = current
                variable = self._lyra2apron.visit(current.stmts[0], environment)
                newnode = Activation(current.identifier, variable)
                self.cfg.nodes[current.identifier] = newnode
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(node)
        # delete last added layer because there are no ReLUs there
        del splits[layer - 1]
        return activations, splits, relus

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
            self.activations, self.splits, self.relus = self.lyra2apron(environment)
        self.run()

    def run(self):
        start = time.time()
        self.interpreter().analyze(self.state(), inputs=self.inputs, outputs=self.outputs, activations=self.activations)
        end = time.time()
        print('Total: {}s'.format(end - start), Style.RESET_ALL)
