#!/usr/bin/python
#
# math from: http://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler.27s_product_formula
#

from Euler import factor
from operator import mul

print '\nAnswer: {0}'.format(max([(reduce(mul, map(lambda p:1-1/float(p), map(lambda t: t[0], factor(n))))**-1, n) for n in range(2, 10**6+1)]))
