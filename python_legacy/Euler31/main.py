#!/usr/bin/python




def main ():

  glCoinList = (1,2,5,10,20,50,100,200)
  coinsTupleList = set(tuple([-1,1]))
  
  for coinTuple in coinsTupleList:
    s = sum(coinTuple) 
    if s == 5:
      print 'Huzza!'
    else:
      possibleCoins = [coin for coin in glCoinList if s-coin >= 0]
      for coin in possibleCoins:
        coinList = list(coinTuple)
        coinList.append(coin)
        coinsTupleList.add(tuple(sorted(coinList)))
  for i in coinsTupleList:
    print i
      
  
  pass

if __name__ == '__main__':
  main()





"""
  if s == 10:
    print s,coins
    return
  outputTupleSet = set()
  possibleCoins = [c for c in glCoinList if (10-s-c) >= 0]
  for coin in possibleCoins:
    coinList = list(coins)
    coinList.append(coin)
    outputTupleSet.add(tuple(sorted(coinList)))
"""
