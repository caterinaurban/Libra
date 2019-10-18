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

#gtimeout 7200 python3 censusX.py False False 0.5 4 tests/census/small-no-bias.py | tee census-no-bias-nosym-0.5-4.log
#gtimeout 7200 python3 censusX.py False False 0.5 6 tests/census/small-no-bias.py | tee census-no-bias-nosym-0.5-6.log
#gtimeout 7200 python3 censusX.py False False 0.5 8 tests/census/small-no-bias.py | tee census-no-bias-nosym-0.5-8.log
#gtimeout 7200 python3 censusX.py False False 0.5 10 tests/census/small-no-bias.py | tee census-no-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 censusX.py True False 0.5 4 tests/census/small-no-bias.py | tee census-no-bias-sym1-0.5-4.log
#gtimeout 7200 python3 censusX.py True False 0.5 6 tests/census/small-no-bias.py | tee census-no-bias-sym1-0.5-6.log
#gtimeout 7200 python3 censusX.py True False 0.5 8 tests/census/small-no-bias.py | tee census-no-bias-sym1-0.5-8.log
#gtimeout 7200 python3 censusX.py True False 0.5 10 tests/census/small-no-bias.py | tee census-no-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 censusX.py False True 0.5 4 tests/census/small-no-bias.py | tee census-no-bias-sym2-0.5-4.log
#gtimeout 7200 python3 censusX.py False True 0.5 6 tests/census/small-no-bias.py | tee census-no-bias-sym2-0.5-6.log
#gtimeout 7200 python3 censusX.py False True 0.5 8 tests/census/small-no-bias.py | tee census-no-bias-sym2-0.5-8.log
#gtimeout 7200 python3 censusX.py False True 0.5 10 tests/census/small-no-bias.py | tee census-no-bias-sym2-0.5-10.log

#---------#
# 0.05-bias
#---------#

#gtimeout 7200 python3 censusX.py False False 0.5 4 tests/census/small-0.05-bias.py | tee census-0.05-bias-nosym-0.5-4.log
#gtimeout 7200 python3 censusX.py False False 0.5 6 tests/census/small-0.05-bias.py | tee census-0.05-bias-nosym-0.5-6.log
#gtimeout 7200 python3 censusX.py False False 0.5 8 tests/census/small-0.05-bias.py | tee census-0.05-bias-nosym-0.5-8.log
#gtimeout 7200 python3 censusX.py False False 0.5 10 tests/census/small-0.05-bias.py | tee census-0.05-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 censusX.py True False 0.5 4 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym1-0.5-4.log
#gtimeout 7200 python3 censusX.py True False 0.5 6 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym1-0.5-6.log
#gtimeout 7200 python3 censusX.py True False 0.5 8 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym1-0.5-8.log
#gtimeout 7200 python3 censusX.py True False 0.5 10 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 censusX.py False True 0.5 4 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym2-0.5-4.log
#gtimeout 7200 python3 censusX.py False True 0.5 6 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym2-0.5-6.log
#gtimeout 7200 python3 censusX.py False True 0.5 8 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym2-0.5-8.log
#gtimeout 7200 python3 censusX.py False True 0.5 10 tests/census/small-0.05-bias.py | tee census-0.05-bias-sym2-0.5-10.log

#---------#
# 0.20-bias
#---------#

#gtimeout 7200 python3 censusX.py False False 0.5 4 tests/census/small-0.20-bias.py | tee census-0.20-bias-nosym-0.5-4.log
#gtimeout 7200 python3 censusX.py False False 0.5 6 tests/census/small-0.20-bias.py | tee census-0.20-bias-nosym-0.5-6.log
#gtimeout 7200 python3 censusX.py False False 0.5 8 tests/census/small-0.20-bias.py | tee census-0.20-bias-nosym-0.5-8.log
#gtimeout 7200 python3 censusX.py False False 0.5 10 tests/census/small-0.20-bias.py | tee census-0.20-bias-nosym-0.5-10.log
#
#gtimeout 7200 python3 censusX.py True False 0.5 4 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym1-0.5-4.log
#gtimeout 7200 python3 censusX.py True False 0.5 6 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym1-0.5-6.log
#gtimeout 7200 python3 censusX.py True False 0.5 8 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym1-0.5-8.log
#gtimeout 7200 python3 censusX.py True False 0.5 10 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym1-0.5-10.log
#
#gtimeout 7200 python3 censusX.py False True 0.5 4 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym2-0.5-4.log
#gtimeout 7200 python3 censusX.py False True 0.5 6 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym2-0.5-6.log
#gtimeout 7200 python3 censusX.py False True 0.5 8 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym2-0.5-8.log
#gtimeout 7200 python3 censusX.py False True 0.5 10 tests/census/small-0.20-bias.py | tee census-0.20-bias-sym2-0.5-10.log

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

