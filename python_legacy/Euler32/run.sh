#!/bin/bash

./main.py | awk '{print $3}' | sort | uniq | awk '{x+=$1};END{print x}'
