#!/usr/bin/python -tt
'''http://projecteuler.net/problem=151'''


import random

random.seed(42)


class Envelope(object):
  ''' holds info about which paper slices remain in an batch
      has methods for randomly updating a batch and for running a complete simulation.
      note: I represent 'A1' as 16 and A5 as 1'''
  def __init__(self):
    self.slices = [16]
    self.slice_mapper = d = {1:[], 2:[1], 4:[2, 1], 8:[4, 2, 1], 16:[8, 4, 2, 1]}
    pass
  def update_random_slice(self):
    # pop a random element and update the envelope
    selected = self.slices.pop(random.randrange(len(self.slices)))
    self.slices += self.slice_mapper[selected]
  def run_slicing_simulation(self):
    single_slice_count = 0
    while self.slices:
      self.update_random_slice()
      if sum(self.slices) > 1 and len(self.slices) == 1:
        single_slice_count += 1
    return single_slice_count


def mean(lst):
  return sum(lst)/float(len(lst))


print 'hello sim!'
res = [Envelope().run_slicing_simulation() for i in range(10**4)]
print mean(res)
print 'goodbye sim!'



import joblib