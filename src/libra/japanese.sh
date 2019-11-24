#!/usr/bin/env bash

###########
# experiment 4: different analysis configurations
###########

timeout 46800 python3 japaneseX.py False False 0.5 4 tests/japanese/20.py | tee japanese-20-nosym-0.5-4.log
timeout 46800 python3 japaneseX.py False False 0.5 6 tests/japanese/20.py | tee japanese-20-nosym-0.5-6.log
timeout 46800 python3 japaneseX.py False False 0.5 8 tests/japanese/20.py | tee japanese-20-nosym-0.5-8.log
timeout 46800 python3 japaneseX.py False False 0.5 10 tests/japanese/20.py | tee japanese-20-nosym-0.5-10.log
#
timeout 46800 python3 japaneseX.py False True 0.5 4 tests/japanese/20.py | tee japanese-20-sym2-0.5-4.log
timeout 46800 python3 japaneseX.py False True 0.5 6 tests/japanese/20.py | tee japanese-20-sym2-0.5-6.log
timeout 46800 python3 japaneseX.py False True 0.5 8 tests/japanese/20.py | tee japanese-20-sym2-0.5-8.log
timeout 46800 python3 japaneseX.py False True 0.5 10 tests/japanese/20.py | tee japanese-20-sym2-0.5-10.log

timeout 46800 python3 japaneseX.py False False 0.25 4 tests/japanese/20.py | tee japanese-20-nosym-0.25-4.log
timeout 46800 python3 japaneseX.py False False 0.25 6 tests/japanese/20.py | tee japanese-20-nosym-0.25-6.log
timeout 46800 python3 japaneseX.py False False 0.25 8 tests/japanese/20.py | tee japanese-20-nosym-0.25-8.log
timeout 46800 python3 japaneseX.py False False 0.25 10 tests/japanese/20.py | tee japanese-20-nosym-0.25-10.log
#
timeout 46800 python3 japaneseX.py False True 0.25 4 tests/japanese/20.py | tee japanese-20-sym2-0.25-4.log
timeout 46800 python3 japaneseX.py False True 0.25 6 tests/japanese/20.py | tee japanese-20-sym2-0.25-6.log
timeout 46800 python3 japaneseX.py False True 0.25 8 tests/japanese/20.py | tee japanese-20-sym2-0.25-8.log
timeout 46800 python3 japaneseX.py False True 0.25 10 tests/japanese/20.py | tee japanese-20-sym2-0.25-10.log

timeout 46800 python3 japaneseX.py False False 0.125 4 tests/japanese/20.py | tee japanese-20-nosym-0.125-4.log
timeout 46800 python3 japaneseX.py False False 0.125 6 tests/japanese/20.py | tee japanese-20-nosym-0.125-6.log
timeout 46800 python3 japaneseX.py False False 0.125 8 tests/japanese/20.py | tee japanese-20-nosym-0.125-8.log
timeout 46800 python3 japaneseX.py False False 0.125 10 tests/japanese/20.py | tee japanese-20-nosym-0.125-10.log
#
timeout 46800 python3 japaneseX.py False True 0.125 4 tests/japanese/20.py | tee japanese-20-sym2-0.125-4.log
timeout 46800 python3 japaneseX.py False True 0.125 6 tests/japanese/20.py | tee japanese-20-sym2-0.125-6.log
timeout 46800 python3 japaneseX.py False True 0.125 8 tests/japanese/20.py | tee japanese-20-sym2-0.125-8.log
timeout 46800 python3 japaneseX.py False True 0.125 10 tests/japanese/20.py | tee japanese-20-sym2-0.125-10.log

timeout 46800 python3 japaneseX.py False False 0 4 tests/japanese/20.py | tee japanese-20-nosym-0-4.log
timeout 46800 python3 japaneseX.py False False 0 6 tests/japanese/20.py | tee japanese-20-nosym-0-6.log
timeout 46800 python3 japaneseX.py False False 0 8 tests/japanese/20.py | tee japanese-20-nosym-0-8.log
timeout 46800 python3 japaneseX.py False False 0 10 tests/japanese/20.py | tee japanese-20-nosym-0-10.log
#
timeout 46800 python3 japaneseX.py False True 0 4 tests/japanese/20.py | tee japanese-20-sym2-0-4.log
timeout 46800 python3 japaneseX.py False True 0 6 tests/japanese/20.py | tee japanese-20-sym2-0-6.log
timeout 46800 python3 japaneseX.py False True 0 8 tests/japanese/20.py | tee japanese-20-sym2-0-8.log
timeout 46800 python3 japaneseX.py False True 0 10 tests/japanese/20.py | tee japanese-20-sym2-0-10.log
