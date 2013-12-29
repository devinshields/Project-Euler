#!/usr/bin/python
'''
  NOTE: that for any primitive pythagorean triple of length L, multiples of size M will have length size M*L
        given a list of all pythagoream triples of L < max_L, we can use a prime sieve-like lookup array to find
        lengths with only one corresponding triple.

  1) find all primitive pythagorean triples smaller than length max_L
      x. http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
      x. http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
  2) iteratively multiple their length until L > max_L, track which lengths hit
  3) count lengths with only one hit

  NOTE: doing this with matricies and tree recursion is more fun, but too slow to finish in a minute when I tested with numpy'''

import fractions

max_L = 1500000

count_vect = [0] * (max_L + 1)

def get_multiples(p):
  m = 1
  while m * p < max_L:
    yield m * p
    m += 1

for m in range(1, int((max_L/2.)**.5)):
  for n in range(1, m):
    if (m-n)%2 and fractions.gcd(m, n) == 1:
      prim_triple = (m**2 - n**2, 2 * m * n, m**2 + n**2)
      for length in get_multiples(sum(prim_triple)):
        count_vect[length] += 1


print 'Answer: {0}'.format(sum(filter(lambda v: v == 1, count_vect)))
