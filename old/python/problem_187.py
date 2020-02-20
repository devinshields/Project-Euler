#!/usr/bin/env python
# coding: utf-8
'''
https://projecteuler.net/problem=187
    A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
    There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
    How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?
'''


import euler


def get_answer():
    '''  '''
    max_value = 10**8

    # get all prime factors that could be 2 factor
    primes = sorted(euler.prime_sieve(max_value/2 + 10**6))
    two_factor_count, max_index = 0, len(primes)

    for i, prime0 in enumerate(primes):
        limit = 10**8 / prime0;
        j = i
        while j <= max_index and primes[j] <= limit:
            two_factor_count += 1
            j += 1
    print 'two_factor_count: {}'.format(two_factor_count)


def main():
    '''  '''
    get_answer()

if __name__ == "__main__":
    main()

