#!/usr/bin/env bash
###########
# experiment 3: different model structures
###########

#=========#
# p=1
#=========#

#---------#
# 10
#---------#

timeout 46800 python3 censusX.py False False 1 4 tests/census/10.py | tee census-10-nosym-1-4.log
timeout 46800 python3 censusX.py False False 1 6 tests/census/10.py | tee census-10-nosym-1-6.log
timeout 46800 python3 censusX.py False False 1 8 tests/census/10.py | tee census-10-nosym-1-8.log
timeout 46800 python3 censusX.py False False 1 10 tests/census/10.py | tee census-10-nosym-1-10.log
#
timeout 46800 python3 censusX.py False True 1 4 tests/census/10.py | tee census-10-sym2-1-4.log
timeout 46800 python3 censusX.py False True 1 6 tests/census/10.py | tee census-10-sym2-1-6.log
timeout 46800 python3 censusX.py False True 1 8 tests/census/10.py | tee census-10-sym2-1-8.log
timeout 46800 python3 censusX.py False True 1 10 tests/census/10.py | tee census-10-sym2-1-10.log

#---------#
# 12
#---------#

timeout 46800 python3 censusX.py False False 1 4 tests/census/12.py | tee census-12-nosym-1-4.log
timeout 46800 python3 censusX.py False False 1 6 tests/census/12.py | tee census-12-nosym-1-6.log
timeout 46800 python3 censusX.py False False 1 8 tests/census/12.py | tee census-12-nosym-1-8.log
timeout 46800 python3 censusX.py False False 1 10 tests/census/12.py | tee census-12-nosym-1-10.log
#
timeout 46800 python3 censusX.py False True 1 4 tests/census/12.py | tee census-12-sym2-1-4.log
timeout 46800 python3 censusX.py False True 1 6 tests/census/12.py | tee census-12-sym2-1-6.log
timeout 46800 python3 censusX.py False True 1 8 tests/census/12.py | tee census-12-sym2-1-8.log
timeout 46800 python3 censusX.py False True 1 10 tests/census/12.py | tee census-12-sym2-1-10.log

#---------#
# 20
#---------#

timeout 46800 python3 censusX.py False False 1 4 tests/census/20.py | tee census-20-nosym-1-4.log
timeout 46800 python3 censusX.py False False 1 6 tests/census/20.py | tee census-20-nosym-1-6.log
timeout 46800 python3 censusX.py False False 1 8 tests/census/20.py | tee census-20-nosym-1-8.log
timeout 46800 python3 censusX.py False False 1 10 tests/census/20.py | tee census-20-nosym-1-10.log
#
timeout 46800 python3 censusX.py False True 1 4 tests/census/20.py | tee census-20-sym2-1-4.log
timeout 46800 python3 censusX.py False True 1 6 tests/census/20.py | tee census-20-sym2-1-6.log
timeout 46800 python3 censusX.py False True 1 8 tests/census/20.py | tee census-20-sym2-1-8.log
timeout 46800 python3 censusX.py False True 1 10 tests/census/20.py | tee census-20-sym2-1-10.log

#---------#
# 40
#---------#

timeout 46800 python3 censusX.py False False 1 4 tests/census/40.py | tee census-40-nosym-1-4.log
timeout 46800 python3 censusX.py False False 1 6 tests/census/40.py | tee census-40-nosym-1-6.log
timeout 46800 python3 censusX.py False False 1 8 tests/census/40.py | tee census-40-nosym-1-8.log
timeout 46800 python3 censusX.py False False 1 10 tests/census/40.py | tee census-40-nosym-1-10.log
#
timeout 46800 python3 censusX.py False True 1 4 tests/census/40.py | tee census-40-sym2-1-4.log
timeout 46800 python3 censusX.py False True 1 6 tests/census/40.py | tee census-40-sym2-1-6.log
timeout 46800 python3 censusX.py False True 1 8 tests/census/40.py | tee census-40-sym2-1-8.log
timeout 46800 python3 censusX.py False True 1 10 tests/census/40.py | tee census-40-sym2-1-10.log

#---------#
# 45
#---------#

