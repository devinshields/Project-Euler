#!/usr/bin/python

import collections

DimCount = collections.namedtuple('DimCount', ['count', 'dim'])

def count_sub_recs(tup):
  p, q = tup
  return sum((q-i) * (p-j) for i in range(q) for j in range(p))

possible_counts = [DimCount(count_sub_recs((i,j)), (i,j)) for i in range(1, 175) for j in range(1, i+1)]
score_sorted    = sorted(possible_counts, key=lambda d: abs(d.count - 2*10**6))
print score_sorted[0].dim[0] * score_sorted[0].dim[1]