gtimeout 46800 python3 censusX.py False False 0.5 4 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.5-4.log
gtimeout 46800 python3 censusX.py False False 0.5 6 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.5-6.log
gtimeout 46800 python3 censusX.py False False 0.5 8 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.5-8.log
gtimeout 46800 python3 censusX.py False False 0.5 10 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.5-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.5 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.5-4.log
#gtimeout 46800 python3 censusX.py True False 0.5 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.5-6.log
#gtimeout 46800 python3 censusX.py True False 0.5 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.5-8.log
#gtimeout 46800 python3 censusX.py True False 0.5 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.5-10.log
#
gtimeout 46800 python3 censusX.py False True 0.5 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.5-4.log
gtimeout 46800 python3 censusX.py False True 0.5 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.5-6.log
gtimeout 46800 python3 censusX.py False True 0.5 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.5-8.log
gtimeout 46800 python3 censusX.py False True 0.5 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.5-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.5 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.5-4.log
gtimeout 46800 python3 censusX.py False False 0.5 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.5-6.log
gtimeout 46800 python3 censusX.py False False 0.5 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.5-8.log
gtimeout 46800 python3 censusX.py False False 0.5 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.5-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.5 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.5-4.log
#gtimeout 46800 python3 censusX.py True False 0.5 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.5-6.log
#gtimeout 46800 python3 censusX.py True False 0.5 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.5-8.log
#gtimeout 46800 python3 censusX.py True False 0.5 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.5-10.log
#
gtimeout 46800 python3 censusX.py False True 0.5 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.5-4.log
gtimeout 46800 python3 censusX.py False True 0.5 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.5-6.log
gtimeout 46800 python3 censusX.py False True 0.5 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.5-8.log
gtimeout 46800 python3 censusX.py False True 0.5 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.5-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.5 4 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.5-4.log
gtimeout 46800 python3 censusX.py False False 0.5 6 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.5-6.log
gtimeout 46800 python3 censusX.py False False 0.5 8 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.5-8.log
gtimeout 46800 python3 censusX.py False False 0.5 10 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.5-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.5 4 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.5-4.log
#gtimeout 46800 python3 censusX.py True False 0.5 6 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.5-6.log
#gtimeout 46800 python3 censusX.py True False 0.5 8 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.5-8.log
#gtimeout 46800 python3 censusX.py True False 0.5 10 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.5-10.log
#
gtimeout 46800 python3 censusX.py False True 0.5 4 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.5-4.log
gtimeout 46800 python3 censusX.py False True 0.5 6 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.5-6.log
gtimeout 46800 python3 censusX.py False True 0.5 8 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.5-8.log
gtimeout 46800 python3 censusX.py False True 0.5 10 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.5-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 censusX.py False False 0.5 4 tests/census/large-layers.py | tee census-large-layers-nosym-0.5-4.log
gtimeout 46800 python3 censusX.py False False 0.5 6 tests/census/large-layers.py | tee census-large-layers-nosym-0.5-6.log
gtimeout 46800 python3 censusX.py False False 0.5 8 tests/census/large-layers.py | tee census-large-layers-nosym-0.5-8.log
gtimeout 46800 python3 censusX.py False False 0.5 10 tests/census/large-layers.py | tee census-large-layers-nosym-0.5-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.5 4 tests/census/large-layers.py | tee census-large-layers-sym1-0.5-4.log
#gtimeout 46800 python3 censusX.py True False 0.5 6 tests/census/large-layers.py | tee census-large-layers-sym1-0.5-6.log
#gtimeout 46800 python3 censusX.py True False 0.5 8 tests/census/large-layers.py | tee census-large-layers-sym1-0.5-8.log
#gtimeout 46800 python3 censusX.py True False 0.5 10 tests/census/large-layers.py | tee census-large-layers-sym1-0.5-10.log
#
gtimeout 46800 python3 censusX.py False True 0.5 4 tests/census/large-layers.py | tee census-large-layers-sym2-0.5-4.log
gtimeout 46800 python3 censusX.py False True 0.5 6 tests/census/large-layers.py | tee census-large-layers-sym2-0.5-6.log
gtimeout 46800 python3 censusX.py False True 0.5 8 tests/census/large-layers.py | tee census-large-layers-sym2-0.5-8.log
gtimeout 46800 python3 censusX.py False True 0.5 10 tests/census/large-layers.py | tee census-large-layers-sym2-0.5-10.log

#=========#
# p=0.25
#=========#

#---------#
# tiny-layers
#---------#

