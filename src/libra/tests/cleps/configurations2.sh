#!/usr/bin/env bash
###################################################
# experiment A: different analysis configurations #
###################################################

#=======#
# boxes #
#=======#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-boxes-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-boxes-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-boxes-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-boxes-0.25-5.log

#==========#
# symbolic #
#==========#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain symbolic --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-symbolic-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain symbolic --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-symbolic-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain symbolic --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-symbolic-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain symbolic --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-symbolic-0.25-5.log

#==========#
# deeppoly #
#==========#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-deeppoly-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-deeppoly-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-deeppoly-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-deeppoly-0.25-5.log

#==========#
# neurify #
#==========#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-neurify-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-neurify-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-neurify-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-neurify-0.25-5.log

#===========================#
# deeppoly+neurify+symbolic #
#===========================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_neurify_symbolic-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_neurify_symbolic-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_neurify_symbolic-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_neurify_symbolic-0.25-5.log

#================#
# boxes+deeppoly #
#================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-boxes_deeppoly-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-boxes_deeppoly-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-boxes_deeppoly-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-boxes_deeppoly-0.25-5.log

#===============#
# boxes+neurify #
#===============#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_neurify --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-boxes_neurify-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_neurify --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-boxes_neurify-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_neurify --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-boxes_neurify-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_neurify --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-boxes_neurify-0.25-5.log

#===================#
# deeppoly+symbolic #
#===================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_symbolic --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_symbolic-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_symbolic --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_symbolic-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_symbolic --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_symbolic-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_symbolic --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_symbolic-0.25-5.log

#==================#
# neurify+symbolic #
#==================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify_symbolic --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-neurify_symbolic-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify_symbolic --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-neurify_symbolic-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify_symbolic --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-neurify_symbolic-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain neurify_symbolic --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-neurify_symbolic-0.25-5.log

#==================#
# deeppoly+neurify #
#==================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_neurify-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_neurify-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-deeppoly_neurify-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain deeppoly_neurify --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-deeppoly_neurify-0.25-5.log

#========================#
# boxes+deeppoly+neurify #
#========================#

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.5 --upper 3 --cpu 32 | tee $1/census-20-boxes_deeppoly_neurify-0.5-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.5 --upper 5 --cpu 32 | tee $1/census-20-boxes_deeppoly_neurify-0.5-5.log

$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.25 --upper 3 --cpu 32 | tee $1/census-20-boxes_deeppoly_neurify-0.25-3.log
$LIBRA $LIBRA_REPO/tests/census/census.txt $LIBRA_REPO/tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.25 --upper 5 --cpu 32 | tee $1/census-20-boxes_deeppoly_neurify-0.25-5.log
