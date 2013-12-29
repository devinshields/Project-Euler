#!/usr/bin/python

import itertools
import urllib2

# -------------- Prior Info -------------------------------------
# pull down text data from the web, read it into a list of ints
fin = urllib2.urlopen('http://projecteuler.net/project/cipher1.txt')
encoded_chars = map(int, fin.read().strip().split(','))

# keys must be lowercase ascii letters
valid_key_chars = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]

# so all possible key sets are:
possible_keys = list(itertools.permutations(valid_key_chars, 3))

# most common words in english. use whitespace bounded words to aviod false positives
#   http://en.wikipedia.org/wiki/Most_common_words_in_English
common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have']
search_phrases = [' {0} '.format(w) for w in common_words]

# -------------- Logic --------------------------------------------------
def decode(key, encoded_chars):
  int_keys = map(ord, key)
  key_sequence = itertools.cycle(int_keys)
  int_pairs = zip(encoded_chars, key_sequence)
  decoded = ''.join([chr(t[0] ^ t[1]) for t in int_pairs])
  return decoded

# try each key set and sum the occurances of all search pharses
key_decoded = ((key, decode(key, encoded_chars)) for key in possible_keys)
count_key_decoded = ((sum(t[1].count(p) for p in search_phrases), t[0], t[1]) for t in key_decoded)

# try all possible keys and get the best one
best_match = sorted(filter(lambda t: t[0], count_key_decoded), key=lambda t: -t[0])[0]
decoded_text = best_match[2]

# get the numeric answer
decoded_ascii_int_sum = sum(ord(i) for i in decoded_text)
print '\nAnswer: {0}'.format(decoded_ascii_int_sum)