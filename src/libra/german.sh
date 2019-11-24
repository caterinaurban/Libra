#!/usr/bin/env bash
#################
# experiment #1: detecting bias
#################

#======================#
# assume (x05 <= 0.04) #
#======================#

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias1.py | tee german-LtEno-bias1-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias1.py | tee german-LtE0.20-bias1-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias2.py | tee german-LtEno-bias2-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias2.py | tee german-LtE0.20-bias2-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias3.py | tee german-LtEno-bias3-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias3.py | tee german-LtE0.20-bias3-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias10.py | tee german-LtEno-bias10-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias10.py | tee german-LtE0.20-bias10-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias5.py | tee german-LtEno-bias5-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias5.py | tee german-LtE0.20-bias5-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias6.py | tee german-LtEno-bias6-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias6.py | tee german-LtE0.20-bias6-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias7.py | tee german-LtEno-bias7-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias7.py | tee german-LtE0.20-bias7-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/LtEno-bias8.py | tee german-LtEno-bias8-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/LtE0.20-bias8.py | tee german-LtE0.20-bias8-nosym-0-12.log

#=====================#
# assume (x05 > 0.04) #
#=====================#

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias1.py | tee german-Gtno-bias1-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 15 tests/german/Gt0.20-bias1.py | tee german-Gt0.20-bias1-nosym-0-15.log

timeout 46800 python3 germanX.py True False 0 15 tests/german/Gtno-bias2.py | tee german-Gtno-bias2-nosym-0-15.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/Gt0.20-bias2.py | tee german-Gt0.20-bias2-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias3.py | tee german-Gtno-bias3-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 15 tests/german/Gt0.20-bias3.py | tee german-Gt0.20-bias3-nosym-0-15.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias10.py | tee german-Gtno-bias10-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/Gt0.20-bias10.py | tee german-Gt0.20-bias10-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias5.py | tee german-Gtno-bias5-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/Gt0.20-bias5.py | tee german-Gt0.20-bias5-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 16 tests/german/Gtno-bias6.py | tee german-Gtno-bias6-nosym-0-16.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/Gt0.20-bias6.py | tee german-Gt0.20-bias6-nosym-0-12.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias7.py | tee german-Gtno-bias7-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 16 tests/german/Gt0.20-bias7.py | tee german-Gt0.20-bias7-nosym-0-16.log

timeout 46800 python3 germanX.py True False 0 12 tests/german/Gtno-bias8.py | tee german-Gtno-bias8-nosym-0-12.log
timeout 46800 python3 germanX.py True False 0 12 tests/german/Gt0.20-bias8.py | tee german-Gt0.20-bias8-nosym-0-12.log
