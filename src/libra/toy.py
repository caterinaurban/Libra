
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

BiasAnalysis('toy.txt', symbolic1=False, difference=0.125, widening=3).main("tests/toy.py")
