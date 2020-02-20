#!/usr/bin/python -tt
#
# problem 90: http://projecteuler.net/problem=90
#

import itertools as it

def add_69s(die):
  if 6 in die or 9 in die:
    return tuple(sorted(set(list(die) + [6, 9])))
  return die

def can_make_all_squares(pair):

  squares = set([1, 4, 9, 16, 25, 36, 49, 64, 81])

  # modify the die, adding 6 if there's a 9 and vice versa
  mod_pair = map(add_69s, pair)

  # make al possible numbers with these dice
  num_set = set()
  num_pairs = list(it.product(mod_pair[0], mod_pair[1]))
  num_set.update(map(lambda t: t[0]*10 + t[1], num_pairs))
  num_set.update(map(lambda t: t[1]*10 + t[0], num_pairs))

  return len(squares) == len(sorted(num_set.intersection(squares)))

def main():

  # get a list of all possible dice pairs - pair-sorted and unique
  dice = it.combinations(range(10),6)
  pairs = sorted(set(map(tuple,map(sorted,it.combinations_with_replacement(dice,2)))))

  # test each pair to see if it can generate all the < 100 squares
  print '\nAnswer: {0}'.format(len(filter(can_make_all_squares, pairs)))

  pass

if __name__ == '__main__':
  main()