timeout 46800 python3 censusX.py False False 1 4 tests/census/45.py | tee census-45-nosym-1-4.log
timeout 46800 python3 censusX.py False False 1 6 tests/census/45.py | tee census-45-nosym-1-6.log
timeout 46800 python3 censusX.py False False 1 8 tests/census/45.py | tee census-45-nosym-1-8.log
timeout 46800 python3 censusX.py False False 1 10 tests/census/45.py | tee census-45-nosym-1-10.log
#
timeout 46800 python3 censusX.py False True 1 4 tests/census/45.py | tee census-45-sym2-1-4.log
timeout 46800 python3 censusX.py False True 1 6 tests/census/45.py | tee census-45-sym2-1-6.log
timeout 46800 python3 censusX.py False True 1 8 tests/census/45.py | tee census-45-sym2-1-8.log
timeout 46800 python3 censusX.py False True 1 10 tests/census/45.py | tee census-45-sym2-1-10.log

#=========#
# p=0.5
#=========#

#---------#
# 10
#---------#

timeout 46800 python3 censusX.py False False 0.5 4 tests/census/10.py | tee census-10-nosym-0.5-4.log
timeout 46800 python3 censusX.py False False 0.5 6 tests/census/10.py | tee census-10-nosym-0.5-6.log
timeout 46800 python3 censusX.py False False 0.5 8 tests/census/10.py | tee census-10-nosym-0.5-8.log
timeout 46800 python3 censusX.py False False 0.5 10 tests/census/10.py | tee census-10-nosym-0.5-10.log
#
timeout 46800 python3 censusX.py False True 0.5 4 tests/census/10.py | tee census-10-sym2-0.5-4.log
timeout 46800 python3 censusX.py False True 0.5 6 tests/census/10.py | tee census-10-sym2-0.5-6.log
timeout 46800 python3 censusX.py False True 0.5 8 tests/census/10.py | tee census-10-sym2-0.5-8.log
timeout 46800 python3 censusX.py False True 0.5 10 tests/census/10.py | tee census-10-sym2-0.5-10.log

#---------#
# 12
#---------#

timeout 46800 python3 censusX.py False False 0.5 4 tests/census/12.py | tee census-12-nosym-0.5-4.log
timeout 46800 python3 censusX.py False False 0.5 6 tests/census/12.py | tee census-12-nosym-0.5-6.log
timeout 46800 python3 censusX.py False False 0.5 8 tests/census/12.py | tee census-12-nosym-0.5-8.log
timeout 46800 python3 censusX.py False False 0.5 10 tests/census/12.py | tee census-12-nosym-0.5-10.log
#
timeout 46800 python3 censusX.py False True 0.5 4 tests/census/12.py | tee census-12-sym2-0.5-4.log
timeout 46800 python3 censusX.py False True 0.5 6 tests/census/12.py | tee census-12-sym2-0.5-6.log
timeout 46800 python3 censusX.py False True 0.5 8 tests/census/12.py | tee census-12-sym2-0.5-8.log
timeout 46800 python3 censusX.py False True 0.5 10 tests/census/12.py | tee census-12-sym2-0.5-10.log

#---------#
# 20
#---------#

timeout 46800 python3 censusX.py False False 0.5 4 tests/census/20.py | tee census-20-nosym-0.5-4.log
timeout 46800 python3 censusX.py False False 0.5 6 tests/census/20.py | tee census-20-nosym-0.5-6.log
timeout 46800 python3 censusX.py False False 0.5 8 tests/census/20.py | tee census-20-nosym-0.5-8.log
timeout 46800 python3 censusX.py False False 0.5 10 tests/census/20.py | tee census-20-nosym-0.5-10.log
#
timeout 46800 python3 censusX.py False True 0.5 4 tests/census/20.py | tee census-20-sym2-0.5-4.log
timeout 46800 python3 censusX.py False True 0.5 6 tests/census/20.py | tee census-20-sym2-0.5-6.log
timeout 46800 python3 censusX.py False True 0.5 8 tests/census/20.py | tee census-20-sym2-0.5-8.log
timeout 46800 python3 censusX.py False True 0.5 10 tests/census/20.py | tee census-20-sym2-0.5-10.log

#---------#
# 40
#---------#

