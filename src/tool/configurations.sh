#!/usr/bin/env bash
###################################################
# Experiment 2: Precision-vs-Scalability Tradeoff #
###################################################

#=======#
# boxes #
#=======#

tool tests/census/census.txt tests/census/20.py --domain boxes --lower 0.5 --upper 3 | tee tests/census/logs2/census-20-boxes-0.5-3.log
tool tests/census/census.txt tests/census/20.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs2/census-20-boxes-0.5-5.log

tool tests/census/census.txt tests/census/20.py --domain boxes --lower 0.25 --upper 3 | tee tests/census/logs2/census-20-boxes-0.25-3.log
tool tests/census/census.txt tests/census/20.py --domain boxes --lower 0.25 --upper 5 | tee tests/census/logs2/census-20-boxes-0.25-5.log

#==========#
# symbolic #
#==========#

tool tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.5 --upper 3 | tee tests/census/logs2/census-20-symbolic-0.5-3.log
tool tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs2/census-20-symbolic-0.5-5.log

tool tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.25 --upper 3 | tee tests/census/logs2/census-20-symbolic-0.25-3.log
tool tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.25 --upper 5 | tee tests/census/logs2/census-20-symbolic-0.25-5.log

#==========#
# deeppoly #
#==========#

tool tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.5 --upper 3 | tee tests/census/logs2/census-20-deeppoly-0.5-3.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs2/census-20-deeppoly-0.5-5.log

tool tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.25 --upper 3 | tee tests/census/logs2/census-20-deeppoly-0.25-3.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.25 --upper 5 | tee tests/census/logs2/census-20-deeppoly-0.25-5.log

#==========#
# neurify #
#==========#

tool tests/census/census.txt tests/census/20.py --domain neurify --lower 0.5 --upper 3 | tee tests/census/logs2/census-20-neurify-0.5-3.log
tool tests/census/census.txt tests/census/20.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs2/census-20-neurify-0.5-5.log

tool tests/census/census.txt tests/census/20.py --domain neurify --lower 0.25 --upper 3 | tee tests/census/logs2/census-20-neurify-0.25-3.log
tool tests/census/census.txt tests/census/20.py --domain neurify --lower 0.25 --upper 5 | tee tests/census/logs2/census-20-neurify-0.25-5.log

#===========================#
# deeppoly+neurify+symbolic #
#===========================#

tool tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 3 | tee tests/census/logs2/census-20-deeppoly_neurify_symbolic-0.5-3.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs2/census-20-deeppoly_neurify_symbolic-0.5-5.log

tool tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 3 | tee tests/census/logs2/census-20-deeppoly_neurify_symbolic-0.25-3.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 5 | tee tests/census/logs2/census-20-deeppoly_neurify_symbolic-0.25-5.log
