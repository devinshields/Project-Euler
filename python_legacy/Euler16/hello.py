import math
x=math.pow(2, 1000)
y=str(int(x))
print y
num_sum = 0
for i in y:
  print i
  num_sum = num_sum + int(i)
  print 'NUMBER',i,'SUM:',num_sum
