#!/usr/bin/python -tt
#
# problem 99: http://projecteuler.net/problem=99
#
import math
pairs = [map(int, l.strip().split(',')) for l in  open('base_exp.txt', 'r')]
log_prods = [(p[1]*math.log(p[0]), i) for i,p in enumerate(pairs)]
print '\nAnswer: {0}'.format(max(log_prods)[1])
