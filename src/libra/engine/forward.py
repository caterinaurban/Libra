"""
Forward Analysis Engine
=======================

:Author: Caterina Urban
"""
from copy import deepcopy
from queue import Queue

from apronpy.manager import PyManager

from libra.core.statements import Call
from libra.engine.interpreter import Interpreter
from libra.semantics.forward import DefaultForwardSemantics

from libra.abstract_domains.state import State
from libra.core.cfg import Node, Function, Activation


class ForwardInterpreter(Interpreter):
    """Forward control flow graph interpreter."""

    def __init__(self, cfg, manager: PyManager, semantics, widening=3, symbolic1=False, symbolic2=False):
        """Forward control flow graph interpreter construction.

        :param cfg: control flow graph to analyze
        :param semantics: semantics of statements in the control flow graph
        :param widening: number of iterations before widening
        :param precursory: precursory control flow graph interpreter
        """
        super().__init__(cfg, semantics, widening)
        self.manager = manager
        self.symbolic1 = symbolic1
        self.symbolic2 = symbolic2

    def analyze(self, initial, earlystop=True, forced_active=None, forced_inactive=None, outputs=None):
        """Forward analysis extracting abstract activation patterns.

        :param initial: initial state of the analysis
        :return: three sets: all activation nodes, always active nodes, always inactive nodes
        """
        worklist = Queue()
        worklist.put(self.cfg.in_node)
        state = deepcopy(initial)
        activated, deactivated = set(), set()

        while not worklist.empty():
            current: Node = worklist.get()  # retrieve the current node
            # execute block
            if isinstance(current, Function):
                state = state.affine(current.stmts[0], current.stmts[1])
            elif isinstance(current, Activation):
                if forced_active and current in forced_active:
                    state = state.relu(current.stmts, active=True)
                    activated.add(current)
                elif forced_inactive and current in forced_inactive:
                    state = state.relu(current.stmts, inactive=True)
                    deactivated.add(current)
                else:
                    state = state.relu(current.stmts)
                    if state.is_bottom():
                        deactivated.add(current)
                    if state.flag:
                        if state.flag > 0:
                            activated.add(current)
                        else:
                            deactivated.add(current)
            else:
                for stmt in reversed(current.stmts):
                    state = self.semantics.assume_call_semantics(stmt, state, self.manager)
            # update worklist
            for node in self.cfg.successors(current):
                worklist.put(self.cfg.nodes[node.identifier])

        found = state.outcome(outputs)

        return activated, deactivated, found


class ActivationPatternForwardSemantics(DefaultForwardSemantics):

    def assume_call_semantics(self, stmt: Call, state: State, manager: PyManager = None) -> State:
        argument = self.semantics(stmt.arguments[0], state).result
        state.assume(argument, manager=manager)
        state.result = set()
        return state
