#!/usr/bin/python

from Euler import prime_sieve, is_perm, factor
from itertools import combinations
from operator import mul

def uniq_f(n):
  return [t[0] for t in factor(n)]

def main ():

  cases = filter(lambda i: i < 10**7, map(lambda t: t[0]*t[1], combinations(prime_sieve(int(1.5*(10**7)**.5)),2)))
  print ''
  tot_tups = []
  for n in cases:
    f = uniq_f(n)
    tot_ratio =  reduce(mul, map(lambda p:1-p**-1, f))**-1
    tot = int(round(n / tot_ratio))
    
    if is_perm(n, tot):
      tot_tups.append((tot_ratio, n, tot))
  
  for tup in sorted(tot_tups)[:10]:
    print tup
  
  pass

if __name__ == '__main__':
  main()
