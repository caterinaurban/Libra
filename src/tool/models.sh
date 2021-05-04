#!/usr/bin/env bash
#################################################################################
# Experiment 1: Effect of Neural Network Structure on Precision and Scalability #
#################################################################################

#----#
# 10 #
#----#

tool tests/census/census.txt tests/census/10.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs1/census-10-boxes-0.5-5.log
tool tests/census/census.txt tests/census/10.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-10-symbolic-0.5-5.log
tool tests/census/census.txt tests/census/10.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs1/census-10-deeppoly-0.5-5.log
tool tests/census/census.txt tests/census/10.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs1/census-10-neurify-0.5-5.log
tool tests/census/census.txt tests/census/10.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-10-deeppoly_neurify_symbolic-0.5-5.log

#---------#
# 12
#---------#

tool tests/census/census.txt tests/census/12.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs1/census-12-boxes-0.5-5.log
tool tests/census/census.txt tests/census/12.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-12-symbolic-0.5-5.log
tool tests/census/census.txt tests/census/12.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs1/census-12-deeppoly-0.5-5.log
tool tests/census/census.txt tests/census/12.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs1/census-12-neurify-0.5-5.log
tool tests/census/census.txt tests/census/12.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-12-deeppoly_neurify_symbolic-0.5-5.log

#---------#
# 20
#---------#

tool tests/census/census.txt tests/census/20.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs1/census-20-boxes-0.5-5.log
tool tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-20-symbolic-0.5-5.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs1/census-20-deeppoly-0.5-5.log
tool tests/census/census.txt tests/census/20.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs1/census-20-neurify-0.5-5.log
tool tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-20-deeppoly_neurify_symbolic-0.5-5.log

#---------#
# 40
#---------#

tool tests/census/census.txt tests/census/40.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs1/census-40-boxes-0.5-5.log
tool tests/census/census.txt tests/census/40.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-40-symbolic-0.5-5.log
tool tests/census/census.txt tests/census/40.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs1/census-40-deeppoly-0.5-5.log
tool tests/census/census.txt tests/census/40.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs1/census-40-neurify-0.5-5.log
tool tests/census/census.txt tests/census/40.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-40-deeppoly_neurify_symbolic-0.5-5.log

#---------#
# 45
#---------#

tool tests/census/census.txt tests/census/45.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs1/census-45-boxes-0.5-5.log
tool tests/census/census.txt tests/census/45.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-45-symbolic-0.5-5.log
tool tests/census/census.txt tests/census/45.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs1/census-45-deeppoly-0.5-5.log
tool tests/census/census.txt tests/census/45.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs1/census-45-neurify-0.5-5.log
tool tests/census/census.txt tests/census/45.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs1/census-45-deeppoly_neurify_symbolic-0.5-5.log
