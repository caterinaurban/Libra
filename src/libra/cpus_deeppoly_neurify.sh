#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################

LIBRA=$1

#==================#
# deeppoly+neurify #
#==================#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/census/logs6/census-20-deeppoly_neurify-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/census/logs6/census-20-deeppoly_neurify-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/census/logs6/census-20-deeppoly_neurify-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/census/logs6/census-20-deeppoly_neurify-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/census/logs6/census-20-deeppoly_neurify-4cpu.log
