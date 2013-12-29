def Cat(filename):
  f = open(filename,'rU')
  text = f.read()
  return text

text = Cat('names.txt')
names = sorted(text.split(','))

t = 0
i = 1
#names = ['"ABCDE"']
for name in names:
  print name,i
  v = 0
  for s in name[1:-1]:
    print s,'->',ord(s)-64
    v = v + ord(s)-64
  t = t + v * i
  i = i +1
print '\n\n***',t


