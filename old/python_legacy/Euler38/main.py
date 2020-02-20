#!/usr/bin/python
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n  1?

"""

def is_pandigital(n, s=9):
  n=str(n)
  return len(n)==s and not '1234567890'[:s].strip(n)

def main ():
  maxN   = 3
  maxPan = 0
  for n in range(2,maxN+1):
    catList = range(1,n+1)
    for num in range(1,10**4):
      res = reduce(lambda x,y: str(x) + str(num*y),catList,'')
      if is_pandigital(res) and res > maxPan:
        maxPan = res
  print maxPan
  pass

if __name__ == '__main__':
  main()
