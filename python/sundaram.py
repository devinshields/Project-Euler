#!/usr/bin/python

def sundaram(max_n):
  ''' http://en.wikipedia.org/wiki/Sieve_of_Sundaram '''
  numbers = range(3, max_n+1, 2)
  half = (max_n)//2
  initial = 4

  for step in xrange(3, max_n+1, 2):
    for i in xrange(initial, half, step):
        numbers[i-1] = 0
    initial += 2*(step+1)

    if initial > half:
      return [2] + filter(None, numbers)


if __name__ == '__main__':
  main()
