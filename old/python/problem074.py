#!/usr/bin/python

from Euler import factorial

def sdf(n):
  """sum_of_digit_factorials"""
  return sum(map(factorial,map(int,str(n))))

def get_cycle_length(n, num_list=[]):
  if not num_list: num_list = [n]
  n_next = sdf(n)
  if n_next in num_list: return 1
  num_list.append(n_next)
  return get_cycle_length(n_next, num_list)+1

def main ():
   
  total = 0
  for i in range(1,10**6):
    if get_cycle_length(i) == 60:
      total += 1
  print '\nAnswer: {0}'.format(total)
  pass

if __name__ == '__main__':
  main()
