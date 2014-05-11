#!/usr/bin/env python
'''
  http://projecteuler.net/problem=93

    1) make a PostfixCalculator
    2) 

'''

import collections
import itertools
from operator import add, sub, mul, div

from postfixcalculator import PostfixCalculator, test_calculator


RunSizeAndDigits = collections.namedtuple('RunSizeAndDigits', ['run_size', 'digits'])


def longest_run_of_ints_from_1_to_n(found_ints):
  found_ints = sorted(set(found_ints))
  for ind, found_int in enumerate(found_ints):
    if (ind + 1) == found_int:
      continue
    else:
      return ind
  return len(found_ints)
    


# full starting symbol vocab - all operators, all digits
full_digits = tuple(range(1, 9+1))
operators   = (add, sub, mul, div)

longest_and_digit_combo = []

# sample digit combos
for digits_combo in itertools.combinations(full_digits, 4):
  #
  valid_trees = []

  digits_combo_word = ''.join(map(str, digits_combo))
  
  # loop over operator subsets
  for sub_ops in itertools.combinations_with_replacement(operators, 3):
    # loop over symbol permutations
    symbols = digits_combo[:] + sub_ops[:]
    for symbol_perm in itertools.permutations(symbols):
      try:
        calc = PostfixCalculator().read_symbols_and_run_calculator(symbol_stream=symbol_perm)
        valid_trees.append(calc)
      except:
        pass

  # stats for this digits_combo
  found_ints = sorted(set(c.calc_results for c in valid_trees if c.calc_results > 0))
  longest_run = longest_run_of_ints_from_1_to_n(found_ints)
  
  res = RunSizeAndDigits(longest_run, digits_combo_word)
  longest_and_digit_combo.append(res)


answer = sorted(longest_and_digit_combo)[-1].digits

print '\nanswer: {0}\n'.format(answer)

