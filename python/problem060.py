#!/usr/bin/python

from itertools import combinations
from Euler import prime_sieve
from math import ceil
  
def main ():
  max_prime = 10**8-1
  p = prime_sieve(max_prime)
  primes = set(p)
  test_p = filter(lambda i: len(str(i)) <= int(ceil(len(str(max_prime))/2.)), p)

  def cat_set_is_prime(prime_set):
    test_num = prime_set[-1]
    for num in prime_set[:-1]:
      if int(''.join(map(str, [num, test_num]))) not in primes or int(''.join(map(str, [test_num, num]))) not in primes:
        return False
    return True

  # get 2-tuples that match the criterion
  new_tup_list = sorted(set([combo for combo in combinations(test_p, 2) if cat_set_is_prime(combo)]))

  # try to add each test_p to the combos to make n+1 tuples satisfying the criterion
  for tup_size in range(3, 5+1):
    cur_tup_list = new_tup_list
    new_tup_list = []
    for tup in cur_tup_list:
      for new_num in test_p:
        if tup[-1] < new_num:
          cand = tuple(list(tup) + [new_num])
          if cat_set_is_prime(cand):
            new_tup_list.append(cand)

  print '\nAnswer: {0}'.format(sum(new_tup_list[0]))
  pass

if __name__ == '__main__':
  main()