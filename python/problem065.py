#!/usr/bin/python
'''
problem 65: http://projecteuler.net/problem=65
'''

import itertools
from fractions import Fraction as frk

def evens_gen(i=0):
  while True:
    i += 1
    yield 2*i

def e_seq(n):
  evens = evens_gen()
  seq   = [1 if (k)%3-1 else evens.next() for k in range(n-1)]
  return 2 + 1/reduce(lambda i, j: j + frk(1, i), seq[::-1])

print 'Answer: {0}'.format(sum(map(int, str(e_seq(100).numerator))))