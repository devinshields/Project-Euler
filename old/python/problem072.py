#!/usr/bin/python

from Euler import factor
from operator import mul

def eulers_totient(n):
  p_list = [t[0] for t in factor(n)]
  return int(round(n / reduce(mul, map(lambda p:1-p**-1, p_list))**-1))

d = 10**6
print sum([eulers_totient(i) for i in range(2, d+1)])
