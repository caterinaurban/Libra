#!/usr/bin/env bash
###################################################
# experiment 4: different analysis configurations #
###################################################

LIBRA=$1

#=======#
# boxes #
#=======#


if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-boxes-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-boxes-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-boxes-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-boxes-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-boxes-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-boxes-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-boxes-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-boxes-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-boxes-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-boxes-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-boxes-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-boxes-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-boxes-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-boxes-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-boxes-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-boxes-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain boxes --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-boxes-0-10.log
fi

#==========#
# symbolic #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-symbolic-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain symbolic --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-symbolic-0-10.log
fi

#==========#
# deeppoly #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-deeppoly-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-deeppoly-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-deeppoly-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-deeppoly-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-deeppoly-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-deeppoly-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-deeppoly-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain deeppoly --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-deeppoly-0-10.log
fi

#==========#
# neurify #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-neurify-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-neurify-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-neurify-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-neurify-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-neurify-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-neurify-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-neurify-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-neurify-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-neurify-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-neurify-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-neurify-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-neurify-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-neurify-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-neurify-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-neurify-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-neurify-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain neurify --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-neurify-0-10.log
fi

#==========#
# product deeppoly symbolic #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_symbolic --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_symbolic-0-10.log
fi

#==========#
# product deeppoly neurify #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_deeppoly_neurify --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-product_deeppoly_neurify-0-10.log
fi

#==========#
# product neurify symbolic #
#==========#

if [ ! -z $2 ]
then
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 4 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 6 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 8 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 10 --cpu $2 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-10.log
else
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 4 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 6 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 8 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.5 --upper 10 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.5-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 4 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 6 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 8 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.25 --upper 10 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.25-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 4 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 6 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 8 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0.125 --upper 10 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0.125-10.log

    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 4 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-4.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 6 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-6.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 8 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-8.log
    $1 tests/japanese/japanese.txt tests/japanese/20.py --domain product_neurify_symbolic --lower 0 --upper 10 | tee tests/japanese/logs/japanese-20-product_neurify_symbolic-0-10.log
fi