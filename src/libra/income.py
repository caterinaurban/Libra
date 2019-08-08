
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

# tests/income/income-1-6-82.1-0.04.py

# # 14.166666666666691 (2.0833333333333344% biased) 11.30702018737793s 11.506721019744873s 22.927498817443848s
BiasAnalysis('income.txt', difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# # 36.04166666666692 () 10.283854007720947s
# BiasAnalysis('income.txt', difference=0.5, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 63.958333333333734 () 7.62021017074585s
# BiasAnalysis('income.txt', difference=0.5, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# # 19.16666666666673 (4.166666666666669% biased) 21.442615032196045s 15.540114879608154s 37.09426498413086s
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# # 46.875000000000306 () 17.402333974838257s
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 62.70833333333361 (23.750000000000085% biased) 10.348506689071655s 484.38126492500305s 494.90869998931885s (~8min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# # 19.16666666666673 (4.166666666666669% biased) 25.11437702178955s 15.761247158050537s 40.98417901992798s
# BiasAnalysis('income.txt', symbolic2=True, difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# # 46.875000000000306 () 24.8491849899292s
# BiasAnalysis('income.txt', symbolic2=True, difference=0.5, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 62.70833333333361 (23.750000000000085% biased) 13.530396938323975s 587.1695568561554s 600.8682231903076s (~10min)
# BiasAnalysis('income.txt', symbolic2=True, difference=0.5, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# # 48.51562500000273 (11.22395833333343% biased) 62.11487102508545s 199.22669315338135s 262.3733539581299s (~4.5min)
# BiasAnalysis('income.txt', difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")    # reference
# # 67.2135416666699 () 44.253633975982666s
# BiasAnalysis('income.txt', difference=0.25, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 80.20833333333562 () 23.447524070739746s
# BiasAnalysis('income.txt', difference=0.25, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# # 52.86458333333588 (13.385416666666792% biased) 109.24523210525513s 222.28100609779358s 332.62294483184814s (~5.5min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# # 74.79166666666974 () 69.78282976150513s
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 82.08333333333492 (34.08854166666704% biased) 28.307310104370117s 955.6036176681519s 984.5736050605774s (~16.5min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# # 52.86458333333588 (13.385416666666792% biased) 120.68958783149719s 225.06509590148926s 346.7741189002991s (~5.5min)
# BiasAnalysis('income.txt', symbolic2=True, difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# # 74.79166666666974 () 88.22659111022949s
# BiasAnalysis('income.txt', symbolic2=True, difference=0.25, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# # 82.08333333333492 (34.08854166666704% biased) 37.627761125564575s 1007.6681549549103s 1045.9103450775146s (~17.5min)
# BiasAnalysis('income.txt', symbolic2=True, difference=0.25, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 66.29231770835105 (15.20182291666713% biased) 296.57992720603943s 868.3405368328094s 1170.2300601005554s (~19.5min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 74.9414062500113%
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 83.82161458333792%
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 69.77539062501576%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 82.73111979167409%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 88.01106770833694% () 136.78432989120483s
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 69.77539062501576%
# BiasAnalysis('income.txt', symbolic2=True, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 82.73111979167409%
# BiasAnalysis('income.txt', symbolic2=True, difference=0.125, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 88.01106770833593%
# BiasAnalysis('income.txt', symbolic2=True, difference=0.125, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# ex: 71.14095052088793%
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# ex: 76.9938151041907%
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=4).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic2=True, difference=0.0625, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic2=True, difference=0.0625, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic2=True, difference=0.0625, widening=4).main("tests/income/income-1-6-82.1-0.04.py")


# tests/income/income-1-6-82.0-0.00.py

# BiasAnalysis('income.txt', difference=0.25, widening=3).main("tests/income/income-1-6-82.0-0.00.py")
