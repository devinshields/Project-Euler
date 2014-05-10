#!/usr/bin/python -tt
'''
  problem 107: http://projecteuler.net/problem=107

  The input graph G is assumed to have the following
  representation: A vertex can be any object that can
  be used as an index into a dictionary.  G is a
  dictionary, indexed by vertices.  For any vertex v,
  G[v] is itself a dictionary, indexed by the neighbors
  of v.  For any edge v->w, G[v][w] is the length of
  the edge.
'''

import MinimumSpanningTree

# configs
fin_path = 'network.txt'

def get_weight(x):
 return int(x) if x.isdigit() else 0

# get the data as numeric link values
rows = [map(get_weight, l.strip().split(',')) for l in open(fin_path, 'rb')]

# build a graph object from the text file and solve using a minimum spanning tree class
G = {node_ind: {} for node_ind in range(40)}
for x, row in enumerate(rows):
  for y, val in enumerate(row):
    if val:
      G[x][y] = val

min_cost_tree = MinimumSpanningTree.MinimumSpanningTree(G)

# cost calculations
original_cost   = sum(G[u][v] for u in range(40) for v in range(40) if v > u and u in G and v in G[u])
minimum_cost    = sum(map(lambda t: G[t[0]][t[1]], min_cost_tree))
maximum_savings = original_cost - minimum_cost


print 'Answer: {0}'.format(maximum_savings)