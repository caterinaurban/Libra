"""
Neurify test

forward runner instantiated to Neurify example
"""
from libra.engine.forward_runner import ForwardRunner
from libra.engine.bias_analysis import AbstractDomain

spec = 'tests/toy.txt'
nn = 'tests/toy.py'
domain = AbstractDomain.PRODUCT_DEEPPOLY_NEURIFY
b = ForwardRunner(spec, domain=domain)
b.main(nn)
