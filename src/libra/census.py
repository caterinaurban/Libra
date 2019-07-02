
import faulthandler
faulthandler.enable()

from libra.engine.bias.bias_analysis import BiasAnalysis

# BiasAnalysis().main("tests/census/model-5-3-acc79.1-bias20-small.py")
BiasAnalysis().main("tests/census/model-5-3-acc79.9-bias20.py")
