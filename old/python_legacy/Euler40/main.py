#!/usr/bin/python

frac = ''.join([str(i) for i in range(1,10**6)])
print 'And the answer is:',reduce(lambda x,y: x*y,[int(frac[j]) for j in [10**i-1 for i in range(6+1)]],1)
