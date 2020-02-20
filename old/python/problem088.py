#!/usr/bin/python

from Euler import factor
from operator import mul


def prod(lst):
  return reduce(mul, lst)

def min_prod_sum(n):
  return 

def print_prod_sum(lst):
  print 'sum: {0}\t\tprod: {1}\t\t{2}'.format(sum(lst), prod(lst), lst)

def main ():
  
  # k == 7 solution
  #lst = (1,1,1,1,1,3,4)
  #print_prod_sum(lst)

  # k == 8 solution
  #lst = (1,1,1,1,1,2,2,3)
  #print_prod_sum(lst)

  # k == 9 solution
  #lst = (1,1,1,1,1,1,1,3,5)
  #print_prod_sum(lst)

  # k == 10 solution
  lst = (1,1,1,1,1,1,1,1,4,4)
  print_prod_sum(lst)



  pass

if __name__ == '__main__':
  main()
