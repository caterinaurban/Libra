#!/usr/bin/env bash
###########
# experiment 5: scalability
###########

#===#
# F
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20F.py | tee census-20F-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80F.py | tee census-80F-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320F.py | tee census-320F-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280F.py | tee census-1280F-deep128.log

#===#
# E
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20E.py | tee census-20E-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80E.py | tee census-80E-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320E.py | tee census-320E-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280E.py | tee census-1280E-deep128.log

#===#
# D
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20D.py | tee census-20D-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80D.py | tee census-80D-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320D.py | tee census-320D-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280D.py | tee census-1280D-deep128.log

#===#
# C
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20C.py | tee census-20C-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80C.py | tee census-80C-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320C.py | tee census-320C-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280C.py | tee census-1280C-deep128.log

#===#
# B
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20B.py | tee census-20B-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80B.py | tee census-80B-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320B.py | tee census-320B-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280B.py | tee census-1280B-deep128.log

#===#
# A
#===#

timeout 46800 python3 censusX.py False False 0.25 2 False tests/census/20A.py | tee census-20A-deep2.log

timeout 46800 python3 censusX.py False False 0.25 8 False tests/census/80A.py | tee census-80A-deep8.log

timeout 46800 python3 censusX.py False False 0.25 32 False tests/census/320A.py | tee census-320A-deep32.log

timeout 46800 python3 censusX.py False False 0.25 128 False tests/census/1280A.py | tee census-1280A-deep128.log
