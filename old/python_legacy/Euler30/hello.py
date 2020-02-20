from math import pow 

def pow5sum(n):
  t=0
  for i in str(n):
    t += pow(int(i),5)
  return t


def main():
  t = 0 
  for i in range(2,int(pow(10,6))):
    if i == pow5sum(i):
      t += i
  print t


main()

#http://primes.utm.edu/glossary/xpage/Tau.html
