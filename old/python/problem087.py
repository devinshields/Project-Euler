#!/usr/bin/python

from Euler import prime_sieve

def main ():
  max_n = 50*10**6

  # get the max primes for each exponent slot
  max_square = int((max_n - 2**3 - 2**4)**(1/2.))+1
  max_cube   = int((max_n - 2**2 - 2**4)**(1/3.))+1
  max_quart  = int((max_n - 2**2 - 2**3)**(1/4.))+1
  
  # sieve for the possible sets
  p_2 = prime_sieve(max_square)
  p_3 = prime_sieve(max_cube)
  p_4 = prime_sieve(max_quart)
  
  # build all feasible combos & filter
  pos_tups = [(i ,j, k) for i in p_2 for j in p_3 for k in p_4]
  pos_nums = [t[0]**2 + t[1]**3 + t[2]**4 for t in pos_tups]

  sub_max_nums = filter(lambda i: i < max_n, pos_nums)

  print '\nAnswer: {0}'.format(len(set(sub_max_nums)))
  pass

if __name__ == '__main__':
  main()
