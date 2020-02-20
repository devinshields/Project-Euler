#!/usr/bin/python -tt
#
# problem 31: http://projecteuler.net/problem=31
#

def main():

  # get a set of sets, seeding with each unique coin
  coins = set([1, 2, 5, 10, 20, 50, 100])
  coin_combos = set([tuple([coin]) for coin in coins])
  final_combos = set([(200)])

  # while the list has any (not sum(_) == 200), keep executing the branch-search loop
  while len(coin_combos):
    # some debug printing
    print 'len(final_combos):',len(final_combos)
    print 'len(coin_combos) :',len(coin_combos)
    print
    # append one coin to each of the sub-200 combos
    possible_combos = []
    for combo in coin_combos:
      for coin in coins:
        c = list(combo)
        c.append(coin)
        if sum(c) == 200:
          final_combos |= set([tuple(sorted(c))])
        elif sum(c) < 200:
          possible_combos.append(tuple(sorted(c)))
    
    # close the loop
    coin_combos = set(possible_combos)

  print '\nAnswer:',len(final_combos)
  
  pass

if __name__ == '__main__':
  main()