#!/usr/bin/python
'''
solver code taken from Norvig's awesome article:    http://norvig.com/sudoku.html
'''


import itertools
import collections


GroupRow = collections.namedtuple('GroupRow', ['group', 'row'])

lines     = [line.strip() for line in open('sudoku.txt', 'r')]
grp_lines = [GroupRow(i - i%10, line) for i,line in enumerate(lines)]

for key, grp in itertools.groupby(grp_lines, key=lambda t: t.group):
  # construct an int matrix
  sudoku = map(lambda t: map(int, t.row), list(grp)[1:])
  print ''.join([''.join(map(lambda i: str(i) if i else '.', row)) for row in sudoku])
  
