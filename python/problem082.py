#!/usr/bin/python
#
# http://projecteuler.net/problem=82
#

from numpy import matrix
from itertools import izip
from Dijkstra import shortestPath

def vec_add(xs,ys):
  return tuple(x + y for x, y in izip(xs, ys))

def main ():

  # read in the matrix/graph
  file_path = 'problem81.matrix.txt'
  A = matrix([map(int,line.strip().split(',')) for line in open(file_path, 'r')])
  
  # build a weighted, directed graph as: {node: {node: weight}}
  nodes = [(x,y) for x in range(A.shape[0]) for y in range(A.shape[1])]
  graph = {node: {} for node in nodes}
  for shift in [(0, 1), (1, 0), (-1, 0)]:
    for node in graph:
      neighbor = vec_add(node,shift)
      if neighbor[0] in range(A.shape[0]) and neighbor[1] in range(A.shape[1]):
        neighbor_val = A[neighbor[0],neighbor[1]]
        graph[node][neighbor] = neighbor_val

  # set the param nodes
  start,end = (-1, -1), A.shape

  # make an imaginary edges for the (start -> leftmost column)
  graph[start] = {}
  for y in range(A.shape[1]):
    graph[start][(y, 0)] = A[y,0]

  # make imaginary edges for the (rightmost column -> end)
  for y in range(A.shape[1]):
    graph[(y, A.shape[1]-1)][end] = 0
  
  # run the algorithm
  Path,P,D = shortestPath(graph,start,end)
  
  print '\nAnswer: {0}'.format(D[end])
  
  pass

if __name__ == '__main__':
  main()
