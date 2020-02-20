#!/usr/bin/env python
'''
  get integer partition counts with the recurrence relationship:
      http://en.wikipedia.org/wiki/Partition_%28number_theory%29#Generating_function
      
  get required pentagonal numbers with:
      http://en.wikipedia.org/wiki/Pentagonal_number
      pentagonal_number(n) := (3 * n**2 - n )/2
'''


import collections
import itertools
import sys


sys.setrecursionlimit(10**4)

 
def memoize(f):
  ''' a simple memoize lookup tool '''
  cache = {}
  def memf(*x):
    if x not in cache:
      cache[x] = f(*x)
    return cache[x]
  return memf


IsPositiveKOffSet = collections.namedtuple('IsPositiveKOffSet', ['is_positive', 'k_offset'])


def get_generalized_pentagonal_number_tups():
  ''' http://en.wikipedia.org/wiki/Pentagonal_number '''
  
  is_pos_pattern = (True, True, False, False)
  is_pos_gen = itertools.cycle(is_pos_pattern)

  def get_indexes():
    for i in itertools.count(1):
      yield i
      yield -i
  
  for sequence_index in get_indexes():
    is_pos = is_pos_gen.next()
    k_offset = sequence_index*(3*sequence_index-1)/2
    ret_val = IsPositiveKOffSet(is_pos, k_offset)
    yield ret_val 


# test
assert tuple(itertools.islice(get_generalized_pentagonal_number_tups(), 5)) == ((True, 1),
                                                                                (True, 2),
                                                                                (False, 5),
                                                                                (False, 7),
                                                                                (True, 12))


@memoize
def p(k):
  ''' integer partition count function, recursive implementation '''
  # base case
  if k < 0:
    return 0
  # base case
  if k == 0:
    return 1
  # recursion case, k > 0
  #   fetch pentagonal number tups until (k - pent) < 0
  #   then, aggregate counts from each subtask
  p_total = 0
  for tup in get_generalized_pentagonal_number_tups():
    #print 'k: {0},  k_offset: {1}, (k-tup.k_offset): {2}'.format(k, tup.k_offset, k-tup.k_offset)
    if (k - tup.k_offset) < 0:
      break
    p_update = (tup.is_positive and 1 or -1) * p(k - tup.k_offset)
    p_total += p_update
  return p_total


# test 
assert p(5)  == 7
assert p(6)  == 11
assert p(7)  == 15
assert p(8)  == 22
assert p(9)  == 30
assert p(10) == 42


# sequential search over the integers for:
#   'least value of n for which p(n) is divisible by one million'.
mod_val = 10**6
for n in itertools.count(5):
  if not p(n) % mod_val:
    print '\nanswer: {0}\n'.format(n)
    sys.exit()