timeout 46800 python3 censusX.py False False 0.5 4 tests/census/40.py | tee census-40-nosym-0.5-4.log
timeout 46800 python3 censusX.py False False 0.5 6 tests/census/40.py | tee census-40-nosym-0.5-6.log
timeout 46800 python3 censusX.py False False 0.5 8 tests/census/40.py | tee census-40-nosym-0.5-8.log
timeout 46800 python3 censusX.py False False 0.5 10 tests/census/40.py | tee census-40-nosym-0.5-10.log
#
timeout 46800 python3 censusX.py False True 0.5 4 tests/census/40.py | tee census-40-sym2-0.5-4.log
timeout 46800 python3 censusX.py False True 0.5 6 tests/census/40.py | tee census-40-sym2-0.5-6.log
timeout 46800 python3 censusX.py False True 0.5 8 tests/census/40.py | tee census-40-sym2-0.5-8.log
timeout 46800 python3 censusX.py False True 0.5 10 tests/census/40.py | tee census-40-sym2-0.5-10.log

#---------#
# 45
#---------#

timeout 46800 python3 censusX.py False False 0.5 4 tests/census/45.py | tee census-45-nosym-0.5-4.log
timeout 46800 python3 censusX.py False False 0.5 6 tests/census/45.py | tee census-45-nosym-0.5-6.log
timeout 46800 python3 censusX.py False False 0.5 8 tests/census/45.py | tee census-45-nosym-0.5-8.log
timeout 46800 python3 censusX.py False False 0.5 10 tests/census/45.py | tee census-45-nosym-0.5-10.log
#
timeout 46800 python3 censusX.py False True 0.5 4 tests/census/45.py | tee census-45-sym2-0.5-4.log
timeout 46800 python3 censusX.py False True 0.5 6 tests/census/45.py | tee census-45-sym2-0.5-6.log
timeout 46800 python3 censusX.py False True 0.5 8 tests/census/45.py | tee census-45-sym2-0.5-8.log
timeout 46800 python3 censusX.py False True 0.5 10 tests/census/45.py | tee census-45-sym2-0.5-10.log

#=========#
# p=0.25
#=========#

#---------#
# 10
#---------#

timeout 46800 python3 censusX.py False False 0.25 4 tests/census/10.py | tee census-10-nosym-0.25-4.log
timeout 46800 python3 censusX.py False False 0.25 6 tests/census/10.py | tee census-10-nosym-0.25-6.log
timeout 46800 python3 censusX.py False False 0.25 8 tests/census/10.py | tee census-10-nosym-0.25-8.log
timeout 46800 python3 censusX.py False False 0.25 10 tests/census/10.py | tee census-10-nosym-0.25-10.log
#
timeout 46800 python3 censusX.py False True 0.25 4 tests/census/10.py | tee census-10-sym2-0.25-4.log
timeout 46800 python3 censusX.py False True 0.25 6 tests/census/10.py | tee census-10-sym2-0.25-6.log
timeout 46800 python3 censusX.py False True 0.25 8 tests/census/10.py | tee census-10-sym2-0.25-8.log
timeout 46800 python3 censusX.py False True 0.25 10 tests/census/10.py | tee census-10-sym2-0.25-10.log

#---------#
# 12
#---------#

timeout 46800 python3 censusX.py False False 0.25 4 tests/census/12.py | tee census-12-nosym-0.25-4.log
timeout 46800 python3 censusX.py False False 0.25 6 tests/census/12.py | tee census-12-nosym-0.25-6.log
timeout 46800 python3 censusX.py False False 0.25 8 tests/census/12.py | tee census-12-nosym-0.25-8.log
timeout 46800 python3 censusX.py False False 0.25 10 tests/census/12.py | tee census-12-nosym-0.25-10.log
#
timeout 46800 python3 censusX.py False True 0.25 4 tests/census/12.py | tee census-12-sym2-0.25-4.log
timeout 46800 python3 censusX.py False True 0.25 6 tests/census/12.py | tee census-12-sym2-0.25-6.log
timeout 46800 python3 censusX.py False True 0.25 8 tests/census/12.py | tee census-12-sym2-0.25-8.log
timeout 46800 python3 censusX.py False True 0.25 10 tests/census/12.py | tee census-12-sym2-0.25-10.log

#---------#
# 20
#---------#

