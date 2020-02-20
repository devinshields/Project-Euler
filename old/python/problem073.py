#!/usr/bin/python

from fractions import Fraction
from math import floor, ceil
from Euler import gcd

def mainly_slow ():
  
  frac_set = set()
  
  #for d in range(2, 100+1):
  for d in range(2, 12*10**3+1):
    if not d%100:
      print d
    
    # for this d, get the ints that bound 1/3 & 2/3
    n_min = int(ceil(d/3.))
    n_max = int(floor(d/2.))

    for n in range(n_min, n_max+1):
      f = Fraction(n,d)
      frac_set.add(f)


  print '\nAnswer:', len(frac_set)-2

  pass

total = 0
for d in range(3, 12*10**3+1):
  for n in range(int(ceil(d/3.)), int(floor(d/2.))):
    if gcd(n,d) == 1:
      total += 1
print total