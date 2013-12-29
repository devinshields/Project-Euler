import itertools

inp = '0123456789'
x=itertools.permutations(inp, len(inp)) 
ind=1
for i in x:
  print ind,i
  if ind == 1000000:
    print i
    break
  ind = ind +1
