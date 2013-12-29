#!/usr/bin/python

import sys

def main ():
  """
  
  """
  fSum = 0
  for i in range(1,1000+1):
    fSum += i**i % 10**10
    fSum %= 10**10
    print i,fSum

  print 'final:',fSum
  
  pass

if __name__ == '__main__':
  main()
