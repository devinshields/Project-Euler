from math import pow

def main():

  a = range(2,100+1)
  b = range(2,100+1)
  x = set()

  for i in a:
    for j in b:
      z = int(pow(i,j))
      x.add(z)
  print len(x)
main()


