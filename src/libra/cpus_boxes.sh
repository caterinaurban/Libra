#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################

LIBRA=$1

#=======#
# boxes #
#=======#

$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.015625 --upper 6 --cpu 64 | tee tests/census/logs8/census-20-boxes-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.015625 --upper 6 --cpu 32 | tee tests/census/logs8/census-20-boxes-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.015625 --upper 6 --cpu 16 | tee tests/census/logs8/census-20-boxes-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.015625 --upper 6 --cpu 8 | tee tests/census/logs8/census-20-boxes-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.015625 --upper 6 --cpu 4 | tee tests/census/logs8/census-20-boxes-4cpu.log
