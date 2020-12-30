from libra.abstract_domains.deeppoly_domain import DeepPolyState
from libra.abstract_domains.neurify_domain import NeurifyState
from libra.abstract_domains.symbolic3_domain import Symbolic3State
from libra.abstract_domains.product_domain import ProductState

NON_APRON_DOMAINS = (
    DeepPolyState,
    NeurifyState,
    Symbolic3State,
    ProductState)
