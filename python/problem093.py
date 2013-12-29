#!/usr/bin/python
'''

'''

import operator
import itertools


def length_of_longest_consecutive_sequence(lst, start=1):
  grp = set(lst)
  for i in itertools.count(1):
    if i not in grp:
      return i-1


# get the operator functions
possible_ops = [operator.add, operator.sub, operator.mul, operator.div]

# get all ordered digit sequences (a, b, c, d)
possible_seq = [(a,b,c,d) for d in range(4, 10) for c in range(3, d) for b in range(2, c) for a in range(1, b)]


# for each sequence, map it through all possible operation trees and find 