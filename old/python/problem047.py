#!/usr/bin/python -tt
#
# problem 47: http://projecteuler.net/problem=47
#

import sys

def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n
 
def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p,e))
    F.sort()
    return F

def dist_factors(i):
  return len(map(lambda x: x[0], factor(i)))

def main():
  i = 10
  factor_nums = []
  while 1:
    i += 1
    tup = (i,dist_factors(i))
    if tup[1] == 4:
      factor_nums.append(i)
      if len(factor_nums) == 4:
        print '\nAnswer:',factor_nums[0]
        sys.exit(0)
    else:
      factor_nums = []
  pass

if __name__ == '__main__':
  main()