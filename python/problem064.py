#!/usr/bin/python
'''
problem 64: http://projecteuler.net/problem=64
            http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Example.2C_square_root_of_114_as_a_continued_fraction
'''

def get_root_as_cont_frac(s, max_iter=500):
  triples = []
  
  (m, d, a) = 0, 1, int(s**.5)
  for j in range(max_iter):

    # track known tuples, ditch as soon as we see a loop
    if (m, d, a) in triples:
      i = triples.index((m, d, a))
      return triples[i:]
    triples.append((m, d, a))

    # update each of the algorithm's local vars
    m1 = d*a-m
    d1 = (s-m1**2)/d
    a1 = (int(s**.5) + m1)/d1
    (m, d, a) = (m1, d1, a1)
  pass

max_n = 10000+1
not_square = [i for i in range(max_n) if i != int(i**.5)**2]
cycle_lengths = [len(get_root_as_cont_frac(i)) for i in not_square]
odd_cycle_count = len(filter(lambda x: x%2, cycle_lengths))
print 'Answer: {0}'.format(odd_cycle_count)