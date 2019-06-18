"""
Polyhedra Abstract Domain
=========================

Relational abstract domain to be used for **numerical analysis**.
The set of possible numerical values of a program variable in a program state
is represented by a conjunction of linear constraints.

:Authors: Caterina Urban
"""
from copy import deepcopy
from typing import Set

from apronpy.environment import PyEnvironment
from apronpy.polka import PyPolkaMPQstrict, PyPolkaMPQloose, PyPolkaRllloose, PyPolkaRllstrict
from apronpy.tcons1 import PyTcons1Array
from apronpy.var import PyVar

from libra.abstract_domains.numerical.apron_domain import APRONState
from libra.abstract_domains.state import State
from libra.core.expressions import VariableIdentifier, Expression, BinaryBooleanOperation, \
    BinaryComparisonOperation, NegationFreeExpression, Lyra2APRON
from libra.core.utils import copy_docstring


class PolyhedraMPQlooseState(APRONState):
    """Polyhedra analysis state based on APRON. An element of the polyhedra abstract domain.

    .. document private methods
    .. automethod:: PolyhedraMPQlooseState._assign
    .. automethod:: PolyhedraMPQlooseState._assume
    .. automethod:: PolyhedraMPQlooseState._output
    .. automethod:: PolyhedraMPQlooseState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyPolkaMPQloose, precursory=precursory)


class PolyhedraMPQstrictState(APRONState):
    """Polyhedra analysis state based on APRON. An element of the polyhedra abstract domain.

    .. document private methods
    .. automethod:: PolyhedraMPQstrictState._assign
    .. automethod:: PolyhedraMPQstrictState._assume
    .. automethod:: PolyhedraMPQstrictState._output
    .. automethod:: PolyhedraMPQstrictState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyPolkaMPQstrict, precursory=precursory)


PolyhedraState =  PolyhedraMPQstrictState


class PolyhedraRlllooseState(APRONState):
    """Polyhedra analysis state based on APRON. An element of the polyhedra abstract domain.

    .. document private methods
    .. automethod:: PolyhedraRlllooseState._assign
    .. automethod:: PolyhedraRlllooseState._assume
    .. automethod:: PolyhedraRlllooseState._output
    .. automethod:: PolyhedraRlllooseState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyPolkaRllloose, precursory=precursory)


class PolyhedraRllstrictState(APRONState):
    """Polyhedra analysis state based on APRON. An element of the polyhedra abstract domain.

    .. document private methods
    .. automethod:: PolyhedraRllstrictState._assign
    .. automethod:: PolyhedraRllstrictState._assume
    .. automethod:: PolyhedraRllstrictState._output
    .. automethod:: PolyhedraRllstrictState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyPolkaRllstrict, precursory=precursory)
