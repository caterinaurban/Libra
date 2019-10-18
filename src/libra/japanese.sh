#!/usr/bin/env bash

###########
# experiment 1: differently biased networks
###########

#=========#
# p=0.5
#=========#

#---------#
# no-bias
#---------#

#gtimeout 7200 python3 japaneseX.py False False 0.5 4 tests/japanese/small-no-bias.py | tee japanese-no-bias-nosym-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 6 tests/japanese/small-no-bias.py | tee japanese-no-bias-nosym-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 8 tests/japanese/small-no-bias.py | tee japanese-no-bias-nosym-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 10 tests/japanese/small-no-bias.py | tee japanese-no-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py True False 0.5 4 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym1-0.5-4.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 6 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym1-0.5-6.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 8 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym1-0.5-8.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 10 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py False True 0.5 4 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym2-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 6 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym2-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 8 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym2-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 10 tests/japanese/small-no-bias.py | tee japanese-no-bias-sym2-0.5-10.log

#---------#
# 0.05-bias
#---------#

#gtimeout 7200 python3 japaneseX.py False False 0.5 4 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-nosym-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 6 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-nosym-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 8 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-nosym-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 10 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py True False 0.5 4 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym1-0.5-4.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 6 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym1-0.5-6.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 8 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym1-0.5-8.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 10 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py False True 0.5 4 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym2-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 6 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym2-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 8 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym2-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 10 tests/japanese/small-0.05-bias.py | tee japanese-0.05-bias-sym2-0.5-10.log

#---------#
# 0.20-bias
#---------#

#gtimeout 7200 python3 japaneseX.py False False 0.5 4 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-nosym-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 6 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-nosym-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 8 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-nosym-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False False 0.5 10 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py True False 0.5 4 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym1-0.5-4.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 6 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym1-0.5-6.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 8 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym1-0.5-8.log
#gtimeout 7200 python3 japaneseX.py True False 0.5 10 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 japaneseX.py False True 0.5 4 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym2-0.5-4.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 6 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym2-0.5-6.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 8 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym2-0.5-8.log
#gtimeout 7200 python3 japaneseX.py False True 0.5 10 tests/japanese/small-0.20-bias.py | tee japanese-0.20-bias-sym2-0.5-10.log

#=========#
# p=0.25
#=========#

#=========#
# p=0.125
#=========#

###########
# experiment 2: differently sized networks
###########

#=========#
# p=0.5
#=========#

#---------#
# tiny-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.5 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.5-4.log
gtimeout 46800 python3 japaneseX.py False False 0.5 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.5-6.log
gtimeout 46800 python3 japaneseX.py False False 0.5 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.5-8.log
gtimeout 46800 python3 japaneseX.py False False 0.5 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.5-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.5 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.5-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.5-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.5-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.5-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.5 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.5-4.log
gtimeout 46800 python3 japaneseX.py False True 0.5 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.5-6.log
gtimeout 46800 python3 japaneseX.py False True 0.5 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.5-8.log
gtimeout 46800 python3 japaneseX.py False True 0.5 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.5-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.5 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.5-4.log
gtimeout 46800 python3 japaneseX.py False False 0.5 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.5-6.log
gtimeout 46800 python3 japaneseX.py False False 0.5 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.5-8.log
gtimeout 46800 python3 japaneseX.py False False 0.5 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.5-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.5 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.5-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.5-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.5-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.5-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.5 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.5-4.log
gtimeout 46800 python3 japaneseX.py False True 0.5 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.5-6.log
gtimeout 46800 python3 japaneseX.py False True 0.5 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.5-8.log
gtimeout 46800 python3 japaneseX.py False True 0.5 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.5-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.5 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.5-4.log
gtimeout 46800 python3 japaneseX.py False False 0.5 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.5-6.log
gtimeout 46800 python3 japaneseX.py False False 0.5 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.5-8.log
gtimeout 46800 python3 japaneseX.py False False 0.5 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.5-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.5 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.5-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.5-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.5-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.5-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.5 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.5-4.log
gtimeout 46800 python3 japaneseX.py False True 0.5 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.5-6.log
gtimeout 46800 python3 japaneseX.py False True 0.5 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.5-8.log
gtimeout 46800 python3 japaneseX.py False True 0.5 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.5-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.5 4 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.5-4.log
gtimeout 46800 python3 japaneseX.py False False 0.5 6 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.5-6.log
gtimeout 46800 python3 japaneseX.py False False 0.5 8 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.5-8.log
gtimeout 46800 python3 japaneseX.py False False 0.5 10 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.5-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.5 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.5-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.5-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.5-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.5 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.5-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.5 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.5-4.log
gtimeout 46800 python3 japaneseX.py False True 0.5 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.5-6.log
gtimeout 46800 python3 japaneseX.py False True 0.5 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.5-8.log
gtimeout 46800 python3 japaneseX.py False True 0.5 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.5-10.log

#=========#
# p=0.25
#=========#

