#!/usr/bin/python
'''   http://projecteuler.net/problem=100

If a box contains twenty-one coloured discs,
  composed of fifteen blue discs and six red discs, and two discs were taken at random,
  it can be seen that the probability of taking two blue discs,
      P(BB) = (15/21) * (14/20) = 1/2.

The next such arrangement for which there is exactly 50 chance of taking two blue discs at random,
  is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over
    10^12 = 1,000,000,000,000 discs in total,
  determine the number of blue discs that the box would contain.


Ratio Formula:
  (b)/(b + r) * (b - 1)/(b + r -1)

50% Points:
                (15, 6)
                (85, 35)
'''


import sys
import fractions


def get_probability_of_two_blues(b ,r):
  p1 = fractions.Fraction(b, b+r)
  p2 = fractions.Fraction(b-1, b+r-1)
  return p1 * p2


half = fractions.Fraction(1, 2)


b = int(7.0710678118669397101025117673099626546641823709 * 10**11) - 1
r = int(2.9289321881330602898974882326900373453358176290 * 10**11) - 1

while True:
  frac = fractions.Fraction(b, b + r) * fractions.Fraction(b - 1, b + r - 1)
  print float(frac), frac
  if frac == half and b + r > 10 ** 12:
    print
    print frac, b, r
    print 'ANSWER:', b
    sys.exit(0)
  elif frac < half:
    b += 1
  else:
    r += 1

  
