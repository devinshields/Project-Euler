#!/usr/bin/python

from Euler import is_prime

def main ():
  """
  
  """

  maxN = 10**6+1
  maxConsecTerms = 0
  maxPrime = 0

  # make a list of primes
  primes = [i for i in range(2,maxN) if is_prime(i)]

  

  for j,p in enumerate(primes):
    print j/780.

    # make a list of the candidate primes
    cand = [c for c in primes[:j]]
  
    # starting at each prime in the candidate list...
    consecTerms=0
    for ind,c in enumerate(cand):
      candSum = 0
      i = ind
      while candSum < p and i < len(cand):
        candSum += cand[i]
        i       += 1
      # aggregate terms until they equal or exceed the target prime
      #print p,c,candSum
      
      consecTerms = i-ind

      if p == candSum:
        if consecTerms > maxConsecTerms:
          maxPrime = p
          maxConsecTerms = consecTerms
          
          #print p,i-ind #,sum(cand[ind:i]),cand[ind:i]
        break
      continue
    print '****',maxPrime,maxConsecTerms
  print 'And the answer is:',maxPrime,'with a total of',maxConsecTerms,'consecutive terms.'
  pass

if __name__ == '__main__':
  main()
