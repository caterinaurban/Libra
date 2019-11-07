
from sys import argv
from libra.engine.bias_analysis import BiasAnalysis
import faulthandler
faulthandler.enable()


s1 = argv[1] == "True"
s2 = argv[2] == "True"
d = float(argv[3])
w = int(argv[4])
p = argv[5]
BiasAnalysis('compasPRIORS.txt', symbolic1=s1, symbolic2=s2, difference=d, widening=w).main(p)
