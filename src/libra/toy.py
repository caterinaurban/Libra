
import faulthandler
faulthandler.enable()
from libra.engine.functional_analysis import FunctionalAnalysis

FunctionalAnalysis('toy.txt', symbolic1=True, difference=0.25, widening=2).main("tests/toy.py")
