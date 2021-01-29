#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################

LIBRA=$1

#===============#
# boxes+neurify #
#===============#

$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.015625 --upper 6 --cpu 64 | tee tests/census/logs8/census-20-boxes_neurify-64cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.015625 --upper 6 --cpu 32 | tee tests/census/logs8/census-20-boxes_neurify-32cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.015625 --upper 6 --cpu 16 | tee tests/census/logs8/census-20-boxes_neurify-16cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.015625 --upper 6 --cpu 8 | tee tests/census/logs8/census-20-boxes_neurify-8cpu.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.015625 --upper 6 --cpu 4 | tee tests/census/logs8/census-20-boxes_neurify-4cpu.log
