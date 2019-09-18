
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

# # 1.7708333333333373 (0.2430555555555556% biased) 98.02823400497437s 45.615397691726685s 143.82035493850708s
# BiasAnalysis('census.txt', difference=0.5, widening=2).main("tests/census/small-no-bias.py")
# # 23.159722222222847% () 132.45482230186462s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.5, widening=4).main("tests/census/small-no-bias.py")
# # 66.84027777777906% () 74.67842602729797s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.5, widening=8).main("tests/census/small-no-bias.py")
# # 72.63888888889083% () 62.07407307624817s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.5, widening=9).main("tests/census/small-no-bias.py")
# # 79.54861111111343% () 49.562731981277466s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.5, widening=10).main("tests/census/small-no-bias.py")
# # 93.50694444444622% () 32.58939599990845s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.5, widening=12).main("tests/census/small-no-bias.py")
# # 73.28993055556022% () 301.13461804389954s
# BiasAnalysis('census.txt', symbolic1=True, difference=0.25, widening=8).main("tests/census/small-no-bias.py")

# # 14.965277777777997% () 785.0173950195312s
# BiasAnalysis('census.txt', symbolic2=True, difference=0.5, widening=8).main("tests/census/medium-no-bias.py")
# # 32.09201388889137% ()
# BiasAnalysis('census.txt', symbolic2=True, difference=0.25, widening=10).main("tests/census/medium-no-bias.py")

