#!/usr/bin/env bash
gtimeout 3600 python3 incomeX.py False False 0.5 2 | tee income-nosym-0.5-2.log
gtimeout 3600 python3 incomeX.py False False 0.5 4 | tee income-nosym-0.5-4.log
gtimeout 3600 python3 incomeX.py False False 0.5 6 | tee income-nosym-0.5-6.log
gtimeout 3600 python3 incomeX.py False False 0.5 8 | tee income-nosym-0.5-8.log

gtimeout 3600 python3 incomeX.py True False 0.5 2 | tee income-sym1-0.5-2.log
gtimeout 3600 python3 incomeX.py True False 0.5 4 | tee income-sym1-0.5-4.log
gtimeout 3600 python3 incomeX.py True False 0.5 6 | tee income-sym1-0.5-6.log
gtimeout 3600 python3 incomeX.py True False 0.5 8 | tee income-sym1-0.5-8.log

gtimeout 3600 python3 incomeX.py False True 0.5 2 | tee income-sym2-0.5-2.log
gtimeout 3600 python3 incomeX.py False True 0.5 4 | tee income-sym2-0.5-4.log
gtimeout 3600 python3 incomeX.py False True 0.5 6 | tee income-sym2-0.5-6.log
gtimeout 3600 python3 incomeX.py False True 0.5 8 | tee income-sym2-0.5-8.log


gtimeout 3600 python3 incomeX.py False False 0.25 2 | tee income-nosym-0.25-2.log
gtimeout 3600 python3 incomeX.py False False 0.25 4 | tee income-nosym-0.25-4.log
gtimeout 3600 python3 incomeX.py False False 0.25 6 | tee income-nosym-0.25-6.log
gtimeout 3600 python3 incomeX.py False False 0.25 8 | tee income-nosym-0.25-8.log

gtimeout 3600 python3 incomeX.py True False 0.25 2 | tee income-sym1-0.25-2.log
gtimeout 3600 python3 incomeX.py True False 0.25 4 | tee income-sym1-0.25-4.log
gtimeout 3600 python3 incomeX.py True False 0.25 6 | tee income-sym1-0.25-6.log
gtimeout 3600 python3 incomeX.py True False 0.25 8 | tee income-sym1-0.25-8.log

gtimeout 3600 python3 incomeX.py False True 0.25 2 | tee income-sym2-0.25-2.log
gtimeout 3600 python3 incomeX.py False True 0.25 4 | tee income-sym2-0.25-4.log
gtimeout 3600 python3 incomeX.py False True 0.25 6 | tee income-sym2-0.25-6.log
gtimeout 3600 python3 incomeX.py False True 0.25 8 | tee income-sym2-0.25-8.log


gtimeout 3600 python3 incomeX.py False False 0.125 2 | tee income-nosym-0.125-2.log
gtimeout 3600 python3 incomeX.py False False 0.125 4 | tee income-nosym-0.125-4.log
gtimeout 3600 python3 incomeX.py False False 0.125 6 | tee income-nosym-0.125-6.log
gtimeout 3600 python3 incomeX.py False False 0.125 8 | tee income-nosym-0.125-8.log

gtimeout 3600 python3 incomeX.py True False 0.125 2 | tee income-sym1-0.125-2.log
gtimeout 3600 python3 incomeX.py True False 0.125 4 | tee income-sym1-0.125-4.log
gtimeout 3600 python3 incomeX.py True False 0.125 6 | tee income-sym1-0.125-6.log
gtimeout 3600 python3 incomeX.py True False 0.125 8 | tee income-sym1-0.125-8.log

gtimeout 3600 python3 incomeX.py False True 0.125 2 | tee income-sym2-0.125-2.log
gtimeout 3600 python3 incomeX.py False True 0.125 4 | tee income-sym2-0.125-4.log
gtimeout 3600 python3 incomeX.py False True 0.125 6 | tee income-sym2-0.125-6.log
gtimeout 3600 python3 incomeX.py False True 0.125 8 | tee income-sym2-0.125-8.log
