#!/bin/bash

./printWords.py | tee  allWords.txt | tr -d $'\n' | wc
