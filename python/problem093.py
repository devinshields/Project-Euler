#!/usr/bin/env python
'''
  http://projecteuler.net/problem=93

    1) make a Postfix calculator
    2) 

'''


import itertools
from operator import add, sub, mul, div
from postfixcalculator import PostfixCalculator, test_calculator


# generate all parse trees
digits    = tuple(range(1, 4+1))
operators = (add, sub, mul, div)
valid_trees = []

# loop over operator subsets
for sub_ops in itertools.combinations(operators, 3):
  # loop over symbol permutations
  symbols = digits[:] + sub_ops[:]
  for symbol_perm in itertools.permutations(symbols):
    print symbol_perm
    try:
      calc = PostfixCalculator().read_symbols_and_run_calculator(symbol_stream=symbol_perm)
      valid_trees.append(calc)
    except:
      pass

found_ints = sorted(set(c.calc_results for c in valid_trees if c.calc_results > 0))

print
print 'len(valid_trees): {0}'.format(len(valid_trees))
print
print found_ints
print


