#!/usr/bin/python

import itertools
import re

# generate all possible keys
possible_keys = [''.join(p) for p in itertools.permutations(map(str, range(10)), 8)]

# fetch the 3-char samples
char_tups = [tuple(line.strip()) for line in open('keylog2.txt','r')]

# for each sample, create a regex and use it to filter the possible keys
# will take 50 * 10^n tests for a full filter
for tup in char_tups:
  regex = '.*{0}.*{1}.*{2}.*'.format(*tup)
  possible_keys = filter(lambda key: re.match(regex, key), possible_keys)

for key in sorted(possible_keys, key=len):
  print 'possible answer:', key
