#!/usr/bin/env python
# coding: utf-8
'''
https://projecteuler.net/problem=179

Find the number of integers 1 < n < 10**7,
for which n and n + 1 have the same number
of positive divisors.

For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

--------------------------------------------------------------------------------
http://mathcentral.uregina.ca/QQ/database/QQ.02.06/joe1.html
--------------------------------------------------------------------------------
    calculate a number's divisor count given that number's prime factorization

'''


import operator

import euler


def main():
    '''  '''

    results = {}
    max_value = 10**7

    for n in range(2, max_value+1):
        if not n % 10**4:
            print n
        factor_sum = reduce(operator.mul, map(lambda tup: tup[1]+1, euler.factor(n)), 1)
        results[n] = factor_sum

    matches = 0
    for n in range(2, max_value):
        if results[n] == results[n+1]:
            matches += 1 

    print matches

if __name__ == "__main__":
    main()

