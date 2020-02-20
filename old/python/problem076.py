#!/usr/bin/python
#
#   math here: http://en.wikipedia.org/wiki/Partition_function_(number_theory)#Partition_function
#

# simple memoize tool
def memoize(f):
  cache = {}
  def memf(*x):
    if x not in cache:
      cache[x] = f(*x)
    return cache[x]
  return memf

# recursive partition function
@memoize
def p(k, n):
  if k == n:
    return 1
  if k > n:
    return 0
  return p(k+1, n) + p(k, n-k)

def main ():
  
  print p(1, 100) - 1
  pass

if __name__ == '__main__':
  main()





'''
def slow():
  max_n = 101
  next_set = set([tuple([0]*(max_n-2)+[1])])
  for r in range(1,max_n+1):
    count = len(next_set)
    print r, count, factor(count)
    seed_set = next_set
    next_set = set()
    for seed in seed_set:
      ind = [i for i in range(len(seed)) if seed[i] > 0]
      # inc the ones spot
      l = list(seed)
      l[-1] += 1
      next_set.add(tuple(l))
      # inc each index
      for i in ind:
        l = list(seed)
        l[i]   -= 1
        l[i-1] += 1
        next_set.add(tuple(l))
  pass

'''
