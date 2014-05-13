#!/usr/bin/env python
'''  '''


import itertools


# read in word data file
words = sorted(set([l.strip()[1:-1] for l in open('words.txt', 'rb').read().split(',')]))


# group words into anagram sets
anagram_word_groups = []
for key, grp in itertools.groupby(sorted([(''.join(sorted(w)), w) for w in words]), lambda t: t[0]):
  grp = list(grp)
  if len(grp) > 1:
    anagram_word_groups.append([t[1] for t in grp])


# get anagram word pairs rather than anagram groups
anagram_pairs = []
for grp in anagram_word_groups:
  for pair in itertools.combinations(grp, 2):
    anagram_pairs.append(pair)


# square anagram tester
def all_possible_mappings(word0, word1, digits=tuple(range(9+1))):
  keys = sorted(set(word0))
  possible_char_permutation = itertools.permutations(digits, len(keys))
  for values in possible_char_permutation:
    mapping = {k:v for k, v in zip(keys, values)}
    # forbid leading 0s
    if mapping[word0[0]] and mapping[word1[0]]:
      yield mapping


def word_as_int(word, mapping):
  return int(''.join([str(mapping[c]) for c in word]))


def get_all_9_char_squares():
  ''' non-floating point method for getting square integers '''
  squares = []
  for i in itertools.count(1):
    sq = i**2
    if sq > 10**10:
      break
    squares.append(sq)
  return set(squares)


square_set = get_all_9_char_squares()



def words_are_square_anagram(word0, word1):
  '''
    try a bijective mapping from characters to digits
    test if word0 is a square
    test if word1 is a square
  '''
  assert tuple(sorted(word0)) == tuple(sorted(word1))

  for mapping in all_possible_mappings(word0, word1):
    if word_as_int(word0, mapping) in square_set:
      if word_as_int(word1, mapping) in square_set:
        yield max(word_as_int(word0, mapping), word_as_int(word1, mapping))

# main
largest_square_anagram = 0
for p in anagram_pairs:
  print p
  for square_anagram_int in words_are_square_anagram(p[0], p[1]):
    largest_square_anagram = max(largest_square_anagram, square_anagram_int)
    
print
print 'answer: {0}'.format(largest_square_anagram)
print

