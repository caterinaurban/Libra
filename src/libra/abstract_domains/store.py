"""
Store
=====

Lifting of a lattice to a set of program variables.

:Authors: Caterina Urban
"""

from typing import Dict, Any, Type, Set

from libra.abstract_domains.lattice import Lattice, EnvironmentMixin
from libra.core.expressions import VariableIdentifier
from libra.core.utils import copy_docstring


class Store(EnvironmentMixin):
    """Mutable element of a store ``Var -> L``,
    lifting a lattice ``L`` to a set of program variables ``Var``.

    .. warning::
        Lattice operations modify the current store.

    .. document private methods
    .. automethod:: Store._less_equal
    .. automethod:: Store._meet
    .. automethod:: Store._join
    """

    def __init__(self, variables: Set[VariableIdentifier],
                 lattice: Type[Lattice], arguments: Dict[str, Any] = None):
        """Create a mapping Var -> L from each variable in Var to the corresponding element in L.

        :param variables: set of program variables
        :param lattice: lattice type
        :param arguments: arguments of the lattice
        """
        super().__init__()
        self._variables = variables
        self._lattice = lattice
        self._arguments = dict() if arguments is None else arguments
        try:
            self._store = {v: self._lattice(**self._arguments) for v in variables}
        except KeyError as key:
            error = f"Missing lattice for variable type {repr(key.args[0])}!"
            raise ValueError(error)

    @property
    def variables(self):
        """Variables of the current store."""
        return self._variables

    @property
    def lattice(self):
        """Current lattice type."""
        return self._lattice

    @property
    def arguments(self):
        """Current arguments of the lattices."""
        return self._arguments

    @property
    def store(self):
        """Current mapping from variables to their corresponding lattice element."""
        return self._store

    def __repr__(self):
        items = sorted(self.store.items(), key=lambda x: x[0].name)
        return ", ".join("{} -> {}".format(variable, value) for variable, value in items)

    @copy_docstring(Lattice.bottom)
    def bottom(self) -> 'Store':
        for var in self.store:
            self.store[var].bottom()
        return self

    @copy_docstring(Lattice.top)
    def top(self) -> 'Store':
        for var in self.store:
            self.store[var].top()
        return self

    @copy_docstring(Lattice.is_bottom)
    def is_bottom(self) -> bool:
        """The current store is bottom if `any` of its variables map to a bottom element."""
        return any(element.is_bottom() for element in self.store.values())

    @copy_docstring(Lattice.is_top)
    def is_top(self) -> bool:
        """The current store is top if `all` of its variables map to a top element."""
        return all(element.is_top() for element in self.store.values())

    @copy_docstring(EnvironmentMixin.unify)
    def unify(self, other: 'Store'):
        for variable in other.variables:
            if variable not in self.variables:
                self.add_variable(variable)
        return self

    @copy_docstring(Lattice._less_equal)
    def _less_equal(self, other: 'Store') -> bool:
        """The comparison is performed point-wise for each variable."""
        return all(self.store[var].less_equal(other.store[var]) for var in self.store)

    @copy_docstring(Lattice._meet)
    def _meet(self, other: 'Store'):
        """The meet is performed point-wise for each variable."""
        for var in self.store:
            self.store[var].meet(other.store[var])
        return self

    @copy_docstring(Lattice._join)
    def _join(self, other: 'Store') -> 'Store':
        """The join is performed point-wise for each variable."""
        for var in self.store:
            self.store[var].join(other.store[var])
        return self

    @copy_docstring(Lattice._widening)
    def _widening(self, other: 'Store'):
        """The widening is performed point-wise for each variable."""
        for var in self.store:
            self.store[var].widening(other.store[var])
        return self

    @copy_docstring(EnvironmentMixin.add_variable)
    def add_variable(self, variable: VariableIdentifier):
        self.variables.add(variable)
        self.store[variable] = self.lattice(**self.arguments).bottom()
        return self

    @copy_docstring(EnvironmentMixin.remove_variable)
    def remove_variable(self, variable: VariableIdentifier):
        self.variables.remove(variable)
        del self.store[variable]
        return self