#---------#
# tiny-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.25 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.25-4.log
gtimeout 46800 python3 japaneseX.py False False 0.25 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.25-6.log
gtimeout 46800 python3 japaneseX.py False False 0.25 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.25-8.log
gtimeout 46800 python3 japaneseX.py False False 0.25 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.25-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.25 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.25-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.25-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.25-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.25-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.25 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.25-4.log
gtimeout 46800 python3 japaneseX.py False True 0.25 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.25-6.log
gtimeout 46800 python3 japaneseX.py False True 0.25 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.25-8.log
gtimeout 46800 python3 japaneseX.py False True 0.25 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.25-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.25 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.25-4.log
gtimeout 46800 python3 japaneseX.py False False 0.25 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.25-6.log
gtimeout 46800 python3 japaneseX.py False False 0.25 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.25-8.log
gtimeout 46800 python3 japaneseX.py False False 0.25 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.25-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.25 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.25-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.25-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.25-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.25-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.25 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.25-4.log
gtimeout 46800 python3 japaneseX.py False True 0.25 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.25-6.log
gtimeout 46800 python3 japaneseX.py False True 0.25 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.25-8.log
gtimeout 46800 python3 japaneseX.py False True 0.25 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.25-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.25 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.25-4.log
gtimeout 46800 python3 japaneseX.py False False 0.25 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.25-6.log
gtimeout 46800 python3 japaneseX.py False False 0.25 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.25-8.log
gtimeout 46800 python3 japaneseX.py False False 0.25 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.25-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.25 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.25-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.25-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.25-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.25-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.25 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.25-4.log
gtimeout 46800 python3 japaneseX.py False True 0.25 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.25-6.log
gtimeout 46800 python3 japaneseX.py False True 0.25 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.25-8.log
gtimeout 46800 python3 japaneseX.py False True 0.25 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.25-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.25 4 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.25-4.log
gtimeout 46800 python3 japaneseX.py False False 0.25 6 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.25-6.log
gtimeout 46800 python3 japaneseX.py False False 0.25 8 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.25-8.log
gtimeout 46800 python3 japaneseX.py False False 0.25 10 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.25-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.25 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.25-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.25-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.25-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.25 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.25-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.25 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.25-4.log
gtimeout 46800 python3 japaneseX.py False True 0.25 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.25-6.log
gtimeout 46800 python3 japaneseX.py False True 0.25 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.25-8.log
gtimeout 46800 python3 japaneseX.py False True 0.25 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.25-10.log

#=========#
# p=0.125
#=========#

#---------#
# tiny-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.125 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.125-4.log
gtimeout 46800 python3 japaneseX.py False False 0.125 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.125-6.log
gtimeout 46800 python3 japaneseX.py False False 0.125 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.125-8.log
gtimeout 46800 python3 japaneseX.py False False 0.125 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-nosym-0.125-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.125 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.125-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.125-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.125-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym1-0.125-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.125 4 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.125-4.log
gtimeout 46800 python3 japaneseX.py False True 0.125 6 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.125-6.log
gtimeout 46800 python3 japaneseX.py False True 0.125 8 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.125-8.log
gtimeout 46800 python3 japaneseX.py False True 0.125 10 tests/japanese/tiny-layers.py | tee japanese-tiny-layers-sym2-0.125-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.125 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.125-4.log
gtimeout 46800 python3 japaneseX.py False False 0.125 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.125-6.log
gtimeout 46800 python3 japaneseX.py False False 0.125 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.125-8.log
gtimeout 46800 python3 japaneseX.py False False 0.125 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-nosym-0.125-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.125 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.125-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.125-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.125-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym1-0.125-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.125 4 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.125-4.log
gtimeout 46800 python3 japaneseX.py False True 0.125 6 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.125-6.log
gtimeout 46800 python3 japaneseX.py False True 0.125 8 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.125-8.log
gtimeout 46800 python3 japaneseX.py False True 0.125 10 tests/japanese/tiny-neurons.py | tee japanese-tiny-neurons-sym2-0.125-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.125 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.125-4.log
gtimeout 46800 python3 japaneseX.py False False 0.125 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.125-6.log
gtimeout 46800 python3 japaneseX.py False False 0.125 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.125-8.log
gtimeout 46800 python3 japaneseX.py False False 0.125 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-nosym-0.125-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.125 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.125-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.125-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.125-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym1-0.125-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.125 4 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.125-4.log
gtimeout 46800 python3 japaneseX.py False True 0.125 6 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.125-6.log
gtimeout 46800 python3 japaneseX.py False True 0.125 8 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.125-8.log
gtimeout 46800 python3 japaneseX.py False True 0.125 10 tests/japanese/large-neurons.py | tee japanese-large-neurons-sym2-0.125-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 japaneseX.py False False 0.125 4 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.125-4.log
gtimeout 46800 python3 japaneseX.py False False 0.125 6 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.125-6.log
gtimeout 46800 python3 japaneseX.py False False 0.125 8 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.125-8.log
gtimeout 46800 python3 japaneseX.py False False 0.125 10 tests/japanese/large-layers.py | tee japanese-large-layers-nosym-0.125-10.log
#
#gtimeout 46800 python3 japaneseX.py True False 0.125 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.125-4.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.125-6.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.125-8.log
#gtimeout 46800 python3 japaneseX.py True False 0.125 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym1-0.125-10.log
#
gtimeout 46800 python3 japaneseX.py False True 0.125 4 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.125-4.log
gtimeout 46800 python3 japaneseX.py False True 0.125 6 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.125-6.log
gtimeout 46800 python3 japaneseX.py False True 0.125 8 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.125-8.log
gtimeout 46800 python3 japaneseX.py False True 0.125 10 tests/japanese/large-layers.py | tee japanese-large-layers-sym2-0.125-10.log
