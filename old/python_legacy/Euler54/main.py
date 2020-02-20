#!/usr/bin/python -tt
import sys
from sets import Set

def get_data():
  return open('poker_small.txt','rU').readlines()

def convert_card(c):
  try:
    return int(c[0])
  except:
    if c[0] == 'T':return 10
    if c[0] == 'J':return 11
    if c[0] == 'Q':return 12
    if c[0] == 'K':return 13
    if c[0] == 'A':return 14

# card # and hand ranking helpers
def card_rank(c):
  return -c[0]

def ord_rank(m):
  return (-m[1],-m[0])

def card_ord(h):
  return sorted(map_hand(h).items(),key=ord_rank)

# data cleaners
def make_hand(h):
  hand = []
  for c in h:
    hand.append((convert_card(c),c[1]))
  return sorted(hand,key=card_rank)

def map_hand(h):
  d = {}
  for i in h:
    c = i[0]
    if c in d:d[c] += 1
    else:d[c] = 1
  return d

# hand ranking helpers
def is_straight(h):
  return [card_rank(c) for c in h] == range(-h[0][0],-h[0][0]+5)

def is_flush(h):

  return len(Set([i[1] for i in h])) == 1

def is_4ofkind(h):
  d = map_hand(h)
  return max(d.values()) == 4

def is_fullhouse(h):
  d = map_hand(h)
  return d.values() == [3,2]

def is_3ofkind(h):
  d = map_hand(h)
  sorted(d.values())
  return d.values()[0] == 3

def is_2pair(h):
  d = map_hand(h)
  print sorted(d.values())
  return d.values() == [2,2,1]

def is_pair(h):
  d = map_hand(h)
  print d.values()
  return d.values() == [2,1,1,1]

# main reduction tool
def hand_reduce(h):
  s = 10

  if is_straight(h) and is_flush(h):return [s,card_ord(h)]
  s -= 1

  if is_4ofkind(h):return [s,card_ord(h)]
  s -= 1

  if is_fullhouse(h):return [s,card_ord(h)]
  s -= 1

  if is_3ofkind(h):return [s,card_ord(h)]
  s -= 1

  if is_2pair(h):return [s,card_ord(h)]
  s -= 1

  if is_pair(h):return [s,card_ord(h)]
  s -= 1

  return [s,card_ord(h)]


def main():
  d = get_data()
  cells = [i[:-1].split(' ') for i in d]
  p1_wins = 0

  for i in cells:
    
    h1 = make_hand(i[0:5])
    h2 = make_hand(i[5:])
    
#    p1_wins += hand_reduce(h1)>hand_reduce(h2)

    print h1,'  ||  ',h2
    print hand_reduce(h1),'  ||  ',hand_reduce(h2)
    print '\n'

  print p1_wins

    
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

