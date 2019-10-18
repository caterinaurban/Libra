
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

BiasAnalysis('japanese.txt', symbolic2=True, difference=0.5, widening=4).main("tests/japanese/small-no-bias.py")
