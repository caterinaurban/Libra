"""
Bias Abstract Domain: Product between DeepPoly and Neurify
============================

Disjunctive relation abstract domain to be used for **algorithmic bias analysis**.

"""
from typing import Set, List, Dict

from apronpy.texpr1 import PyTexpr1
from apronpy.var import PyVar
from apronpy.manager import PyManager

from libra.abstract_domains.deeppoly_domain import IntervalLattice
from libra.abstract_domains.state import State
from libra.core.expressions import Lyra2APRON, NegationFreeExpression, VariableIdentifier, Expression
from libra.core.utils import copy_docstring
from libra.abstract_domains.bounds_domain import BoundsDomain

class ProductState(State):

    """
    .. document private methods
    .. automethod:: DeepPolyState._assign
    .. automethod:: DeepPolyState._assume
    .. automethod:: DeepPolyState._output
    .. automethod:: DeepPolyState._substitute
    """
    def __init__(self, inputs: Set[VariableIdentifier], domain1, domain2, precursory: State = None):
        super().__init__(precursory=precursory)

        assert(isinstance(domain1, BoundsDomain) and isinstance(domain1, State))
        assert(isinstance(domain2, BoundsDomain) and isinstance(domain2, State))

        self._domain1 = domain1
        self._domain2 = domain2

        self.inputs = {k.name for k in inputs}
        self.bounds = dict()
        for k in self.inputs:
            self.bounds[k] = IntervalLattice(0, 1)

        self.flag = None

    @copy_docstring(State.bottom)
    def bottom(self):
        self._domain1.bottom()
        self._domain2.bottom()
        return self

    @copy_docstring(State.top)
    def top(self):
        self._domain1.top()
        self._domain2.top()
        return self

    def __repr__(self):
        items = sorted(self.bounds.items(), key=lambda x: x[0])
        return ", ".join("{} -> {}".format(variable, value) for variable, value in items)

    @copy_docstring(State.is_bottom)
    def is_bottom(self) -> bool:
        return self._domain1.is_bottom() or self._domain2.is_bottom()

    @copy_docstring(State.is_top)
    def is_top(self) -> bool:
        return self._domain1.is_top() and self._domain2.is_top()

    @copy_docstring(State._less_equal)
    def _less_equal(self, other: 'ProductState') -> bool:
        raise NotImplementedError(f"Call to _is_less_equal is unexpected!")

    @copy_docstring(State._join)
    def _join(self, other: 'ProductState') -> 'ProductState':
        self._domain1._join(other._domain1)
        self._domain2._join(other._domain2)
        return self

    @copy_docstring(State._meet)
    def _meet(self, other: 'ProductState') -> 'ProductState':
        self._domain1._meet(other._domain1)
        self._domain2._meet(other._domain2)
        return self

    @copy_docstring(State._widening)
    def _widening(self, other: 'ProductState') -> 'ProductState':
        raise NotImplementedError(f"Call to _widening is unexpected!")

    @copy_docstring(State._assign)
    def _assign(self, left: Expression, right: Expression) -> 'ProductState':
        raise NotImplementedError(f"Call to _assign is unexpected!")

    @copy_docstring(State._assume)
    def _assume(self, condition: Expression, bwd: bool = False) -> 'ProductState':
        raise NotImplementedError(f"Call to _assume is unexpected!")

    def assume(self, condition, manager: PyManager = None, bwd: bool = False) -> 'ProductState':
        self._domain1.assume(condition, manager, bwd)
        self._domain2.assume(condition, manager, bwd)
        return self

    @copy_docstring(State._substitute)
    def _substitute(self, left: Expression, right: Expression) -> 'ProductState':
        raise NotImplementedError(f"Call to _substitute is unexpected!")

    def forget(self, variables: List[VariableIdentifier]) -> 'ProductState':
        raise NotImplementedError(f"Call to _forget is unexpected!")

    def _share_bounds(self, var_name):
        self.bounds[var_name] = IntervalLattice(
            max(self._domain1.get_bounds(var_name).lower, self._domain2.get_bounds(var_name).lower),
            min(self._domain1.get_bounds(var_name).upper, self._domain2.get_bounds(var_name).upper),
        )
        self._domain1.resize_bounds(var_name, self.bounds[var_name])
        self._domain2.resize_bounds(var_name, self.bounds[var_name])

    def affine(self, left: List[PyVar], right: List[PyTexpr1]) -> 'ProductState':
        self._domain1.affine(left, right)
        self._domain2.affine(left, right)

        for lhs in left:
            self._share_bounds(str(lhs))

        return self

    def relu(self, stmt: PyVar, active: bool = False, inactive: bool = False) -> 'ProductState':
        self._domain1.relu(stmt, active, inactive)
        self._domain2.relu(stmt, active, inactive)

        self._share_bounds(str(stmt))

        return self

    def outcome(self, outcomes: Set[VariableIdentifier]):
        found = None
        if self.is_bottom():
            found = '⊥'
        else:
            for chosen in outcomes:
                outcome = self.bounds[chosen.name]
                lower = outcome.lower
                unique = True
                remaining = outcomes - {chosen}
                for discarded in remaining:
                    alternative = self.bounds[discarded.name]
                    upper = alternative.upper
                    if lower <= upper:
                        unique = False
                        break
                if unique:
                    found = chosen
                    break
        return found

    _negation_free = NegationFreeExpression()
    _lyra2apron = Lyra2APRON()
