#!/usr/bin/python -tt
'''
problem 104:        http://projecteuler.net/problem=104
cheating from :-( : http://blog.dreamshire.com/2009/06/04/project-euler-problem-104-solution/
NOTE: my call to str(int(fin(n))) turned out to grow linearly as the string representing fib(n) gre
      so I cheated. the implementation below use a closed for calculation to get the top 10 digits
      and a %10**9 truncated calculation for the lower 10 digits. Very clever.
'''

from euler import is_pandigital
 
def top_digits(n):
  ''' Use: http://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
      to calculate an aproximation of the Nth Fibonacci number. For the top
      digits, the approximation is good enough.
  '''
  t = n * 0.20898764024997873 + (-0.3494850021680094)
  return int(10**(t - int(t) + 8))
 
n, f0, f1 = 2, 1, 1
while not is_pandigital(f1) or not is_pandigital(top_digits(n)):
 f0, f1 = f1, (f1+f0)%10**9
 n += 1
print "Answer to PE104 = ", n