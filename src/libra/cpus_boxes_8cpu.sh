#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################

LIBRA=$1

#=======#
# boxes #
#=======#

$1 tests/census/census.txt tests/census/20.py --domain boxes --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs6/census-20-boxes-8cpu.log