timeout 46800 python3 censusX.py False False 0.25 4 tests/census/20.py | tee census-20-nosym-0.25-4.log
timeout 46800 python3 censusX.py False False 0.25 6 tests/census/20.py | tee census-20-nosym-0.25-6.log
timeout 46800 python3 censusX.py False False 0.25 8 tests/census/20.py | tee census-20-nosym-0.25-8.log
timeout 46800 python3 censusX.py False False 0.25 10 tests/census/20.py | tee census-20-nosym-0.25-10.log
#
timeout 46800 python3 censusX.py False True 0.25 4 tests/census/20.py | tee census-20-sym2-0.25-4.log
timeout 46800 python3 censusX.py False True 0.25 6 tests/census/20.py | tee census-20-sym2-0.25-6.log
timeout 46800 python3 censusX.py False True 0.25 8 tests/census/20.py | tee census-20-sym2-0.25-8.log
timeout 46800 python3 censusX.py False True 0.25 10 tests/census/20.py | tee census-20-sym2-0.25-10.log

#---------#
# 40
#---------#

timeout 46800 python3 censusX.py False False 0.25 4 tests/census/40.py | tee census-40-nosym-0.25-4.log
timeout 46800 python3 censusX.py False False 0.25 6 tests/census/40.py | tee census-40-nosym-0.25-6.log
timeout 46800 python3 censusX.py False False 0.25 8 tests/census/40.py | tee census-40-nosym-0.25-8.log
timeout 46800 python3 censusX.py False False 0.25 10 tests/census/40.py | tee census-40-nosym-0.25-10.log
#
timeout 46800 python3 censusX.py False True 0.25 4 tests/census/40.py | tee census-40-sym2-0.25-4.log
timeout 46800 python3 censusX.py False True 0.25 6 tests/census/40.py | tee census-40-sym2-0.25-6.log
timeout 46800 python3 censusX.py False True 0.25 8 tests/census/40.py | tee census-40-sym2-0.25-8.log
timeout 46800 python3 censusX.py False True 0.25 10 tests/census/40.py | tee census-40-sym2-0.25-10.log

#---------#
# 45
#---------#

timeout 46800 python3 censusX.py False False 0.25 4 tests/census/45.py | tee census-45-nosym-0.25-4.log
timeout 46800 python3 censusX.py False False 0.25 6 tests/census/45.py | tee census-45-nosym-0.25-6.log
timeout 46800 python3 censusX.py False False 0.25 8 tests/census/45.py | tee census-45-nosym-0.25-8.log
timeout 46800 python3 censusX.py False False 0.25 10 tests/census/45.py | tee census-45-nosym-0.25-10.log
#
timeout 46800 python3 censusX.py False True 0.25 4 tests/census/45.py | tee census-45-sym2-0.25-4.log
timeout 46800 python3 censusX.py False True 0.25 6 tests/census/45.py | tee census-45-sym2-0.25-6.log
timeout 46800 python3 censusX.py False True 0.25 8 tests/census/45.py | tee census-45-sym2-0.25-8.log
timeout 46800 python3 censusX.py False True 0.25 10 tests/census/45.py | tee census-45-sym2-0.25-10.log

#=========#
# p=0.125
#=========#

#---------#
# 10
#---------#

timeout 46800 python3 censusX.py False False 0.125 4 tests/census/10.py | tee census-10-nosym-0.125-4.log
timeout 46800 python3 censusX.py False False 0.125 6 tests/census/10.py | tee census-10-nosym-0.125-6.log
timeout 46800 python3 censusX.py False False 0.125 8 tests/census/10.py | tee census-10-nosym-0.125-8.log
timeout 46800 python3 censusX.py False False 0.125 10 tests/census/10.py | tee census-10-nosym-0.125-10.log
#
timeout 46800 python3 censusX.py False True 0.125 4 tests/census/10.py | tee census-10-sym2-0.125-4.log
timeout 46800 python3 censusX.py False True 0.125 6 tests/census/10.py | tee census-10-sym2-0.125-6.log
timeout 46800 python3 censusX.py False True 0.125 8 tests/census/10.py | tee census-10-sym2-0.125-8.log
timeout 46800 python3 censusX.py False True 0.125 10 tests/census/10.py | tee census-10-sym2-0.125-10.log

#---------#
# 12
#---------#

