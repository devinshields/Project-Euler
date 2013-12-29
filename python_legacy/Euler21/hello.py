def is_amicable(num):
  x = div_sum(num)
  y= div_sum(x)
  print '**',num,x,y 
  if num == y and x != y:
    return num
  return 0

def div_sum(num):
  t=0
  for i in range(1,num/2+1):
    if num%i == 0:
      t = t + i
  return t

t=0
for i in range(1,10000):
  t = t + is_amicable(i)

print '\n\n',t
