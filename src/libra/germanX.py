
from sys import argv
from libra.engine.functional_analysis import FunctionalAnalysis
import faulthandler
faulthandler.enable()


s1 = argv[1] == "True"
s2 = argv[2] == "True"
d = float(argv[3])
w = int(argv[4])
p = argv[5]
FunctionalAnalysis('german.txt', symbolic1=s1, symbolic2=s2, difference=d, widening=w).main(p)
