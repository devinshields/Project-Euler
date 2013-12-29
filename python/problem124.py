#!/usr/bin/python -tt
'''
  problem 124: http://projecteuler.net/problem=124
'''

import euler
import operator


def rad(x):
  return reduce(operator.mul, map(operator.itemgetter(0), euler.factor(x)))
assert rad(504) == 42

n_max = 100000
rad_list = sorted([(1,1)] + [(n, rad(n)) for n in range(2, n_max+1)], key = lambda t: t[::-1])

def E(i):
  return rad_list[i-1][0]

print 'Answer: {0}'.format(E(10000))