gtimeout 46800 python3 censusX.py False False 0.25 4 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.25-4.log
gtimeout 46800 python3 censusX.py False False 0.25 6 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.25-6.log
gtimeout 46800 python3 censusX.py False False 0.25 8 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.25-8.log
gtimeout 46800 python3 censusX.py False False 0.25 10 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.25-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.25 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.25-4.log
#gtimeout 46800 python3 censusX.py True False 0.25 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.25-6.log
#gtimeout 46800 python3 censusX.py True False 0.25 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.25-8.log
#gtimeout 46800 python3 censusX.py True False 0.25 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.25-10.log
#
gtimeout 46800 python3 censusX.py False True 0.25 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.25-4.log
gtimeout 46800 python3 censusX.py False True 0.25 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.25-6.log
gtimeout 46800 python3 censusX.py False True 0.25 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.25-8.log
gtimeout 46800 python3 censusX.py False True 0.25 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.25-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.25 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.25-4.log
gtimeout 46800 python3 censusX.py False False 0.25 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.25-6.log
gtimeout 46800 python3 censusX.py False False 0.25 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.25-8.log
gtimeout 46800 python3 censusX.py False False 0.25 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.25-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.25 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.25-4.log
#gtimeout 46800 python3 censusX.py True False 0.25 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.25-6.log
#gtimeout 46800 python3 censusX.py True False 0.25 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.25-8.log
#gtimeout 46800 python3 censusX.py True False 0.25 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.25-10.log
#
gtimeout 46800 python3 censusX.py False True 0.25 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.25-4.log
gtimeout 46800 python3 censusX.py False True 0.25 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.25-6.log
gtimeout 46800 python3 censusX.py False True 0.25 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.25-8.log
gtimeout 46800 python3 censusX.py False True 0.25 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.25-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.25 4 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.25-4.log
gtimeout 46800 python3 censusX.py False False 0.25 6 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.25-6.log
gtimeout 46800 python3 censusX.py False False 0.25 8 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.25-8.log
gtimeout 46800 python3 censusX.py False False 0.25 10 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.25-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.25 4 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.25-4.log
#gtimeout 46800 python3 censusX.py True False 0.25 6 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.25-6.log
#gtimeout 46800 python3 censusX.py True False 0.25 8 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.25-8.log
#gtimeout 46800 python3 censusX.py True False 0.25 10 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.25-10.log
#
gtimeout 46800 python3 censusX.py False True 0.25 4 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.25-4.log
gtimeout 46800 python3 censusX.py False True 0.25 6 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.25-6.log
gtimeout 46800 python3 censusX.py False True 0.25 8 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.25-8.log
gtimeout 46800 python3 censusX.py False True 0.25 10 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.25-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 censusX.py False False 0.25 4 tests/census/large-layers.py | tee census-large-layers-nosym-0.25-4.log
gtimeout 46800 python3 censusX.py False False 0.25 6 tests/census/large-layers.py | tee census-large-layers-nosym-0.25-6.log
gtimeout 46800 python3 censusX.py False False 0.25 8 tests/census/large-layers.py | tee census-large-layers-nosym-0.25-8.log
gtimeout 46800 python3 censusX.py False False 0.25 10 tests/census/large-layers.py | tee census-large-layers-nosym-0.25-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.25 4 tests/census/large-layers.py | tee census-large-layers-sym1-0.25-4.log
#gtimeout 46800 python3 censusX.py True False 0.25 6 tests/census/large-layers.py | tee census-large-layers-sym1-0.25-6.log
#gtimeout 46800 python3 censusX.py True False 0.25 8 tests/census/large-layers.py | tee census-large-layers-sym1-0.25-8.log
#gtimeout 46800 python3 censusX.py True False 0.25 10 tests/census/large-layers.py | tee census-large-layers-sym1-0.25-10.log
#
gtimeout 46800 python3 censusX.py False True 0.25 4 tests/census/large-layers.py | tee census-large-layers-sym2-0.25-4.log
gtimeout 46800 python3 censusX.py False True 0.25 6 tests/census/large-layers.py | tee census-large-layers-sym2-0.25-6.log
gtimeout 46800 python3 censusX.py False True 0.25 8 tests/census/large-layers.py | tee census-large-layers-sym2-0.25-8.log
gtimeout 46800 python3 censusX.py False True 0.25 10 tests/census/large-layers.py | tee census-large-layers-sym2-0.25-10.log

#=========#
# p=0.125
#=========#

#---------#
# tiny-layers
#---------#

