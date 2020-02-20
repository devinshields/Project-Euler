#!/usr/bin/python
#
# some source from: http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/
#

from numpy import matrix
from itertools import izip
from Dijkstra import shortestPath

def vec_add(xs,ys):
  return tuple(x + y for x, y in izip(xs, ys))

def main ():

  # read in the matrix/graph
  #file_path = 'problem81.matrix.small.txt'
  file_path = 'problem81.matrix.txt'
  A = matrix([map(int,line.strip().split(',')) for line in open(file_path, 'r')])
  
  # build a weighted, directed graph as: {node: {node: weight}}
  nodes = [(x,y) for x in range(A.shape[0]) for y in range(A.shape[1])]
  graph = {node: {} for node in nodes}
  for shift in [(1, 0), (0, 1)]:
    for node in graph:
      neighbor = vec_add(node,shift)
      if neighbor[0] < A.shape[0] and neighbor[1] < A.shape[1]:
        neighbor_val = A[neighbor[0],neighbor[1]]
        graph[node][neighbor] = neighbor_val

  # set the param nodes
  start,end = (-1, -1), vec_add(A.shape,(-1, -1))

  # make an imaginary node above the graph
  graph[start] = {(0,0): A[0,0]}
  
  # run the algorithm
  Path,P,D = shortestPath(graph,start,end)
  print end
  print '\nAnswer: {0}'.format(D[end])
  print
  print graph
  pass

if __name__ == '__main__':
  main()
