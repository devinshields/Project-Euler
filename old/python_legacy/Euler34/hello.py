from math import factorial

def digit_fac_sum(n):
  s = str(n)
  t=0
  for i in s:
    t = t + factorial(int(i))
  return t

def main():
  t=0
  for i in range(3,1000000):
    if i == digit_fac_sum(i):
      t = t+i
  print '\n*** ',t

main()


