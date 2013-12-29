#!/usr/bin/python
"""

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

***
devin's note:
	'divisible by' goes by prime numbers, indexes go up by 1
***
"""
from itertools import permutations

def main ():

  nums = []
  for i in permutations('0123456789'):
    num = ''.join(i)
    # check if divisible by 17
    if int(num[7:10])%17==0:
      # check if divisible by 13
      if int(num[6:9])%13==0:
	# check if divisible by 11
        if int(num[5:8])%11==0:
	  # check if divisible by 7
          if int(num[4:7])%7==0:
	    # check if divisible by 5
            if num[5] in ['0','5']:
	      # check if divisible by 3
	      if int(num[2:5])%3==0:
		# check if divisible by 2
	      	if int(num[3])%2==0:
		  nums.append(int(num))

  print 'And the answer is:',sum(nums)
  pass

if __name__ == '__main__':
  main()
