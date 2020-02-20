#!/usr/bin/python
"""

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 212
15 = 7 + 222
21 = 3 + 232
25 = 7 + 232
27 = 19 + 222
33 = 31 + 212

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
import sys
from Euler import is_prime
from math import floor

def main ():

  # set the max number to test
	maxPrime = 10**4

	# grab a list of primes & the nums we're going to test
	primes = [i for i in range(1,maxPrime) if is_prime(i)]
	testNums = [i for i in range(2,maxPrime) if i not in primes and (i % 2) == 1]

	# get a list of candidate primes for each composite number
	for ind,testNum in enumerate(testNums):
		candPrimes = [p for p in primes if p < testNum] 
		
		s = False

		# for each prime candidate, do some math
		for c in candPrimes:
			t = ((testNum-c)/2.)**.5
			if t == floor(t):
				print testNum,c
				s = True
				continue
		if s == False:
			print 'All Done! Answer:', testNum
			sys.exit(0)


	pass

if __name__ == '__main__':

  main()
