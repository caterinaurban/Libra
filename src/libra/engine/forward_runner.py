
import ast
from queue import Queue
from pip._vendor.colorama import Style
from typing import Set, Dict 
import time

from apronpy.manager import PyManager
from apronpy.box import PyBoxMPQManager
from apronpy.texpr1 import PyTexpr1
from apronpy.environment import PyEnvironment
from apronpy.var import PyVar
 
from libra.core.cfg import Node, Function, Activation
from libra.engine.bias_analysis import AbstractDomain
from libra.core.expressions import VariableIdentifier
from libra.engine.runner import Runner
from libra.abstract_domains.deeppoly_domain import DeepPolyState
from libra.abstract_domains.neurify_domain import NeurifyState
from libra.abstract_domains.interval_domain import BoxState
from libra.abstract_domains.product_domain import ProductState
from libra.abstract_domains.symbolic1_domain import Symbolic1State
from libra.abstract_domains.symbolic2_domain import Symbolic2State
from libra.core.statements import Assignment, Lyra2APRON
from libra.frontend.cfg_generator import ast_to_cfg
from libra.engine.forward import ForwardInterpreter, ActivationPatternForwardSemantics

class ForwardRunner(Runner):

    def __init__(self, spec, domain=AbstractDomain.SYMBOLIC2, difference=0.25, widening=2):
        super().__init__()
        self.spec = spec
        self.domain = domain
        self.difference = difference
        self.widening = widening

        self.outputs: Set[VariableIdentifier] = None                            # output variables
        self.man1: PyManager = PyBoxMPQManager() # legacy, for symbolic domain

    def interpreter(self):
        return ForwardInterpreter(self.cfg, self.man1, ActivationPatternForwardSemantics(), widening=self.widening)

    def state(self):
        inputs, variables, self.outputs = self.variables
        if self.domain == AbstractDomain.BOXES:
            state = BoxState(self.man1, variables)
        elif self.domain == AbstractDomain.SYMBOLIC1:
            # generally faster than SYMBOLIC2 for small neural networks
            state = Symbolic1State(self.man1, variables)
        elif self.domain == AbstractDomain.SYMBOLIC2:
            # generally faster than SYMBOLIC1 for large neural networks
            state = Symbolic2State(self.man1, variables)
        elif self.domain == AbstractDomain.DEEPPOLY:
            state = DeepPolyState(inputs)
        elif self.domain == AbstractDomain.PRODUCT:
            state = ProductState(inputs)
        else:
            assert self.domain == AbstractDomain.NEURIFY
            state = NeurifyState(inputs)
        return state

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
                layer += 1
                newnode = Function(current.identifier, (vars, exprs))
                self.cfg.nodes[current.identifier] = newnode
            elif isinstance(current, Activation):
                variable = self._lyra2apron.visit(current.stmts[0], environment)
                newnode = Activation(current.identifier, variable)
                self.cfg.nodes[current.identifier] = newnode
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(node)

    def main(self, path):
        self.path = path
        with open(self.path, 'r') as source:
            self.source = source.read()
            self.tree = ast.parse(self.source)
            self.cfg = ast_to_cfg(self.tree)

            _, variables, _ = self.variables
            r_vars = list()
            for variable in variables:
                r_vars.append(PyVar(variable.name))
            environment = PyEnvironment([], r_vars)
            self.lyra2apron(environment)
        self.run()

    def run(self):
        start = time.time()
        self.interpreter().analyze(self.state(), outputs=self.outputs)
        end = time.time()
        print('Total Time: {}s'.format(end - start), Style.RESET_ALL)
