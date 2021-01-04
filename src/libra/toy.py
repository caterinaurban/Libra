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
domain = AbstractDomain.BOXES
minL = 0.25
maxU = 2
BiasAnalysis(spec, domain=domain, minL=minL, startL=1, startU=0, maxU=maxU).main(nn)
