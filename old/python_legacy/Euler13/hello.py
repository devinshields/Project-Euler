import sys
fileString = sys.stdin.read()
lines = fileString.split("\n")

print 'Num of Lines:',len(lines)

y=0
i=0
for line in lines:
  print i
  i=i+1
  num = int(line)
  print ' ',y
  print '+',num
  y = y + num

  print '=',y,'\n' 

