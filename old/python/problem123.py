#!/usr/bin/python -tt
'''
    problem 123: http://projecteuler.net/problem=123
'''


from euler import prime_sieve

primes = prime_sieve(10**6)
np = zip(range(1, len(primes)+1),primes)
np = filter(lambda tup: tup[0] % 2, np)

for n, p in np:
  moded = ((p-1)**n + (p + 1)**n) % p**2
  if moded > 10**10:
    print n
    break

