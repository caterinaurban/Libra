
import faulthandler
faulthandler.enable()

from libra.engine.bias.bias_analysis import BiasAnalysis

BiasAnalysis().main("tests/income/income-1-6-82.1-0.04.py")
# BiasAnalysis().main("tests/income/income-1-6-77.3-0.20.py")
# BiasAnalysis().main("tests/income/income-1-6-82.0-0.00.py")