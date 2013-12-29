#!/usr/bin/python
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?

"""
from math import floor

def main ():
  permDic = {}
  for p in range(12,1000+1):
    #print p
    for side1 in range(1,p+1):
      #print side1

      for side2 in range(1,p+1):
        side3 = p - side1 - side2
        if side3<=0: continue
        if (side1**2 + side2**2)**.5 == side3:
	  if p not in permDic: permDic[p] = []
	  permDic[p].append(sum([x**2 for x in [side1,side2,side3]]))
  for p in permDic:
    print p, len(set([x for x in permDic[p]]))

if __name__ == '__main__':
  main()
