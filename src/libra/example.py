"""
Small Example
=============

:Author: Caterina Urban
"""
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis, AbstractDomain

spec = 'tests/example.txt'
nn = 'tests/example.py'
domain = AbstractDomain.BOXES
lower = 0.015625
upper = 4
BiasAnalysis(spec, domain=domain, difference=lower, widening=upper).main(nn)
