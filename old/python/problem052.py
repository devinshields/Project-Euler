#!/usr/bin/python -tt
#
# problem 52: http://projecteuler.net/problem=52
#

import sys

i = 10
while 1:
  i += 1
  if len(set([''.join(sorted(str(i*x))) for x in range(1,7)])) == 1:
    print '\nAnswer:',i
    sys.exit(0)