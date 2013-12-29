#!/usr/bin/python
#
# http://projecteuler.net/problem=54
#

from itertools import groupby

# convert face cards to numberics
def text_to_card_tup(card):
  ''' map card text to numerical values '''
  card_map = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 't':10, 'j':11, 'q':12, 'k':13, 'a':14}
  return (card_map[card[0]], card[1])

# gets card groups by card # size -> [[5,5,5],[4,4]]
def card_groups(hand):
  sorted_cards = sorted(hand)
  card_groups = [list(map(lambda c: c[0], grp)) for key,grp in groupby(sorted_cards,key=lambda c: c[0])]
  return sorted(card_groups, key=lambda grp: (-len(grp), -sum(grp)))

# straight & flush tests
def is_flush(hand):
  return len(set(map(lambda card: card[1], hand))) == 1

def is_straight(hand):
  ordered_cards = sorted(map(lambda c: c[0], hand))
  return ordered_cards == range(min(ordered_cards), max(ordered_cards)+1)

# total ordering on poker hands
def rank_hand(hand):
  crd_grp = card_groups(hand)
  if is_straight(hand) and is_flush(hand): return [10, crd_grp]
  if map(len, crd_grp) == [4,1]:           return [9, crd_grp]
  if map(len, crd_grp) == [3,2]:           return [8, crd_grp]
  if is_flush(hand):                       return [7, crd_grp]
  if is_straight(hand):                    return [6, crd_grp]
  if map(len, crd_grp) == [3,1,1]:         return [5, crd_grp]
  if map(len, crd_grp) == [2,2,1]:         return [4, crd_grp]
  if map(len, crd_grp) == [2,1,1,1]:       return [3, crd_grp]
  return [2, crd_grp]    

# read in the poker data
card_rows = [map(text_to_card_tup,line.lower().strip().split(' ')) for line in open('./poker.txt', 'r')]
all_two_hands = [[sorted(row[:5]), sorted(row[5:])] for row in card_rows]

wins = sum([rank_hand(hands[0]) > rank_hand(hands[1]) for hands in all_two_hands])
print '\nAnswer: {0}'.format(wins)
