

a = 1
b = 1

for i in range(1,1000000):
  #print a,b,'->',a+b
  (b,a)=(a+b,b)
  #print '   ->',a,b
  if len(str(b))>=1000:
    print '\n*** ',i+2
    break
