def is_abundant(num):
  return num < div_sum(num)

def div_sum(num):
  t=0
  for i in range(1,num/2+1):
    if num%i == 0:
      t = t + i
  return t

def is_abundant_sum(i,ab_num):
  for j in range(1,i/2+1):
    #print 'Testing:',i
    #print '   with:',j,'and',i-j,'->'
    #print '        ',ab_num[j],'+',ab_num[i-j],'->',ab_num[j]+ab_num[i-j]==i
    if ab_num[j]+ab_num[i-j]==i:
      return True
  return False
    
#start main method
ab_num = []
max_test = 28123+3
for i in range(0,max_test):
  print i
  if is_abundant(i):
    ab_num.append(i)
  else:
    ab_num.append(0)
  #print i,ab_num[-1]


t = 0
for i in range(1,max_test):
  if not is_abundant_sum(i,ab_num):
    x=t
    t = t + i
    print '   ',i, 'is not an abunant sum. t->t',x,'->',t
print '\n\nANSWER:', t
