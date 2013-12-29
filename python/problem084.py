#!/usr/bin/python
#
# http://projecteuler.net/problem=84
#
# 0) count only the final square of each round
# 1) At the beginning of the game, the CC and CH cards are shuffled
#     a. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile
#     b. There are sixteen cards in each pile
# 2) if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

# Community Chest (2/16 cards):
#   Advance to GO
#   Go to JAIL
# Chance (10/16 cards):
#   Advance to GO
#   Go to JAIL
#   Go to C1
#   Go to E3
#   Go to H2
#   Go to R1
#   Go to next R (railway company)
#   Go to next R
#   Go to next U (utility company)
#   Go back 3 squares.
# --------------------

# Layers of state:
#                   1) position on the board
#                   2) number of consecutive doubles thrown while not in jail
#                   3) ordering of Chance & Comm. Chest cards


def main ():

  pass

if __name__ == '__main__':
  main()
