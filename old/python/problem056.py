#!/usr/bin/python -tt
#
# problem 56: http://projecteuler.net/problem=56
#

print max(map(lambda n: sum(map(int,str(n))),[a**b for a in range(2,100) for b in range(2,100)]))