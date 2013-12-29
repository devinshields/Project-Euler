#!/usr/bin/python -tt
#
# problem 95: http://projecteuler.net/problem=95
#

from euler import factor
import itertools
from operator import mul
import tarjan

def get_sum_of_divisors(n):
  if not n%(10**4):
    print n
  facts = factor(n)
  poss_fact_list = map(lambda t: [t[0]**i for i in range(t[1]+1)], facts)
  pos_prod = list(itertools.product(*poss_fact_list))
  div_list = map(lambda t: reduce(mul, t), pos_prod)
  return sum(div_list)-n

def main():

  # get a mapping of numbers to their divisor sums
  d = {i: [get_sum_of_divisors(i)] for i in range(10, 10**6+1)}
  
  # get the graph's connected components
  conn_comps = tarjan.tarjan(d)
  
  # get the cycle lengths
  len_of_conn = map(lambda l: (len(l), l), conn_comps)
  tup = max(len_of_conn)
  
  print '\nAnswer: {0}'.format(min(tup[1]))

if __name__ == '__main__':
  main()