timeout 46800 python3 censusX.py False False 0.125 4 tests/census/12.py | tee census-12-nosym-0.125-4.log
timeout 46800 python3 censusX.py False False 0.125 6 tests/census/12.py | tee census-12-nosym-0.125-6.log
timeout 46800 python3 censusX.py False False 0.125 8 tests/census/12.py | tee census-12-nosym-0.125-8.log
timeout 46800 python3 censusX.py False False 0.125 10 tests/census/12.py | tee census-12-nosym-0.125-10.log
#
timeout 46800 python3 censusX.py False True 0.125 4 tests/census/12.py | tee census-12-sym2-0.125-4.log
timeout 46800 python3 censusX.py False True 0.125 6 tests/census/12.py | tee census-12-sym2-0.125-6.log
timeout 46800 python3 censusX.py False True 0.125 8 tests/census/12.py | tee census-12-sym2-0.125-8.log
timeout 46800 python3 censusX.py False True 0.125 10 tests/census/12.py | tee census-12-sym2-0.125-10.log

#---------#
# 20
#---------#

timeout 46800 python3 censusX.py False False 0.125 4 tests/census/20.py | tee census-20-nosym-0.125-4.log
timeout 46800 python3 censusX.py False False 0.125 6 tests/census/20.py | tee census-20-nosym-0.125-6.log
timeout 46800 python3 censusX.py False False 0.125 8 tests/census/20.py | tee census-20-nosym-0.125-8.log
timeout 46800 python3 censusX.py False False 0.125 10 tests/census/20.py | tee census-20-nosym-0.125-10.log
#
timeout 46800 python3 censusX.py False True 0.125 4 tests/census/20.py | tee census-20-sym2-0.125-4.log
timeout 46800 python3 censusX.py False True 0.125 6 tests/census/20.py | tee census-20-sym2-0.125-6.log
timeout 46800 python3 censusX.py False True 0.125 8 tests/census/20.py | tee census-20-sym2-0.125-8.log
timeout 46800 python3 censusX.py False True 0.125 10 tests/census/20.py | tee census-20-sym2-0.125-10.log

#---------#
# 40
#---------#

timeout 46800 python3 censusX.py False False 0.125 4 tests/census/40.py | tee census-40-nosym-0.125-4.log
timeout 46800 python3 censusX.py False False 0.125 6 tests/census/40.py | tee census-40-nosym-0.125-6.log
timeout 46800 python3 censusX.py False False 0.125 8 tests/census/40.py | tee census-40-nosym-0.125-8.log
timeout 46800 python3 censusX.py False False 0.125 10 tests/census/40.py | tee census-40-nosym-0.125-10.log
#
timeout 46800 python3 censusX.py False True 0.125 4 tests/census/40.py | tee census-40-sym2-0.125-4.log
timeout 46800 python3 censusX.py False True 0.125 6 tests/census/40.py | tee census-40-sym2-0.125-6.log
timeout 46800 python3 censusX.py False True 0.125 8 tests/census/40.py | tee census-40-sym2-0.125-8.log
timeout 46800 python3 censusX.py False True 0.125 10 tests/census/40.py | tee census-40-sym2-0.125-10.log

#---------#
# 45
#---------#

timeout 46800 python3 censusX.py False False 0.125 4 tests/census/45.py | tee census-45-nosym-0.125-4.log
timeout 46800 python3 censusX.py False False 0.125 6 tests/census/45.py | tee census-45-nosym-0.125-6.log
timeout 46800 python3 censusX.py False False 0.125 8 tests/census/45.py | tee census-45-nosym-0.125-8.log
timeout 46800 python3 censusX.py False False 0.125 10 tests/census/45.py | tee census-45-nosym-0.125-10.log
#
timeout 46800 python3 censusX.py False True 0.125 4 tests/census/45.py | tee census-45-sym2-0.125-4.log
timeout 46800 python3 censusX.py False True 0.125 6 tests/census/45.py | tee census-45-sym2-0.125-6.log
timeout 46800 python3 censusX.py False True 0.125 8 tests/census/45.py | tee census-45-sym2-0.125-8.log
timeout 46800 python3 censusX.py False True 0.125 10 tests/census/45.py | tee census-45-sym2-0.125-10.log
