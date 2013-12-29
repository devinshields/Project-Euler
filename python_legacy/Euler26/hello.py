import re

prec = 20000
rng = 1000
def decimal_expansion(a, b):
  (q,r) = (a/b, a%b)
  s1 = str(q)
  l2 = []
  for i in range(prec):
    a = r * 10
    q = a/b
    r = a%b
    l2.append(q)
    if r == 0:
      break
  s2 = ''.join([str(x) for x in l2])
  return s2

max_i = 1
max_len = 1

r = re.compile(r"(.+?)\1+")    
for i in range(1,rng):
  s = decimal_expansion(1, i)
  res = r.findall(s)
  if res:
    z = sorted(res,key=len)[-1]

    if len(z)>max_len:
      max_len = len(z)
      max_i = i
      print i, len(z), z,'\n'


print '\n\n***\n' , max_i, max_len






