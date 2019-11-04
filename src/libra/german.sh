#!/usr/bin/env bash
#################
# experiment #4 #
#################

#======================#
# assume (x05 <= 0.04) #
#======================#

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias1LtE.py | tee german-no-bias1-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias1LtE.py | tee german-0.20-bias1-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias2LtE.py | tee german-no-bias2-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias2LtE.py | tee german-0.20-bias2-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias3LtE.py | tee german-no-bias3-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias3LtE.py | tee german-0.20-bias3-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias10LtE.py | tee german-no-bias10-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias10LtE.py | tee german-0.20-bias10-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias5LtE.py | tee german-no-bias5-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias5LtE.py | tee german-0.20-bias5-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias6LtE.py | tee german-no-bias6-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias6LtE.py | tee german-0.20-bias6-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias7LtE.py | tee german-no-bias7-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias7LtE.py | tee german-0.20-bias7-nosym-0-10LtE.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias8LtE.py | tee german-no-bias8-nosym-0-10LtE.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias8LtE.py | tee german-0.20-bias8-nosym-0-10LtE.log

#=====================#
# assume (x05 > 0.04) #
#=====================#

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias1Gt.py | tee german-no-bias1-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias1Gt.py | tee german-0.20-bias1-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias2Gt.py | tee german-no-bias2-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias2Gt.py | tee german-0.20-bias2-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias3Gt.py | tee german-no-bias3-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias3Gt.py | tee german-0.20-bias3-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias10Gt.py | tee german-no-bias10-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias10Gt.py | tee german-0.20-bias10-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias5Gt.py | tee german-no-bias5-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias5Gt.py | tee german-0.20-bias5-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias6Gt.py | tee german-no-bias6-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias6Gt.py | tee german-0.20-bias6-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias7Gt.py | tee german-no-bias7-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias7Gt.py | tee german-0.20-bias7-nosym-0-10Gt.log

timeout 46800 python3 germanX.py True False 0 10 tests/german/small-no-bias8Gt.py | tee german-no-bias8-nosym-0-10Gt.log
timeout 46800 python3 germanX.py True False 0 10 tests/german/small-0.20-bias8Gt.py | tee german-0.20-bias8-nosym-0-10Gt.log
