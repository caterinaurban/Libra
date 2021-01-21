#!/usr/bin/env bash
############################
# experiment D: autotuning #
############################

LIBRA=$1

#==========#
# symbolic #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 | tee tests/census/logs4/census-20-symbolic.log
