#!/usr/bin/python

import sys

def main ():
  """
  
  """
  pent = set( n * (3*n - 1) / 2 for n in range(2,10**4) )
 
  for pj in pent: 
    for pk in pent:
      if pj - pk in pent and pj + pk in pent: 
        print "Answer is",pj - pk
  pass	

if __name__ == '__main__':
  main()
