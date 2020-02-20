#!/usr/bin/python
'''
PLAN:

  x) convert all roman numerals to real digits
  x) convert numbers to their ideal roman form
  x) char count everything
'''

import re


char_to_num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
num_to_char = {t[1]:t[0] for t in char_to_num.items()}

def is_positive(pair):
  ''' looks at a pair of adjacent roman numerals, decides is they should be interpreted as negative.  '''
  return pair[0] >= pair[1]


def roman_to_int(roman):
  ''' converts an arbitrary roman numeral to int '''
  int_vals = map(lambda c: char_to_num[c], roman)
  pairs    = zip(int_vals[:-1], int_vals[1:]) + [(int_vals[-1], 0)]
  return sum(map(lambda p: is_positive(p) and p[0] or -1 * p[0], pairs))


def replace_roman_chars(roman):
  ''' rules:
          Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
          I can only be placed before V and X.
          X can only be placed before L and C.
          C can only be placed before D and M.
  '''
  roman = re.sub(r'VIIII', r'IX', roman)
  roman = re.sub(r'IIII', r'IV', roman)

  roman = re.sub(r'LXXXX', r'XC', roman)
  roman = re.sub(r'XXXX', r'XL', roman)
  
  roman = re.sub(r'DCCCC', r'CM', roman)
  roman = re.sub(r'CCCC', r'CD', roman)

  return roman


def int_to_roman(i):
  # subtractively build out a verbose numeral
  dec, roman = i, ''
  for key in sorted(num_to_char)[::-1]:
    while dec >= key:
      dec, roman = dec - key, roman + num_to_char[key]
  # apply regex replacement rules
  return replace_roman_chars(roman)


def optimize_roman(roman):
  return int_to_roman(roman_to_int(roman))


# read in the numeral data
numerals  = [l.strip() for l in open(r'roman.txt','rb')]
optimized = map(optimize_roman, numerals)

print sum(map(len, numerals)) - sum(map(len, optimized))