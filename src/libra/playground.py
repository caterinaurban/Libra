
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

from libra.engine.bias.bias_analysis import BiasAnalysis, JoinHeuristics

# BiasAnalysis().main("tests/example.py")

# BiasAnalysis().main("tests/example0.py")  # no joins
# BiasAnalysis().main("tests/example0.py", heuristic=JoinHeuristics.NotTop)

# BiasAnalysis().main("tests/example3.py")  # no joins
# BiasAnalysis().main("tests/example3.py", heuristic=JoinHeuristics.NotTop)

# BiasAnalysis().main("tests/model-10-5-0.97.py")  # no joins
# BiasAnalysis().main("tests/model-10-5-0.97.py", heuristic=JoinHeuristics.NotTop)

# BiasAnalysis().main("tests/model-10-6-1.00.py")  # no joins
# BiasAnalysis().main("tests/model-10-6-1.00.py", heuristic=JoinHeuristics.NotTop)

BiasAnalysis().main("tests/model-20-6-1.00.py")  # no joins
# BiasAnalysis().main("tests/model-20-6-1.00.py", heuristic=JoinHeuristics.NotTop)
