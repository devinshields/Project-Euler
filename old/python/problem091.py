#!/usr/bin/python

from itertools import combinations

def is_right_tri(points):
  '''get various line lengths, sort, test for pythag's equality'''
  p1,p2 = points[0],points[1]
  d1,d2 = p1[0]**2 + p1[1]**2,p2[0]**2 + p2[1]**2
  d3    = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
  three_dist = sorted([d1, d2, d3])
  return sum(three_dist[:2]) == three_dist[-1]

def main ():
  grid_max = 50
  points = [(i, j) for i in range(grid_max+1) for j in range(grid_max+1) if (i,j) != (0, 0)]
  
  print sum([1 for two_points in combinations(points, 2) if is_right_tri(two_points)])
  pass

if __name__ == '__main__':
  main()
