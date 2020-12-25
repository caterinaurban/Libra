"""
Bias Abstract Domain: Product between DeepPoly and Neurify
============================

Disjunctive relation abstract domain to be used for **algorithmic bias analysis**.

"""
from typing import Set, List, Dict
from copy import deepcopy

from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar
from apronpy.manager import PyManager

from libra.abstract_domains.state import State
from libra.core.expressions import Lyra2APRON, NegationFreeExpression, VariableIdentifier, Expression, \
    BinaryComparisonOperation, BinaryBooleanOperation, Literal
from libra.abstract_domains.deeppoly_domain import IntervalLattice, texpr_to_dict, evaluate
from libra.core.utils import copy_docstring

LOW = 0
UP = 1

class ProductDeepPolyNeurifyState(State):

    """Neurify [Wang et al.] state.

    .. document private methods
    .. automethod:: DeepPolyState._assign
    .. automethod:: DeepPolyState._assume
    .. automethod:: DeepPolyState._output
    .. automethod:: DeepPolyState._substitute
    """
    def __init__(self, inputs: Set[VariableIdentifier], precursory: State = None):
        super().__init__(precursory=precursory)
        pass

    @copy_docstring(State.bottom)
    def bottom(self):
        pass

    @copy_docstring(State.top)
    def top(self):
        pass

    def __repr__(self):
        pass

    @copy_docstring(State.is_bottom)
    def is_bottom(self) -> bool:
        pass

    @copy_docstring(State.is_top)
    def is_top(self) -> bool:
        pass

    @copy_docstring(State._less_equal)
    def _less_equal(self, other: 'ProductDeepPolyNeurifyState') -> bool:
        raise NotImplementedError(f"Call to _is_less_equal is unexpected!")

    @copy_docstring(State._join)
    def _join(self, other: 'ProductDeepPolyNeurifyState') -> 'ProductDeepPolyNeurifyState':
        pass

    @copy_docstring(State._meet)
    def _meet(self, other: 'ProductDeepPolyNeurifyState') -> 'ProductDeepPolyNeurifyState':
        pass

    @copy_docstring(State._widening)
    def _widening(self, other: 'ProductDeepPolyNeurifyState') -> 'ProductDeepPolyNeurifyState':
        raise NotImplementedError(f"Call to _widening is unexpected!")

    @copy_docstring(State._assign)
    def _assign(self, left: Expression, right: Expression) -> 'ProductDeepPolyNeurifyState':
        raise NotImplementedError(f"Call to _assign is unexpected!")

    @copy_docstring(State._assume)
    def _assume(self, condition: Expression, bwd: bool = False) -> 'ProductDeepPolyNeurifyState':
        raise NotImplementedError(f"Call to _assume is unexpected!")

    def assume(self, condition, manager: PyManager = None, bwd: bool = False) -> 'ProductDeepPolyNeurifyState':
        pass

    @copy_docstring(State._substitute)
    def _substitute(self, left: Expression, right: Expression) -> 'ProductDeepPolyNeurifyState':
        raise NotImplementedError(f"Call to _substitute is unexpected!")

    def forget(self, variables: List[VariableIdentifier]) -> 'ProductDeepPolyNeurifyState':
        raise NotImplementedError(f"Call to _forget is unexpected!")

    def affine(self, left: List[PyVar], right: List[PyTexpr1]) -> 'ProductDeepPolyNeurifyState':
        pass

    def relu(self, stmt: PyVar, active: bool = False, inactive: bool = False) -> 'ProductDeepPolyNeurifyState':
        pass

    def outcome(self, outcomes: Set[VariableIdentifier]):
        pass

    _negation_free = NegationFreeExpression()
    _lyra2apron = Lyra2APRON()
