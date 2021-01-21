#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################

LIBRA=$1

#===================#
# deeppoly+symbolic #
#===================#

$1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee tests/japanese/logs3/japanese-20-deeppoly_symbolic-64cpu.log
$1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee tests/japanese/logs3/japanese-20-deeppoly_symbolic-32cpu.log
$1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee tests/japanese/logs3/japanese-20-deeppoly_symbolic-16cpu.log
$1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee tests/japanese/logs3/japanese-20-deeppoly_symbolic-8cpu.log
$1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly_symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee tests/japanese/logs3/japanese-20-deeppoly_symbolic-4cpu.log
