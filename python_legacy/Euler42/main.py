#!/usr/bin/python

import sys


def wordCharSum(word):
  return sum([ord(c)-96 for c in word])


def main ():
  """
  
  """
  
  # set up the triangel numbers
  tri = [int(1./2*n*(n+1)) for n in range(1,10000)]

  # pull down words in the file
  filename = 'words.txt'
  f = open(filename, 'r')
  text = f.read().replace('"','').lower()
  words = text.split(',')

  # get the char sum for each word
  wordSums = [wordCharSum(word) for word in words]

  members = 0
  for wordSum in wordSums:
    if wordSum in tri:
      members += 1
  print members

    
  pass

if __name__ == '__main__':
  main()
