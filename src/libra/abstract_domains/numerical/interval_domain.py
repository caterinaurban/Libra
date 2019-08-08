"""
Interval Abstract Domain
========================

Non-relational abstract domain to be used for **numerical analysis**.
The set of possible numerical values of a program variable in a program state
is represented as an interval.

:Authors: Caterina Urban
"""
from typing import Set

from apronpy.manager import PyManager
from apronpy.box import PyBox

from libra.abstract_domains.numerical.apron_domain import APRONState
from libra.abstract_domains.state import State
from libra.core.expressions import VariableIdentifier


class BoxState(APRONState):
    """Interval analysis state based on APRON. An element of the interval abstract domain.

    .. document private methods
    .. automethod:: BoxState._assign
    .. automethod:: BoxState._assume
    .. automethod:: BoxState._output
    .. automethod:: BoxState._substitute

    """

    def __init__(self, manager: PyManager, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(manager, variables, PyBox, precursory=precursory)
