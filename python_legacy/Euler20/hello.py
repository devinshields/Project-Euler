
import math


x = math.factorial(100)
str_num = str(x)

num_sum = 0

for i in str_num[:-1]:
  num_sum = num_sum + int(i)


print 'NUMBER',str_num[:-1],'SUM:',num_sum
