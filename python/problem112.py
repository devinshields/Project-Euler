#!/usr/bin/python -tt
'''
    problem 112: http://projecteuler.net/problem=112
'''


import itertools

def is_bouncy(x):
  if x < 100:
    return False
  s   = list(str(x))
  srt = sorted(s)
  return not (s == srt or s == srt[::-1])

assert not is_bouncy(134468)
assert not is_bouncy(66420)
assert is_bouncy(155349)

bouncy_count = 0.
for n in itertools.count(1):
  bouncy_count += is_bouncy(n)
  #print is_bouncy(n), bouncy_count, n, bouncy_count/n
  ratio = bouncy_count/n
  if ratio >= .99:
    print 'Answer: {0}'.format(n)
    break

