#!/usr/bin/python
#
# problem 63: http://projecteuler.net/problem=63
#

n_set = set()
for i in range(1,10**3):
  for power in range(1,30):  
    if len(str(i**power)) == power:
      n_set.add(i**power)
print '\nAnswer:', len(n_set)