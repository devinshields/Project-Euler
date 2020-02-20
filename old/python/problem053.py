#!/usr/bin/python -tt
#
# problem 53: http://projecteuler.net/problem=53
#

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

count = 0
for n in range(2, 100+1):
  for r in range(2, n+1):
    val = nCr(n,r)
    if val > 10**6:
      count += 1
print '\nAnswer:', count