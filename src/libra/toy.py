"""
Toy Example
===========

:Author: Caterina Urban
"""
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis, AbstractDomain

spec = 'tests/toy.txt'
nn = 'tests/toy.py'
domain = AbstractDomain.BOXES1
lower = 0.25
upper = 2
BiasAnalysis(spec, domain=domain, difference=lower, widening=upper).main(nn)
