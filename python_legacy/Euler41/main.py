#!/usr/bin/python
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
from itertools import permutations
from math import sqrt

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(sqrt(n))
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def main ():

  bigPrime = 0
  s= '123456789'
  for r in range(1,11):
    for i in permutations(s[:r]):
      num = int(''.join(i))
      if num > bigPrime and is_prime(num):
        bigPrime = num

  print 'And the answer is:',bigPrime
  pass
  
if __name__ == '__main__':
  main()
