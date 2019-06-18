"""
Octagon Abstract Domain
=======================

Relational abstract domain to be used for **numerical analysis**.
The set of possible numerical values of a program variable in a program state
is represented by a conjunction of linear constraints.

:Authors: Caterina Urban
"""
from typing import Set

from apronpy.oct import PyOctD, PyOctMPQ

from libra.abstract_domains.numerical.apron_domain import APRONState
from libra.abstract_domains.state import State
from libra.core.expressions import VariableIdentifier


class OctagonDState(APRONState):
    """Octagon analysis state based on APRON. An element of the octagon abstract domain.

    .. document private methods
    .. automethod:: OctagonDState._assign
    .. automethod:: OctagonDState._assume
    .. automethod:: OctagonDState._output
    .. automethod:: OctagonDState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyOctD, precursory=precursory)


class OctagonMPQState(APRONState):
    """Octagon analysis state based on APRON. An element of the octagon abstract domain.

    .. document private methods
    .. automethod:: OctagonMPQState._assign
    .. automethod:: OctagonMPQState._assume
    .. automethod:: OctagonMPQState._output
    .. automethod:: OctagonMPQState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyOctMPQ, precursory=precursory)


OctagonState = OctagonMPQState
