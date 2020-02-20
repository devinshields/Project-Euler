#!/usr/bin/python -tt
import sys
sys.path.append('../primes')

from Euler import is_pandigital 
 
def main():

  maxNum = 2000

  for i in range(maxNum):
    for j in range(i,maxNum):
      if is_pandigital(''.join([str(i),str(j),str(i*j)])):
        print i,j,i*j

if __name__ == '__main__':
  main()

