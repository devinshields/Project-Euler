#!/usr/bin/python -tt
'''
    problem 113: http://projecteuler.net/problem=113
'''


#googol = 10**100
#print len(str(googol))


# should be solvable with some form of dynamic programming.
# given a base 10 number X with digits (b,c,d,...) and 
# knowing the decending non-bouncy numbers, if a >= b,
# allowing abcd... will give (10-a) * non_bouncy(X).
#
#
#
#


# As n increases, the proportion of bouncy numbers below n increases
# such that there are only 12951 numbers below one-million that are not bouncy
# and only 277032 non-bouncy numbers below 10^10.


# cheating: http://math.stackexchange.com/questions/10839/combinatorial-counting


import math


def nCr(n,r):
  return math.factorial(n) / math.factorial(r) / math.factorial(n-r)


num_digits_in_max_number = 99
digits_in_base           = 9


decreasing = sum(nCr(digits_in_base   + k, digits_in_base  ) for k in range(1, num_digits_in_max_number+1))
increasing = sum(nCr(digits_in_base-1 + k, digits_in_base-1) for k in range(1, num_digits_in_max_number+1)) # there's less choice with increasing numbers, while incrementing the choice can't be 0.

total = increasing + decreasing






print total

print (nCr(109, 100) - 1) + (nCr(110, 100) - 101) - (9 * 100)

