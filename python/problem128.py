#!/usr/bin/python -tt
'''
  problem 128: http://projecteuler.net/problem=128
'''

class Tile(object):
  def __init__(self, i):
    self.number = i
  @property
  def adj_tiles(self):
    return [i+self.number for i in range(5)]

t = Tile(5)
t.number
t.adj_tiles