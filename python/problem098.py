#!/usr/bin/python -tt
'''
plan:
  x) find all anagram pairs
  x) try all posible substitutions that result in double square (must be efficient)

'''

import csv
import collections
import itertools

AnagramPair = collections.namedtuple('AnagramPair', ['sorted_chars', 'word'])

# get a word hashset and sorted word list
word_set = set([l for l in csv.reader(open(r'./words.txt', 'rb'))][0])
words    = sorted(word_set)

#
pairs = sorted(AnagramPair(sorted(w), w) for w in words)

# grab just the sorted set of distinct words for all char equivalent word groups
word_grps   = [sorted(set([p.word for p in grp])) for key, grp in itertools.groupby(pairs, lambda p: p.sorted_chars)]

# remove non-anagram words
char_groups = filter(lambda grp: len(grp) > 1, word_grps)

# ensure all anagram groups are len == 2
anagram_pairs = sorted(itertools.chain(*map(lambda grp: list(itertools.combinations(grp, 2)), char_groups)))

# test print
for p in anagram_pairs:
  print p

# matching the sorted, uniq chars in a word pair against this list 
# will give all possible (char -> digit mappings)
all_digit_perms = list(itertools.permutations(range(10)))

# tool to generate all possible (char -> 0_9_digit) mappings
#   remember that there are no leading 0s.
def all_char_dig_mappings(pair):
  for seq in all_digit_perms:
    possible_char_map = {c:i for c,i in zip(sorted(set(pair[0])), seq)}
    if possible_char_map[pair[0]] != 0 and possible_char_map[pair[1]] != 0: # check for no leading zeros
      print possible_char_map
      yield possible_char_map


for d in all_char_dig_mappings(anagram_pairs[3]):
  print d