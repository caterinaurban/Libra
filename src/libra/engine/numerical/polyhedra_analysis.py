"""
Polyhedra Analysis
==================

:Author: Caterina Urban
"""
from libra.abstract_domains.numerical.polyhedra_domain import PolyhedraState
from libra.engine.backward import BackwardInterpreter
from libra.engine.forward import ForwardInterpreter
from libra.engine.runner import Runner
from libra.semantics.backward import DefaultBackwardSemantics
from libra.semantics.forward import DefaultForwardSemantics


class ForwardPolyhedraAnalysis(Runner):

    def interpreter(self):
        return ForwardInterpreter(self.cfg, DefaultForwardSemantics(), 3)

    def state(self):
        return PolyhedraState(self.variables)


class BackwardPolyhedraAnalysis(Runner):

    def interpreter(self):
        return BackwardInterpreter(self.cfg, DefaultBackwardSemantics(), 3)

    def state(self):
        return PolyhedraState(self.variables)
