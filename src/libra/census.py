
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

BiasAnalysis('census.txt', symbolic2=True, difference=0.5, widening=4).main("tests/census/small-no-bias.py")
