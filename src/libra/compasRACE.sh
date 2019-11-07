#!/usr/bin/env bash

###########
# experiment 3: queries
###########

#---------#
# RACE
#---------#

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias1.py | tee compas-Lt25small-no-bias1-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias1.py | tee compas-Lt25small-0.20-bias1-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races1.py | tee compas-Lt25small-0.20-bias-2races1-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias2.py | tee compas-Lt25small-no-bias2-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias2.py | tee compas-Lt25small-0.20-bias2-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races2.py | tee compas-Lt25small-0.20-bias-2races2-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias3.py | tee compas-Lt25small-no-bias3-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias3.py | tee compas-Lt25small-0.20-bias3-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races3.py | tee compas-Lt25small-0.20-bias-2races3-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias4.py | tee compas-Lt25small-no-bias4-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias4.py | tee compas-Lt25small-0.20-bias4-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races4.py | tee compas-Lt25small-0.20-bias-2races4-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias5.py | tee compas-Lt25small-no-bias5-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias5.py | tee compas-Lt25small-0.20-bias5-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races5.py | tee compas-Lt25small-0.20-bias-2races5-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias6.py | tee compas-Lt25small-no-bias6-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias6.py | tee compas-Lt25small-0.20-bias6-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races6.py | tee compas-Lt25small-0.20-bias-2races6-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias7.py | tee compas-Lt25small-no-bias7-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias7.py | tee compas-Lt25small-0.20-bias7-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races7.py | tee compas-Lt25small-0.20-bias-2races7-sym-0-10.log

timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-no-bias8.py | tee compas-Lt25small-no-bias8-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias8.py | tee compas-Lt25small-0.20-bias8-sym-0-10.log
timeout 46800 python3 compasRACE.py True False 0 10 tests/compas/Lt25small-0.20-bias-2races8.py | tee compas-Lt25small-0.20-bias-2races8-sym-0-10.log

#---------#
# GENDER
#---------#

# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias1.py | tee compas-2545small-no-bias1-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias1.py | tee compas-2545small-0.20-bias1-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races1.py | tee compas-2545small-0.20-bias-2races1-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias2.py | tee compas-2545small-no-bias2-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias2.py | tee compas-2545small-0.20-bias2-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races2.py | tee compas-2545small-0.20-bias-2races2-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias3.py | tee compas-2545small-no-bias3-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias3.py | tee compas-2545small-0.20-bias3-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races3.py | tee compas-2545small-0.20-bias-2races3-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias4.py | tee compas-2545small-no-bias4-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias4.py | tee compas-2545small-0.20-bias4-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races4.py | tee compas-2545small-0.20-bias-2races4-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias5.py | tee compas-2545small-no-bias5-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias5.py | tee compas-2545small-0.20-bias5-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races5.py | tee compas-2545small-0.20-bias-2races5-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias6.py | tee compas-2545small-no-bias6-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias6.py | tee compas-2545small-0.20-bias6-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races6.py | tee compas-2545small-0.20-bias-2races6-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias7.py | tee compas-2545small-no-bias7-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias7.py | tee compas-2545small-0.20-bias7-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races7.py | tee compas-2545small-0.20-bias-2races7-sym-0-10.log
#
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-no-bias8.py | tee compas-2545small-no-bias8-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias8.py | tee compas-2545small-0.20-bias8-sym-0-10.log
# timeout 46800 python3 compasGENDER.py True False 0 10 tests/compas/2545small-0.20-bias-2races8.py | tee compas-2545small-0.20-bias-2races8-sym-0-10.log

#---------#
# PRIORS
#---------#

# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias1.py | tee compas-Asmall-no-bias1-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias1.py | tee compas-Asmall-0.20-bias1-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races1.py | tee compas-Asmall-0.20-bias-2races1-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias2.py | tee compas-Asmall-no-bias2-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias2.py | tee compas-Asmall-0.20-bias2-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races2.py | tee compas-Asmall-0.20-bias-2races2-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias3.py | tee compas-Asmall-no-bias3-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias3.py | tee compas-Asmall-0.20-bias3-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races3.py | tee compas-Asmall-0.20-bias-2races3-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias4.py | tee compas-Asmall-no-bias4-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias4.py | tee compas-Asmall-0.20-bias4-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races4.py | tee compas-Asmall-0.20-bias-2races4-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias5.py | tee compas-Asmall-no-bias5-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias5.py | tee compas-Asmall-0.20-bias5-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races5.py | tee compas-Asmall-0.20-bias-2races5-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias6.py | tee compas-Asmall-no-bias6-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias6.py | tee compas-Asmall-0.20-bias6-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races6.py | tee compas-Asmall-0.20-bias-2races6-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias7.py | tee compas-Asmall-no-bias7-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias7.py | tee compas-Asmall-0.20-bias7-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races7.py | tee compas-Asmall-0.20-bias-2races7-sym-0-10.log
#
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-no-bias8.py | tee compas-Asmall-no-bias8-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias8.py | tee compas-Asmall-0.20-bias8-sym-0-10.log
# timeout 46800 python3 compasPRIORS.py True False 0 10 tests/compas/Asmall-0.20-bias-2races8.py | tee compas-Asmall-0.20-bias-2races8-sym-0-10.log
