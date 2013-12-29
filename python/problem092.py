#!/usr/bin/python

import sys
sys.setrecursionlimit(10**6)

def sum_dig_sqr(n):
  sm = 0
  while n:
    sm += (n%10)**2
    n /= 10
  return sm

def is_89_loop(n):
  #print n
  if n == 89:
    return True
  if n == 1:
    return False
  return is_89_loop(sum_dig_sqr(n))


def main ():
  
  max_n = 10*10**5
  print sum([is_89_loop(n) for n in range(1, max_n)])
  pass

if __name__ == '__main__':
  main()
