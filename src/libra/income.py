
import faulthandler
faulthandler.enable()

from libra.engine.bias.bias_analysis import BiasAnalysis

# tests/income/income-1-6-82.1-0.04.py

# 14.166666666666698% (2.0833333333333344% biased), 27.533817768096924s
# BiasAnalysis('income.txt', symbolic1=False, difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 36.04166666666692% (9.166666666666684% biased), 75.87717294692993s (1.2646195491min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.5, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 63.958333333333734% (24.375000000000107% biased), 513.8358287811279s (8.5639304797min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.5, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 19.166666666666735% (4.16666666666667% biased), 49.422054052352905s
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
BiasAnalysis('income.txt', symbolic2=True, difference=0.5, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 46.875000000000306% (12.916666666666691% biased), 363.51512718200684s (6.058585453min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 62.7083333333337% (25.208333333333435% biased), 468.7294659614563s (7.812157766min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.5, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 48.51562500000331% (11.250000000000119% biased), 303.09604692459106s (5.0516007821min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 67.21354166666987% (20.59895833333359% biased), 682.0296800136566s (11.3671613336min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.25, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 80.20833333333563% (32.57812500000032% biased) 1495.0552401542664s (24.9175873359min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.25, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 52.864583333336874% (13.151041666666822% biased), 380.6457459926605s (6.3440957665min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# BiasAnalysis('income.txt', symbolic2=True, difference=0.25, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 74.79166666666971% (23.04687500000029% biased), 679.9877507686615s (11.3331291795min)
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 82.08333333333543% (35.3125000000005% biased), 1210.909075975418s (20.1818179329min) <===
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 66.2923177083505% (15.032552083333833% biased), 1204.3694179058075s (20.0728236318min)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 74.9414062500113% (22.460937500000576% biased), 5785.83523106575s (1.6071764531h)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 83.82161458333792% (33.43750000000041% biased), 7704.459925174713s (2.140127757h)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.125, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 71.14095052088793% (15.552164713542481% biased), 5281.735915184021s (1.4671488653h)
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 76.9938151041907%
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=False, difference=0.0625, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

# 69.77539062501576%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# BiasAnalysis('income.txt', symbolic2=True, difference=0.125, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
# 82.73111979167409%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
# 88.01106770833593%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.125, widening=4).main("tests/income/income-1-6-82.1-0.04.py")

#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=2).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=3).main("tests/income/income-1-6-82.1-0.04.py")
#
# BiasAnalysis('income.txt', symbolic1=True, difference=0.0625, widening=4).main("tests/income/income-1-6-82.1-0.04.py")


# tests/income/income-1-6-77.3-0.20.py

# BiasAnalysis().main("tests/income/income-1-6-77.3-0.20.py")

# tests/income/income-1-6-82.0-0.00.py

# BiasAnalysis().main("tests/income/income-1-6-82.0-0.00.py")

# tests/income/income-1-6-78.2-0.00.py

# 75.67708333333466%
# BiasAnalysis('income.txt', symbolic1=True, difference=0.25, widening=4).main("tests/income/income-1-6-78.2-0.00.py")
