#!/usr/bin/python
'''
problem 68: http://projecteuler.net/problem=68

plan of attack:
  1) generate all 10! possible arrangements
  2) map these into sets of 3 tuples that represent 3-bars in the star grid
  3) filter out all non 'lowest outter digit first' arrangements
  4) filter out all 17 digit results
  5) check if the 3-bar config is a valid magic shape, sum-compare all tuples

'''

import itertools
import collections

MagicRing = collections.namedtuple('MagicRing', ['number_sequence', 'three_bars'])

get_elements = lambda search_list, ind: [search_list[i] for i in ind]
ind_set = [(0, 1, 2), (3, 2, 4), (5, 4, 7), (6, 7, 8), (9, 8, 1)]

# make all possible rings
rings = itertools.imap(lambda seq: MagicRing(seq, map(lambda ind: tuple(get_elements(seq, ind)), ind_set)), itertools.permutations(range(1, 10+1)))

# filter out 17 digit rings
rings = itertools.ifilter(lambda r: (len(''.join(map(str, [n for tup in r.three_bars for n in tup]))) < 17), rings)

# filter out non-'lowest digit first'
rings = itertools.ifilter(lambda r: r.three_bars[0][0] == min(map(lambda t: t[0], r.three_bars)), rings)

# filter out rings whose 3 bars don't sum to one value
rings = itertools.ifilter(lambda r: min(map(sum, r.three_bars)) == max(map(sum, r.three_bars)), rings)

for r in rings:
  print ''.join(map(str, [n for tup in r.three_bars for n in tup])), r