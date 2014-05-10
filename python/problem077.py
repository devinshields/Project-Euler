#!/usr/bin/env python
'''   
  http://projecteuler.net/problem=77
'''

import itertools
import euler


def count(S, m, n):
  ''' source: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
  
      S - ascending list of globally available integer components (coins)
      m - index into S[]. S[:m] is the set of allowed components for this run
      n - target value for this run

      math trick:
          count(S, m, n) == count(S, m-1, n) + count(S, m, n - S[m-1])
  '''
  # base case, found exact change
  if n == 0:
    return 1
  
  # base case, overshot the target value / combo isn't feasable
  if n < 0:
    return 0

  # base case, no smaller coins available
  if m <= 0:
      return 0
  
  # recurse!
  return count(S, m-1, n) + count(S, m, n - S[m-1])


def count_prime_summations(target_value):
  ''' sieve for 'coin' values below the target
      and pass to the combo counter '''
  S = euler.prime_sieve(target_value+1)
  return count(S, len(S), target_value)


# test
assert count_prime_summations(10) == 5


for target_value in itertools.count(10):
  if count_prime_summations(target_value) > 5000:
    print 'answer: {0}'.format(target_value)
    break


