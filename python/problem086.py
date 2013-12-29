#!/usr/bin/python
'''
  think of the cube as an unfolded paper cube like here:
    http://puzzles.nigelcoldwell.co.uk/three.htm

--------------------------------------------------------
  From the Euler example:
--------------------------------------------------------
     - - - - - - - - - - 
    |           |       |
    |           |       |
    |           |       |
  6 |           |       |
    |           |       |
    | _ _ _ _ _ | _ _ _ |
          5         3
--------------------------------------------------------
  length/hypotenuse:  (6^2 + (5+3)^2)^(1/2) == 10
--------------------------------------------------------

  NOTE: for simplicity assume that all cube descriptions 
        are ordered. the above would be (3, 5, 6).

  NOTE: Shortest paths can only have integer lengths
        when (sum(cube(:1)), cube[2]) are legs of a
        Pythagorean triple.

--------------------------------------------------------
  TEST: find cubes when M = 100 to confirm
        my understanding of the problem
--------------------------------------------------------
import itertools

def cubes_smaller_than(M=100):
  possible_cubes = sorted(set(tuple(sorted(tup)) for tup in itertools.combinations_with_replacement(range(1, M + 1), 3)))
  pythag_cubes   = filter(lambda c: ((sum(c[:2])**2 + c[2]**2)**.5).is_integer(), possible_cubes)
  for cube in pythag_cubes:
    yield cube

print len(list(cubes_smaller_than())) # this correctly produces 2060
--------------------------------------------------------

  PLAN OF ATTACK:
    1) produce all Pythagorean primitive triples with hypotenuse < M

'''

import itertools
import sys

#
# ------------------------------------------------ #
#
# *** this is too slow ***
pythag_cube_count = 0
M = 0
while True:
  if pythag_cube_count > 10**6:
    print 'Answer: {0}'.format(M)
    sys.exit(0)
  M += 1
  cubes              = ((k, j, M) for j in range(1, M+1) for k in range(1, j+1))
  pythag_cubes       = itertools.ifilter(lambda c: ((sum(c[:2])**2 + c[2]**2)**.5).is_integer(), cubes)
  pythag_cube_count += len(list(pythag_cubes))
  print M, pythag_cube_count



#
# ------------------------------------------------ #
#
pythag_cube_count = 0
for M in itertools.count(1):
  for small_sides_sum in range(2, 2*M+1):
    if ((small_sides_sum**2 + M**2)**.5).is_integer():
      pythag_cube_count += min(M, small_sides_sum-1) - (small_sides_sum-1)/2  # *** I don't understand why this works/what's going on here. ***

  if pythag_cube_count > 10**6:
    print 'Answer: {0}'.format(M)
    break