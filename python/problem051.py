#!/usr/bin/python -tt
#
# problem 51: http://projecteuler.net/problem=51
#

from Euler import is_prime
from sundaram import sundaram
from itertools import groupby,combinations
import sys

def main():
  
  p = filter(lambda prime: prime > 10000, sundaram(10**6))
  primes = set(p)

  for prime in p:
    s = str(prime)
    for num_replace_digits in range(1,len(s)):
      for replace_combo in list(combinations(range(len(s)), num_replace_digits)):
        rep_str = ''.join([s[i] if i not in replace_combo else '{0}' for i,c in enumerate(s)])
        cand_ints = [int(rep_str.format(i)) for i in range(0,10)]
        prime_ints = filter(lambda x: x in primes, cand_ints)

        if len(prime_ints) >= 8 and prime in prime_ints:
          print '\nAnswer: {0}'.format(s)
          sys.exit(0)
  pass

if __name__ == '__main__':
  main()
