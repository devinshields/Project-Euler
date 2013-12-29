#!/usr/bin/python -tt
import sys
from itertools import permutations
from Euler import is_prime

def rotate(num):
  s = str(num)
  l = len(s)
  return [int(s[0-phase:] + s[:l-phase]) for phase in range(1,l)]

def main():

  # get primes in the first 10^6,
  primes  = [i for i in range(1,1000000) if is_prime(i) and '0' not in str(i)]
  cPrimes = []

  # loop through the primes
  for j,p in enumerate(primes):
    #print j
    if p in cPrimes:continue
    
    rotated = rotate(p)
    rotated.append(p)
    
    #print rotated
    
    # test if it's a cPrime
    if reduce(lambda x, y: x and is_prime(y), rotated,True):
      for i in rotated:
        cPrimes.append(i)
    
  #print cPrimes
  print sorted(list(set(cPrimes)))
  print 'Circ Primes:',len(list(set(cPrimes)))
  
if __name__ == '__main__':
  main()

