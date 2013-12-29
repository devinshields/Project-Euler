#!/usr/bin/python
'''   http://projecteuler.net/problem=116
'''

import math
import collections


M = 50

Combo = collections.namedtuple('Combo', ['large_red', 'small_red', 'black'])


# generate all possible combos
combos_00 = sorted(Combo(large, small, M-large-small) for large in range(M+1) for small in range(large+1) if (M-large-small) >= 0)


# check for a separating black square when there are 2 reds
combos_01 = filter(lambda c: c.small_red == 0 or c.black > 0, combos_00)


# check that no red is length 1 or 2
combos_02 = filter(lambda c: not (c.small_red in (1, 2) or c.large_red in (1,2)), combos_01)



for c in combos_02:
  print c




