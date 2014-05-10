#!/usr/bin/env python
'''
  http://projecteuler.net/problem=66
'''


def get_minimal_diophantine_x(D):
  print 'solving: D == {0}'.format(D)

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

