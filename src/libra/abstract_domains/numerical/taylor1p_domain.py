"""
Taylor1+ Abstract Domain
========================

:Authors: Caterina Urban
"""
from typing import Set
from apronpy.t1p import PyT1pD, PyT1pMPQ, PyT1pMPFR

from libra.abstract_domains.numerical.apron_domain import APRONState
from libra.abstract_domains.state import State
from libra.core.expressions import VariableIdentifier


class Taylor1pDState(APRONState):
    """Taylor1+ analysis state based on APRON. An element of the taylor1+ abstract domain.

    .. document private methods
    .. automethod:: T1pDState._assign
    .. automethod:: T1pDState._assume
    .. automethod:: T1pDState._output
    .. automethod:: T1pDState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyT1pD, precursory=precursory)


class Taylor1pMPQState(APRONState):
    """Interval analysis state based on APRON. An element of the interval abstract domain.

    .. document private methods
    .. automethod:: T1pMPQState._assign
    .. automethod:: T1pMPQState._assume
    .. automethod:: T1pMPQState._output
    .. automethod:: T1pMPQState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyT1pMPQ, precursory=precursory)


Taylor1pState = Taylor1pMPQState


class Taylor1pMPFRState(APRONState):
    """Interval analysis state based on APRON. An element of the interval abstract domain.

    .. document private methods
    .. automethod:: T1pMPFRState._assign
    .. automethod:: T1pMPFRState._assume
    .. automethod:: T1pMPFRState._output
    .. automethod:: T1pMPFRState._substitute

    """

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        super().__init__(variables, PyT1pMPFR, precursory=precursory)
