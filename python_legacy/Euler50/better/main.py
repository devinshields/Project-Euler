#!/usr/bin/python

from Euler import is_prime
from time import clock

# start a process timer
clock()

# setup a counter
max = 0

# get a list of primes
z = [n for n in range(10**6+1) if is_prime(n)]
lenght = len(z)

for a in range(0, lenght-1):
  #
  t = 0
  sum = 0
  wyrazy = 0

  #
  for i in range(a, lenght-1):
    sum = sum + z[i]
    if sum > 10**6:
      break
    wyrazy += 1
    if is_prime(sum) and sum != z[i] and wyrazy > max:
      r = sum
      max = wyrazy
print(r)
print(clock())
