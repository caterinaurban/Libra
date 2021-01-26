#!/usr/bin/env bash
###################################################
# experiment A: different analysis configurations #
###################################################

LIBRA=$1

#=======#
# boxes #
#=======#

$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-boxes-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-boxes-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-boxes-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-boxes-0.25-5.log

#==========#
# symbolic #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-symbolic-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-symbolic-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-symbolic-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain symbolic --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-symbolic-0.25-5.log

#==========#
# deeppoly #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-deeppoly-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-deeppoly-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-deeppoly-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-deeppoly-0.25-5.log

#==========#
# neurify #
#==========#

$1 tests/census/census.txt tests/census/20.py --domain neurify --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-neurify-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-neurify-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain neurify --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-neurify-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain neurify --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-neurify-0.25-5.log

#===========================#
# deeppoly+neurify+symbolic #
#===========================#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-deeppoly_neurify_symbolic-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-deeppoly_neurify_symbolic-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-deeppoly_neurify_symbolic-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify_symbolic --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-deeppoly_neurify_symbolic-0.25-5.log

#================#
# boxes+deeppoly #
#================#

$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-boxes_deeppoly-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-boxes_deeppoly-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-boxes_deeppoly-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-boxes_deeppoly-0.25-5.log

#===============#
# boxes+neurify #
#===============#

$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-boxes_neurify-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-boxes_neurify-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-boxes_neurify-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_neurify --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-boxes_neurify-0.25-5.log

#===================#
# deeppoly+symbolic #
#===================#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_symbolic --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-deeppoly_symbolic-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_symbolic --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-deeppoly_symbolic-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_symbolic --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-deeppoly_symbolic-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_symbolic --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-deeppoly_symbolic-0.25-5.log

#==================#
# neurify+symbolic #
#==================#

$1 tests/census/census.txt tests/census/20.py --domain neurify_symbolic --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-neurify_symbolic-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain neurify_symbolic --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-neurify_symbolic-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain neurify_symbolic --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-neurify_symbolic-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain neurify_symbolic --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-neurify_symbolic-0.25-5.log

#==================#
# deeppoly+neurify #
#==================#

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-deeppoly_neurify-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-deeppoly_neurify-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-deeppoly_neurify-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain deeppoly_neurify --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-deeppoly_neurify-0.25-5.log

#========================#
# boxes+deeppoly+neurify #
#========================#

$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.5 --upper 3 | tee tests/census/logs5/census-20-boxes_deeppoly_neurify-0.5-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.5 --upper 5 | tee tests/census/logs5/census-20-boxes_deeppoly_neurify-0.5-5.log

$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.25 --upper 3 | tee tests/census/logs5/census-20-boxes_deeppoly_neurify-0.25-3.log
$1 tests/census/census.txt tests/census/20.py --domain boxes_deeppoly_neurify --lower 0.25 --upper 5 | tee tests/census/logs5/census-20-boxes_deeppoly_neurify-0.25-5.log
