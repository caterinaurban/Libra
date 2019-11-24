#!/usr/bin/env bash

python3 playgroundX.py False False 0 2 | tee playground-nosym-0-2.log
python3 playgroundX.py False False 0 3 | tee playground-nosym-0-3.log
python3 playgroundX.py False False 0 4 | tee playground-nosym-0-4.log

python3 playgroundX.py True False 0 2 | tee playground-sym1-0-2.log
python3 playgroundX.py True False 0 3 | tee playground-sym1-0-3.log
python3 playgroundX.py True False 0 4 | tee playground-sym1-0-4.log

python3 playgroundX.py False True 0 2 | tee playground-sym2-0-2.log
python3 playgroundX.py False True 0 3 | tee playground-sym2-0-3.log
python3 playgroundX.py False True 0 4 | tee playground-sym2-0-4.log
