#!/usr/bin/python

from bigfloat import *

dig_sum = 0
for i in range(2,100):
  if i in [x**2 for x in range(10+1)]:continue
  c_list = filter(lambda c:str.isdigit(c), str(sqrt(i, precision(10**4))))[:100]
  dig_sum += sum(map(int,c_list))

print 'Answer: {0}'.format(dig_sum)
