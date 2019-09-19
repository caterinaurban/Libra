
import faulthandler
faulthandler.enable()
from libra.engine.bias_analysis import BiasAnalysis

# BiasAnalysis().main("tests/example.py")
# BiasAnalysis('playground.txt').main("tests/example0.py")
# BiasAnalysis('playground.txt').main("tests/example2.py")
# BiasAnalysis('playground.txt').main("tests/example3.py")

# # 25.0 (25.0% biased) 0.15158510208129883s 3.6247379779815674s 3.8694889545440674s
# BiasAnalysis('playground.txt', difference=0.25, widening=4).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.8611981868743896s 0.3377547264099121s 1.257138967514038s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=2).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.812960147857666s 0.30427026748657227s 1.1739461421966553s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=3).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.829779863357544s 0.3374330997467041s 1.231825828552246s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=4).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.3660581111907959s 0.32540297508239746s 0.7585849761962891s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.25, widening=2).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.3202991485595703s 0.3031191825866699s 0.6830089092254639s <===
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.25, widening=3).main("tests/model-10-5-0.97.py")
# # 25.0 (25.0% biased) 0.3634219169616699s 0.3383219242095947s 0.7663030624389648s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.25, widening=4).main("tests/model-10-5-0.97.py")

# # 25.0 (25.0% biased) 0.24852204322814941s 0.7434532642364502s 1.0528631210327148s
# BiasAnalysis('playground.txt', difference=0.125, widening=2).main("tests/model-10-5-0.97.py")
# # 37.5 (37.5% biased) 0.20398998260498047s 1.0458550453186035s 1.3371529579162598s
# BiasAnalysis('playground.txt', difference=0.125, widening=3).main("tests/model-10-5-0.97.py")
# # 37.5 (37.5% biased) 0.19133996963500977s 3.363255023956299s 3.618574857711792s
# BiasAnalysis('playground.txt', difference=0.125, widening=4).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 1.1622118949890137s 0.491041898727417s 1.7147769927978516s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=2).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 1.149907112121582s 0.48775792121887207s 1.703446865081787s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=3).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 1.1623070240020752s 0.4915308952331543s 1.713324785232544s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=4).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 0.44672584533691406s 0.489605188369751s 0.997532844543457s <===
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.125, widening=2).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 0.4320809841156006s 0.5026333332061768s 0.9987890720367432s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.125, widening=3).main("tests/model-10-5-0.97.py")
# # 50.0 (50.0% biased) 0.443835973739624s 0.5086121559143066s 1.0177128314971924s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.125, widening=4).main("tests/model-10-5-0.97.py")

# # 100.0 (73.6328125% biased) 1.3627080917358398s 5.73189115524292s 7.26416277885437s
BiasAnalysis('playground.txt', difference=0, widening=2).main("tests/model-10-5-0.97.py")
# # 100.0 (74.21875% biased) 1.022963047027588s 7.4370551109313965s 8.591149091720581s
# BiasAnalysis('playground.txt', difference=0, widening=3).main("tests/model-10-5-0.97.py")
# # 100.0 (74.21875% biased) 0.7698900699615479s 8.733776092529297s 9.602909326553345s
# BiasAnalysis('playground.txt', difference=0, widening=4).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 9.67160177230835s 3.0475850105285645s 12.805122137069702s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=2).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 7.141970157623291s 3.414651870727539s 10.635745763778687s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=3).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 5.4372148513793945s 3.6349539756774902s 9.142781019210815s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=4).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 1.504511833190918s 3.1173629760742188s 4.713061094284058s <===
# BiasAnalysis('playground.txt', symbolic2=True, difference=0, widening=2).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 1.173940896987915s 3.3100898265838623s 4.566112995147705s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0, widening=3).main("tests/model-10-5-0.97.py")
# # 100.0 (75.0% biased) 0.8827242851257324s 3.5295209884643555s 4.481604099273682s
# BiasAnalysis('playground.txt', symbolic2=True, difference=0, widening=4).main("tests/model-10-5-0.97.py")

# BiasAnalysis('playground.txt', symbolic2=True, difference=0.25, widening=4).main("tests/model-10-6-1.00.py")
# BiasAnalysis('playground.txt', symbolic2=True, difference=0.0625, widening=4).main("tests/model-20-6-1.00.py")
