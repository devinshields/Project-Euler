#!/usr/bin/python
from itertools import permutations
from Euler import is_prime
from itertools import izip, tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def main ():
  """
  
  """
  
  #
  primes  = [i for i in range(10**3,10**4) if is_prime(i) and '0' not in str(i)]
  #print primes
  
  for p in primes:
    perms = sorted(list(set([int(''.join(perm)) for perm in permutations(str(p)) if is_prime(int(''.join(perm)))])))
    if len(perms) < 3:continue

    diffDiff = [b-a for a,b in pairwise([y-x for x,y in pairwise(perms)])]
    if 0 in diffDiff:

      print p,perms
      print p,diffDiff
      print 

  
  
  
  pass

if __name__ == '__main__':
  main()
