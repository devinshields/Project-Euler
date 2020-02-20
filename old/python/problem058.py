#!/usr/bin/python

import sys
from Euler import is_prime

def get_square_edges(side_num):
  if side_num == 1:
    return [1]
  n = (2*side_num - 1)
  return [n**2, n**2 - (n-1), n**2 - 2*(n-1), n**2 - 3*(n-1)]

def main ():
  side_num = 0
  prime_count = 0
  total_count = 0

  while 1:
    side_num += 1
    edges = get_square_edges(side_num)
    prime_count += sum(map(is_prime, edges))
    total_count += len(edges)
    prime_ratio = prime_count * 1. / total_count

    if prime_ratio < .1 and side_num > 1:
      print '\nAnswer:', side_num*2-1
      sys.exit(0)

  pass

if __name__ == '__main__':
  main()
