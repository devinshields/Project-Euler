#!/usr/bin/env python
'''
  http://projecteuler.net/problem=66
  http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Example.2C_square_root_of_114_as_a_continued_fraction
'''


from fractions import Fraction
import sys


def get_root_as_cont_frac(s, max_iter=500):
  base_int = int(s**.5)
  triples = []
  (m, d, a) = 0, 1, int(s**.5)
  for j in range(max_iter):

    # track known tuples, ditch as soon as we see a loop
    if (m, d, a) in triples:
      i = triples.index((m, d, a))
      return (base_int, tuple(map(lambda t: t[2], triples[i:])))
    triples.append((m, d, a))

    # update each of the algorithm's local vars
    m1 = d*a-m
    d1 = (s-m1**2)/d
    a1 = (int(s**.5) + m1)/d1
    (m, d, a) = (m1, d1, a1)


# test  -  http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#sqrts
assert get_root_as_cont_frac(2)   == (1, (2,))
assert get_root_as_cont_frac(3)   == (1, (1, 2))
assert get_root_as_cont_frac(5)   == (2, (4,))
assert get_root_as_cont_frac(7)   == (2, (1, 1, 1, 4))
assert get_root_as_cont_frac(13)  == (3, (1, 1, 1, 1, 6))
assert get_root_as_cont_frac(14)  == (3, (1, 2, 1, 6))
assert get_root_as_cont_frac(15)  == (3, (1, 6))
assert get_root_as_cont_frac(69)  == (8, (3, 3, 1, 4, 1, 3, 3, 16))
assert get_root_as_cont_frac(114) == (10, (1, 2, 10, 2, 1, 20))


def convergence_sequence_from_cont_frac(cont_frac):
  aproximations = []
  for aprox_depth in range(len(cont_frac[1])):
    partial_cont_frac = cont_frac[1][:aprox_depth+1]
    # note: process the continuos fraction components backwards.
    #       the odd looking lambda and default 0 value cover cases where
    #       there's only 1 continuous fraction component without dividing by 0.
    aprox_frac = reduce(lambda a0, a1: (a0 and Fraction(1, a0) or 0) + Fraction(a1, 1), partial_cont_frac[::-1], 0)**-1
    aprox = cont_frac[0] + aprox_frac          
    aproximations.append(aprox)
  return tuple(aproximations)


# test
assert convergence_sequence_from_cont_frac(get_root_as_cont_frac(14)) == \
                        (Fraction(4, 1), Fraction(11, 3), Fraction(15, 4), Fraction(101, 27))


def diophantine(x, y, D):
    return x**2 - D * y**2


def get_minimal_diophantine_x(D):
  print 'solving: D == {0}\n'.format(D)

  # get square root D's continued fraction representation
  cont_frac = get_root_as_cont_frac(D)

  # and pair up convergents in the series
  convergents = convergence_sequence_from_cont_frac(cont_frac)

  #

  # plug in convergent fractions as (x, y)
  sys.exit()

  return 1


# test
assert get_minimal_diophantine_x(2) == 3
assert get_minimal_diophantine_x(3) == 2
assert get_minimal_diophantine_x(5) == 9
assert get_minimal_diophantine_x(6) == 5
assert get_minimal_diophantine_x(7) == 8

assert get_minimal_diophantine_x(13) == 649


# 
max_D = 7

# get non-squares less than max_D
d_list = filter(lambda i: (round(i**.5))**2 != i, range(2, max_D+1))

print '\nd_list: {0}\n'.format(d_list)


# map each equation parameter D to its minimal solution, (D, minimal_x)
d_min_x_tups = [(get_minimal_diophantine_x(d), d) for d in d_list]


# fetch and print the D with the biggest x min
answer = sorted(d_min_x_tups)[-1][1]
print '\nanswer: {0}\n'.format(answer)

