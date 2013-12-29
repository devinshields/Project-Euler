#!/usr/bin/python -tt
'''
  problem 120: http://projecteuler.net/problem=120
'''


def sr(a, n):
  return ((a-1)**n + (a+1)**n) % a**2
assert sr(7, 3) == 42


def get_r_maxs():
  ''' for 3 <= a <= 1000, find sum r_max '''
  for a in range(3,1000+1):
    r_max = max([sr(a, n) for n in range(1, 10000)])
    yield r_max


print sum(get_r_maxs())