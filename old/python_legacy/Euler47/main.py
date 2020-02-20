#!/usr/bin/python

from Euler import is_prime
from itertools import izip, tee

def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = tee(iterable)
  next(b, None)
  return izip(a, b)

def pFact(num):
  pfactors = []
  while True:
    j = 2
    while j < num+1:
      if num%j==0 and is_prime(j):
        num = num/j
        pfactors.append(j)
        break
      j+=1
    if num==1:
      break
  return pfactors

def main ():
  """
  
  """
  numToDistFacts = {}
  for i in range(1,10**5):
    primeSet = sorted(list(set(pFact(i))))
    l = len(primeSet)
    if l == 4:
      #print i,l
      print i
  
  pass

if __name__ == '__main__':
  main()
