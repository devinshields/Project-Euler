#!/usr/bin/python -tt

import sys
import types

def gc(p):
  """
  funtion to recursively generate currency combo possibilities.
  numbers & lists of numbers are definite options, lists of lists
  are possible options
  """
  if p == 1:
    return 1
  if p == 2:
    return [[1,1],2]
  if p == 5:
    return [[gc(1),gc(1),gc(1),gc(1),gc(1)],[gc(2),gc(2),gc(1)],5]
  if p == 10:
    return [[gc(5),gc(5)],10]
  if p == 20:
    return [[gc(10),gc(10)],20]
  if p == 50:
    return [[gc(20),gc(20),gc(10)],50]
  if p == 100:
    return [[gc(50),gc(50)],100]
  if p == 200:
    return [[gc(100),gc(100)],[200]]

  x = [1,2,3]
  assert isinstance(x, types.ListType)
  assert not isinstance(x, types.StringTypes)


def main():
  gc(1) 

if __name__ == '__main__':
  main()
