def is_pal(s):
  for i in range(0,len(s)/2):
    if not s[i] == s[len(s)-i-1]:
     return False
  return True

def main():
  t=0
  for i in xrange(1,1000000):
    if is_pal(bin(i)[2:]) and is_pal(str(i)):
      t = t + i
  print t
main()


