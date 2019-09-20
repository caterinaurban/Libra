
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

# print("tests/japanese/small-no-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=2).main("tests/japanese/small-no-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=4).main("tests/japanese/small-no-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=6).main("tests/japanese/small-no-bias.py")
# # 50%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=8).main("tests/japanese/small-no-bias.py")
# # >88%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.25, widening=8).main("tests/japanese/small-no-bias.py")
#
BiasAnalysis('japanese.txt', symbolic1=True, difference=0.125, widening=4).main("tests/japanese/small-no-bias.py")

# print("tests/japanese/small-0.05-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=2).main("tests/japanese/small-0.05-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=4).main("tests/japanese/small-0.05-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=6).main("tests/japanese/small-0.05-bias.py")
# # ~46%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=8).main("tests/japanese/small-0.05-bias.py")
# # >88%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.25, widening=8).main("tests/japanese/small-0.05-bias.py")

# print("tests/japanese/small-0.20-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=2).main("tests/japanese/small-0.20-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=4).main("tests/japanese/small-0.20-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=6).main("tests/japanese/small-0.20-bias.py")
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=8).main("tests/japanese/small-0.20-bias.py")
# # ~44%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.5, widening=10).main("tests/japanese/small-0.20-bias.py")
# # >88%
# BiasAnalysis('japanese.txt', symbolic1=True, difference=0.25, widening=10).main("tests/japanese/small-0.20-bias.py")
