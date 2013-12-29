#!/usr/bin/python

from fractions import Fraction
from math import floor

frac_set = set()
for d in range(2,10**6+1):
  n = floor(3./7.*d)
  f = Fraction(int(n),d)
  if float(f) < float(Fraction(3,7)):
    frac_set.add(f)
print '\nAnswer:',sorted(frac_set)[-1]
