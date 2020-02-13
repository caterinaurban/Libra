#!/usr/bin/env bash
###########
# experiment 2: bias queries
###########

#---------#
# RACE
#---------#

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias1.py | tee compas-Lt25no-bias1-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias1.py | tee compas-Lt250.20-bias1-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias2.py | tee compas-Lt25no-bias2-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias2.py | tee compas-Lt250.20-bias2-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias3.py | tee compas-Lt25no-bias3-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias3.py | tee compas-Lt250.20-bias3-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias4.py | tee compas-Lt25no-bias4-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias4.py | tee compas-Lt250.20-bias4-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias5.py | tee compas-Lt25no-bias5-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias5.py | tee compas-Lt250.20-bias5-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias6.py | tee compas-Lt25no-bias6-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias6.py | tee compas-Lt250.20-bias6-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias7.py | tee compas-Lt25no-bias7-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias7.py | tee compas-Lt250.20-bias7-sym-0-10.log

timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt25no-bias8.py | tee compas-Lt25no-bias8-sym-0-10.log
timeout 46800 python3 compasXrace.py True False 0 10 tests/compas/Lt250.20-bias8.py | tee compas-Lt250.20-bias8-sym-0-10.log

#---------#
# AGE
#---------#

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias1.py | tee compas-Mno-bias1-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias1.py | tee compas-M0.20-bias1-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias2.py | tee compas-Mno-bias2-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias2.py | tee compas-M0.20-bias2-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias3.py | tee compas-Mno-bias3-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias3.py | tee compas-M0.20-bias3-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias4.py | tee compas-Mno-bias4-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias4.py | tee compas-M0.20-bias4-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias5.py | tee compas-Mno-bias5-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias5.py | tee compas-M0.20-bias5-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias6.py | tee compas-Mno-bias6-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias6.py | tee compas-M0.20-bias6-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias7.py | tee compas-Mno-bias7-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias7.py | tee compas-M0.20-bias7-sym-0-10.log

timeout 46800 python3 compasXage.py True False 0 10 tests/compas/Mno-bias8.py | tee compas-Mno-bias8-sym-0-10.log
timeout 46800 python3 compasXage.py True False 0 10 tests/compas/M0.20-bias8.py | tee compas-M0.20-bias8-sym-0-10.log

#---------#
# PRIORS
#---------#

timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/Cno-bias1.py | tee compas-Cno-bias1-sym-0-10.log
timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/C0.20-bias1.py | tee compas-C0.20-bias1-sym-0-10.log    # 15

timeout 46800 python3 compasXpriors.py True False 0 10 tests/compas/Cno-bias2.py | tee compas-Cno-bias2-sym-0-10.log        # 12
timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/C0.20-bias2.py | tee compas-C0.20-bias2-sym-0-10.log    # 15

timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/Cno-bias3.py | tee compas-Cno-bias3-sym-0-10.log        # 15
timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/C0.20-bias3.py | tee compas-C0.20-bias3-sym-0-10.log

timeout 46800 python3 compasXpriors.py True False 0 17 tests/compas/Cno-bias4.py | tee compas-Cno-bias4-sym-0-10.log        # 19
timeout 46800 python3 compasXpriors.py True False 0 10 tests/compas/C0.20-bias4.py | tee compas-C0.20-bias4-sym-0-10.log    # 12

timeout 46800 python3 compasXpriors.py True False 0 19 tests/compas/Cno-bias5.py | tee compas-Cno-bias5-sym-0-10.log
timeout 46800 python3 compasXpriors.py True False 0 15 tests/compas/C0.20-bias5.py | tee compas-C0.20-bias5-sym-0-10.log

timeout 46800 python3 compasXpriors.py True False 0 12 tests/compas/Cno-bias6.py | tee compas-Cno-bias6-sym-0-10.log
timeout 46800 python3 compasXpriors.py True False 0 15 tests/compas/C0.20-bias6.py | tee compas-C0.20-bias6-sym-0-10.log

timeout 46800 python3 compasXpriors.py True False 0 15 tests/compas/Cno-bias7.py | tee compas-Cno-bias7-sym-0-10.log
timeout 46800 python3 compasXpriors.py True False 0 17 tests/compas/C0.20-bias7.py | tee compas-C0.20-bias7-sym-0-10.log    # 19

timeout 46800 python3 compasXpriors.py True False 0 15 tests/compas/Cno-bias8.py | tee compas-Cno-bias8-sym-0-10.log
timeout 46800 python3 compasXpriors.py True False 0 17 tests/compas/C0.20-bias8.py | tee compas-C0.20-bias8-sym-0-10.log    # 19
