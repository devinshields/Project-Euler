#!/usr/bin/python
'''   http://projecteuler.net/problem=116
'''

import math
import collections
import operator


M = 50


Combo = collections.namedtuple('Combo', ['black', 'red', 'green', 'blue'])


# build out all possible block configurations
combos = []
for blue in range(M/4 + 1):
  for red in range(M/2 + 1):
    for green in range(M/3 + 1):
      black = M - 2*red - 3*green - 4*blue
      if black >= 0:
        combos.append(Combo(black, red, green, blue))
combos = sorted(combos)


# check that they're valid
for c in combos:
   assert M == sum(map(lambda t: t[0]*t[1], zip(c, (1,2,3,4))))


#
total = 0
for c in combos:
  total += math.factorial(sum(c)) / reduce(operator.mul, map(math.factorial, c), 1)
  
print total
