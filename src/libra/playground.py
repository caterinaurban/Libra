
import faulthandler
faulthandler.enable()

######################
# Numerical Analyses #
######################

# from libra.engine.numerical.interval_analysis import ForwardIntervalAnalysis
# ForwardIntervalAnalysis().main("tests/example.py")

# from libra.engine.numerical.interval_analysis import ForwardBoxAnalysis
# ForwardBoxAnalysis().main("tests/example.py")

# from libra.engine.numerical.interval_analysis import BackwardIntervalAnalysis
# BackwardIntervalAnalysis().main("tests/example.py")

# from libra.engine.numerical.polyhedra_analysis import ForwardPolyhedraAnalysis
# ForwardPolyhedraAnalysis().main("tests/example.py")

# from libra.engine.numerical.polyhedra_analysis import BackwardPolyhedraAnalysis
# BackwardPolyhedraAnalysis().main("tests/example.py")

#################
# Bias Analyses #
#################

from libra.engine.bias.bias_analysis import BiasAnalysis

# BiasAnalysis().main("tests/example.py")
# BiasAnalysis().main("tests/example0.py")
# BiasAnalysis().main("tests/example2.py")
# BiasAnalysis().main("tests/example3.py")

# # 25.0% (25.0% biased) 0.17382192611694336s 3.322619915008545s 3.528939723968506s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0.25, widening=4).main("tests/model-10-5-0.97.py")
# # 25.0% (25.0% biased) 0.6399009227752686s 0.30579304695129395s 0.9775271415710449s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=2).main("tests/model-10-5-0.97.py")
# # 25.0% (25.0% biased) 0.6397461891174316s 0.31095409393310547s 0.9934120178222656s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=3).main("tests/model-10-5-0.97.py")
# # 25.0% (25.0% biased) 0.6328930854797363s 0.31067585945129395s 0.9749112129211426s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.25, widening=4).main("tests/model-10-5-0.97.py")

# # 25.0% (25.0% biased) 0.2308197021484375s 0.7276649475097656s 0.992746114730835s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0.125, widening=2).main("tests/model-10-5-0.97.py")
# # 37.5% (37.5% biased) 0.22934508323669434s 1.027214765548706s 1.2892968654632568s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0.125, widening=3).main("tests/model-10-5-0.97.py")
# # 37.5% (37.5% biased) 0.2405529022216797s 3.3661580085754395s 3.637967824935913s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0.125, widening=4).main("tests/model-10-5-0.97.py")
# # 50.0% (50.0% biased) 0.8401069641113281s 0.4834442138671875s 1.3561789989471436s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=2).main("tests/model-10-5-0.97.py")
# # 50.0% (50.0% biased) 0.8726568222045898s 0.48987889289855957s 1.3988838195800781s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=3).main("tests/model-10-5-0.97.py")
# # 50.0% (50.0% biased) 0.8680739402770996s 0.4996151924133301s 1.401702880859375s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0.125, widening=4).main("tests/model-10-5-0.97.py")

# 100.0% (73.6328125% biased) 1.4397509098052979s 6.321099042892456s 7.872607946395874s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0, widening=2).main("tests/model-10-5-0.97.py")     # 7.834737300872803s
# 100.0% (74.21875% biased) 1.0723309516906738s 7.6071250438690186s 8.770008087158203s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0, widening=3).main("tests/model-10-5-0.97.py")     # 9.138473987579346s
# 100.0% (74.21875% biased) 0.8227808475494385s 9.023157119750977s 9.921536922454834s
# BiasAnalysis('playground.txt', symbolic1=False, difference=0, widening=4).main("tests/model-10-5-0.97.py")     # 10.073421716690063s
# 100.0% (75.0% biased) 2.3313472270965576s 3.279317855834961s 5.673985958099365s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=2).main("tests/model-10-5-0.97.py")     # 13.498871088027954s
BiasAnalysis('playground.txt', symbolic2=True, difference=0, widening=2).main("tests/model-10-5-0.97.py")     # 13.498871088027954s
# 100.0% (75.0% biased) 1.8078088760375977s 3.4563162326812744s 5.3152501583099365s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=3).main("tests/model-10-5-0.97.py")     # 10.897016763687134s
# 100.0% (75.0% biased) 1.3733391761779785s 3.664357900619507s 5.084070920944214s
# BiasAnalysis('playground.txt', symbolic1=True, difference=0, widening=4).main("tests/model-10-5-0.97.py")     # 9.397150993347168s

# BiasAnalysis().main("tests/model-10-6-1.00.py")
# BiasAnalysis().main("tests/model-20-6-1.00.py")
