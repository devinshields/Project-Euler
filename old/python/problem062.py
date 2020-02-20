#!/usr/bin/python
#
# problem 62: http://projecteuler.net/problem=62

from itertools import groupby

def main ():
  five_perms = []
  group_tups = sorted([(''.join(sorted(str(i**3))), i**3) for i in range(340,10**5)])
  for key, grp in groupby(group_tups, lambda t: t[0]):
    grp = [n for n in grp]
    if len(grp) == 5:
      five_perms.append(grp[0][1])
  print '\nAnswer:', min(five_perms)
  pass

if __name__ == '__main__':
  main()
