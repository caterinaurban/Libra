
import faulthandler
faulthandler.enable()
from libra.engine.functional_analysis import FunctionalAnalysis

# 100.0 (73.44797685362308% biased) 0.8057699203491211s 1.758193016052246s 2.665310859680176s
FunctionalAnalysis('playground.txt', symbolic2=True, difference=0.015625, widening=4, analysis=True).main("tests/example.py")
