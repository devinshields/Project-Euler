#!/usr/bin/python
#
# problem 57: http://projecteuler.net/problem=57
#

from fractions import Fraction as f

iter = lambda x: f(1,2 + x)

counter = 0
loop_counter = 1

whole = f(1)
frac = f(1,2)
while loop_counter < 10**3:
  loop_counter += 1
  frac = iter(frac)
  num = whole + frac
  if len(str(num.numerator)) > len(str(num.denominator)):
    counter += 1
print '\nAnswer:', counter
