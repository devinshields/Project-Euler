
import math

def next_collatz(n):
  if n%2==0:
    return n/2
  return 3*n+1

max_length = 1
for i in range(2,1000000):
  i_c = 1
  i_j = i
  while i_j != 1:
    i_c = i_c+1
    i_j = next_collatz(i_j)
#print i,i_j,i_c
  if i_c > max_length:
    max_length = i_c
    max_i = i
    print 'Current Longest String from:',max_i,max_length

print '\n\n***Current Longest String from:',max_i,max_length


