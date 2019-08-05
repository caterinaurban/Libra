"""
Interval Analysis
=================

:Author: Caterina Urban
"""
from apronpy.manager import PyBoxMPQManager

from libra.engine.backward import BackwardInterpreter
from libra.engine.forward import ForwardInterpreter
from libra.engine.runner import Runner
from libra.semantics.backward import DefaultBackwardSemantics
from libra.semantics.forward import DefaultForwardSemantics

from libra.abstract_domains.numerical.interval_domain import IntervalState, BoxState


class ForwardIntervalAnalysis(Runner):

    def interpreter(self):
        return ForwardInterpreter(self.cfg, DefaultForwardSemantics(), 3)

    def state(self):
        return IntervalState(self.variables)


class ForwardBoxAnalysis(Runner):

    def interpreter(self):
        return ForwardInterpreter(self.cfg, PyBoxMPQManager(), DefaultForwardSemantics(), 3)

    def state(self):
        return BoxState(PyBoxMPQManager(), self.variables)


class BackwardIntervalAnalysis(Runner):

    def interpreter(self):
        return BackwardInterpreter(self.cfg, DefaultBackwardSemantics(), 3)

    def state(self):
        return IntervalState(self.variables)


class BackwardBoxAnalysis(Runner):

    def interpreter(self):
        return BackwardInterpreter(self.cfg, DefaultBackwardSemantics(), 3)

    def state(self):
        return BoxState(self.variables)
