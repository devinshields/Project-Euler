#!/usr/bin/python
'''   http://projecteuler.net/problem=116
'''

import math
import collections


M = 50


Combo = collections.namedtuple('Combo', ['block_size', 'block_count', 'black_count', 'total_count'])


combos = sorted(Combo(block_size, block_count, M - block_size*block_count, block_size*block_count + (M-block_size*block_count)) for block_size in (2,3,4) for block_count in range(1, M/block_size + 1))


# check that all possible block combos add up
for c in combos:
  assert c.total_count == M
  #print c


# map combos to their permutation count
combo_count = 0
for c in combos:
  combo_count += math.factorial(c.block_count + c.black_count) / math.factorial(c.block_count) / math.factorial(c.black_count)

print combo_count
