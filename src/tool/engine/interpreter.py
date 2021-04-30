"""
Analysis Engine
===============

:Author: Anonymous
"""

from abc import ABCMeta, abstractmethod

from tool.core.cfg import ControlFlowGraph
from tool.engine.result import AnalysisResult

from tool.abstract_domains.state import State
from tool.semantics.semantics import Semantics


class Interpreter(metaclass=ABCMeta):
    def __init__(self, cfg: ControlFlowGraph, semantics, precursory=None):
        """Control flow graph interpreter.

        :param cfg: control flow graph to analyze
        :param semantics: semantics of statements in the control flow graph
        :param precursory: precursory control flow graph interpreter
        """
        self._result = AnalysisResult(cfg)
        self._semantics: Semantics = semantics
        self._precursory: 'Interpreter' = precursory

    @property
    def cfg(self):
        return self.result.cfg

    @property
    def result(self):
        return self._result

    @property
    def semantics(self):
        return self._semantics

    @property
    def precursory(self):
        return self._precursory

    @abstractmethod
    def analyze(self, initial: State):
        """Run the analysis.

        :param initial: initial analysis state
        :return: result of the analysis
        """
