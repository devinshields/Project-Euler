#!/usr/bin/python
'''
problem 66: http://projecteuler.net/problem=66
            http://en.wikipedia.org/wiki/Pell's_equation#Fundamental_solution_via_continued_fractions
            http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Example.2C_square_root_of_114_as_a_continued_fraction

  Let frac{h_i}{k_i} denote the sequence of convergents
    to the continued fraction for \sqrt{n}.
    Then the pair (x1,y1) solving Pell's equation and minimizing x
    satisfies x1 = hi and y1 = ki for some i.

'''

import collections

MDA = collections.namedtuple('MDA',['m','d','a'])

def get_root_as_cont_frac(s, max_iter=500):
  triples = []

  (m, d, a) = 0, 1, int(s**.5)
  orig = MDA(m, d, a)
  for j in range(max_iter):

    # track known tuples, ditch as soon as we see a loop
    if (m, d, a) in triples:
      i = triples.index(MDA(m, d, a))
      return map(lambda t: t[2], [orig] + triples[i:])
    triples.append(MDA(m, d, a))

    # update each of the algorithm's local vars
    m1 = d*a-m
    d1 = (s-m1**2)/d
    a1 = (int(s**.5) + m1)/d1
    (m, d, a) = (m1, d1, a1)


assert get_root_as_cont_frac(114) == [10, 1, 2, 10, 2, 1, 20]


get_root_as_cont_frac(2)
get_root_as_cont_frac(3)
get_root_as_cont_frac(5)
get_root_as_cont_frac(6)


max_D = 1000
max_D = 7

Ds = filter(lambda x: round(x**.5)**2 != x, range(2, max_D+1))

print Ds