#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################



#==========#
# symbolic #
#==========#

$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 64 | tee $1/census-20-symbolic-64cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 32 | tee $1/census-20-symbolic-32cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 16 | tee $1/census-20-symbolic-16cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 8 | tee $1/census-20-symbolic-8cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain symbolic --min_lower 0 --lower 1 --upper 0 --max_upper 20 --cpu 4 | tee $1/census-20-symbolic-4cpu.log
