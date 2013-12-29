#!/usr/bin/python
#
#   math here: http://en.wikipedia.org/wiki/Partition_function_(number_theory)#Partition_function
#

import sys
sys.setrecursionlimit(10**6)

class PartitionCounter(object):
  def __init__(self):
    '''cache will hold all previously evaluated "Intermediate function" values'''
    self.cache = {}
  def p(self, k, n):
    '''recursive definition of the partition function with memoization'''
    if (k, n) in self.cache:
      return self.cache[(k, n)]
    if k > n:
      self.cache[(k, n)] = 0
      return 0
    if k == n:
      self.cache[(k, n)] = 1
      return 1
    val = self.p(k+1, n) + self.p(k, n-k)
    self.cache[(k, n)] = val
    return val

def main ():
  
  pc = PartitionCounter()
  for n in range(3,10**6):
    count =  pc.p(1, n)
    if (count % 10**5) == 0:
      print '\nAnswer: {0} {1}'.format(n, count)
      sys.exit(0)
    
    if not n % 100:
      print n
  pass

if __name__ == '__main__':
  main()
