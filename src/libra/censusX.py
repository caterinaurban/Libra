
from sys import argv
from libra.engine.functional_analysis import FunctionalAnalysis
import faulthandler
faulthandler.enable()

import sys
sys.setrecursionlimit(10000)


s1 = argv[1] == "True"
s2 = argv[2] == "True"
d = float(argv[3])
w = int(argv[4])
a = argv[5] == "True"
p = argv[6]
FunctionalAnalysis('census.txt', symbolic1=s1, symbolic2=s2, difference=d, widening=w, analysis=a).main(p)
