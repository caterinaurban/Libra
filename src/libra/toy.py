
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

BiasAnalysis('toy.txt', symbolic1=True, difference=0.25, widening=2).main("tests/toy.py")
