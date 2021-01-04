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
minL = 0.015625
maxU = 4
BiasAnalysis(spec, domain=domain, minL=minL, startL=1, startU=0, maxU=maxU).main(nn)