gtimeout 46800 python3 censusX.py False False 0.125 4 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.125-4.log
gtimeout 46800 python3 censusX.py False False 0.125 6 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.125-6.log
gtimeout 46800 python3 censusX.py False False 0.125 8 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.125-8.log
gtimeout 46800 python3 censusX.py False False 0.125 10 tests/census/tiny-layers.py | tee census-tiny-layers-nosym-0.125-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.125 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.125-4.log
#gtimeout 46800 python3 censusX.py True False 0.125 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.125-6.log
#gtimeout 46800 python3 censusX.py True False 0.125 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.125-8.log
#gtimeout 46800 python3 censusX.py True False 0.125 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym1-0.125-10.log
#
gtimeout 46800 python3 censusX.py False True 0.125 4 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.125-4.log
gtimeout 46800 python3 censusX.py False True 0.125 6 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.125-6.log
gtimeout 46800 python3 censusX.py False True 0.125 8 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.125-8.log
gtimeout 46800 python3 censusX.py False True 0.125 10 tests/census/tiny-layers.py | tee census-tiny-layers-sym2-0.125-10.log

#---------#
# tiny-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.125 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.125-4.log
gtimeout 46800 python3 censusX.py False False 0.125 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.125-6.log
gtimeout 46800 python3 censusX.py False False 0.125 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.125-8.log
gtimeout 46800 python3 censusX.py False False 0.125 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-nosym-0.125-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.125 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.125-4.log
#gtimeout 46800 python3 censusX.py True False 0.125 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.125-6.log
#gtimeout 46800 python3 censusX.py True False 0.125 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.125-8.log
#gtimeout 46800 python3 censusX.py True False 0.125 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym1-0.125-10.log
#
gtimeout 46800 python3 censusX.py False True 0.125 4 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.125-4.log
gtimeout 46800 python3 censusX.py False True 0.125 6 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.125-6.log
gtimeout 46800 python3 censusX.py False True 0.125 8 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.125-8.log
gtimeout 46800 python3 censusX.py False True 0.125 10 tests/census/tiny-neurons.py | tee census-tiny-neurons-sym2-0.125-10.log

#---------#
# small-no-bias
#---------#

# done in experiment #1

#---------#
# large-neurons
#---------#

gtimeout 46800 python3 censusX.py False False 0.125 4 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.125-4.log
gtimeout 46800 python3 censusX.py False False 0.125 6 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.125-6.log
gtimeout 46800 python3 censusX.py False False 0.125 8 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.125-8.log
gtimeout 46800 python3 censusX.py False False 0.125 10 tests/census/large-neurons.py | tee census-large-neurons-nosym-0.125-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.125 4 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.125-4.log
#gtimeout 46800 python3 censusX.py True False 0.125 6 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.125-6.log
#gtimeout 46800 python3 censusX.py True False 0.125 8 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.125-8.log
#gtimeout 46800 python3 censusX.py True False 0.125 10 tests/census/large-neurons.py | tee census-large-neurons-sym1-0.125-10.log
#
gtimeout 46800 python3 censusX.py False True 0.125 4 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.125-4.log
gtimeout 46800 python3 censusX.py False True 0.125 6 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.125-6.log
gtimeout 46800 python3 censusX.py False True 0.125 8 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.125-8.log
gtimeout 46800 python3 censusX.py False True 0.125 10 tests/census/large-neurons.py | tee census-large-neurons-sym2-0.125-10.log

#---------#
# large-layers
#---------#

gtimeout 46800 python3 censusX.py False False 0.125 4 tests/census/large-layers.py | tee census-large-layers-nosym-0.125-4.log
gtimeout 46800 python3 censusX.py False False 0.125 6 tests/census/large-layers.py | tee census-large-layers-nosym-0.125-6.log
gtimeout 46800 python3 censusX.py False False 0.125 8 tests/census/large-layers.py | tee census-large-layers-nosym-0.125-8.log
gtimeout 46800 python3 censusX.py False False 0.125 10 tests/census/large-layers.py | tee census-large-layers-nosym-0.125-10.log
#
#gtimeout 46800 python3 censusX.py True False 0.125 4 tests/census/large-layers.py | tee census-large-layers-sym1-0.125-4.log
#gtimeout 46800 python3 censusX.py True False 0.125 6 tests/census/large-layers.py | tee census-large-layers-sym1-0.125-6.log
#gtimeout 46800 python3 censusX.py True False 0.125 8 tests/census/large-layers.py | tee census-large-layers-sym1-0.125-8.log
#gtimeout 46800 python3 censusX.py True False 0.125 10 tests/census/large-layers.py | tee census-large-layers-sym1-0.125-10.log
#
gtimeout 46800 python3 censusX.py False True 0.125 4 tests/census/large-layers.py | tee census-large-layers-sym2-0.125-4.log
gtimeout 46800 python3 censusX.py False True 0.125 6 tests/census/large-layers.py | tee census-large-layers-sym2-0.125-6.log
gtimeout 46800 python3 censusX.py False True 0.125 8 tests/census/large-layers.py | tee census-large-layers-sym2-0.125-8.log
gtimeout 46800 python3 censusX.py False True 0.125 10 tests/census/large-layers.py | tee census-large-layers-sym2-0.125-10.log
