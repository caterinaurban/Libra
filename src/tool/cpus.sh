#!/usr/bin/env bash
##########################################
# Experiment 3: Leveraging Multiple CPUs #
##########################################

#=======#
# boxes #
#=======#

$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs3/census-20-boxes-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs3/census-20-boxes-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs3/census-20-boxes-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs3/census-20-boxes-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs3/census-20-boxes-4cpu.log

#==========#
# symbolic #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs3/census-20-symbolic-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs3/census-20-symbolic-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs3/census-20-symbolic-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs3/census-20-symbolic-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs3/census-20-symbolic-4cpu.log

#==========#
# deeppoly #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs3/census-20-deeppoly-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs3/census-20-deeppoly-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs3/census-20-deeppoly-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs3/census-20-deeppoly-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs3/census-20-deeppoly-4cpu.log

#==========#
# neurify #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs3/census-20-neurify-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs3/census-20-neurify-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs3/census-20-neurify-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs3/census-20-neurify-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs3/census-20-neurify-4cpu.log

#===========================#
# deeppoly+neurify+symbolic #
#===========================#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs3/census-20-deeppoly_neurify_symbolic-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs3/census-20-deeppoly_neurify_symbolic-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs3/census-20-deeppoly_neurify_symbolic-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs3/census-20-deeppoly_neurify_symbolic-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs3/census-20-deeppoly_neurify_symbolic-4cpu.log
