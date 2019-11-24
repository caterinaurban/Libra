
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

# 100.0 (73.44797685362308% biased) 0.8057699203491211s 1.758193016052246s 2.665310859680176s
BiasAnalysis('playground.txt', symbolic2=True, difference=0, widening=2).main("tests/example.py")
