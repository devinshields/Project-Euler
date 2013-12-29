#!/usr/bin/python -tt
import sys
sys.path.append('/Users/admin/Desktop/python-work/Project_Euler/primes')
from Euler import is_prime 

def left_prime(n):
  if len(str(n)) ==1:return is_prime(n)
  return is_prime(n) and left_prime(int(str(n)[:-1]))

def right_prime(n):
  if len(str(n)) ==1:return is_prime(n)
  return is_prime(n) and right_prime(int(str(n)[1:]))

def main():
  (i,t)=(10,[])
  while len(t) < 11:
    if left_prime(i) and right_prime(i):
      t.append(i)
      print len(t),'\n',t
    i += 1
  print 'Euler #34:',sum(t)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

