#!/usr/bin/python

import sys

space = ''

smallDigits = {
               0:'',
               1:'one',
               2:'two',
               3:'three',
               4:'four',
               5:'five',
               6:'six',
               7:'seven',
               8:'eight',
               9:'nine',
               10:'ten',
               11:'eleven',
               12:'twelve',
               13:'thirteen',
               14:'fourteen',
               15:'fifteen',
               16:'sixteen',
               17:'seventeen',
               18:'eighteen',
               19:'nineteen',
               20:''
               }
tensNames = {
              2:'twenty',
              3:'thirty',
              4:'forty',
              5:'fifty',
              6:'sixty',
              7:'seventy',
              8:'eighty',
              9:'ninety'
            }               

def getWordsForNumber(num):
  
  if num == 1000:
    return space.join(['one','thousand'])

  hundreds = (num - num % 100)/100
  tens = (num - num % 10)/10

  # recurse when greater than 100
  if hundreds > 0:
  
    smallNum = getWordsForNumber(num % 100)
    if smallNum:
      smallNum = space.join(['and',smallNum])

    return space.join([getWordsForNumber(hundreds),'hundred',smallNum])
  
  # take care of the teens
  if tens < 2:
    return smallDigits[num]

  # the 20s & above
  return space.join([tensNames[tens],getWordsForNumber(num-tens*10)])

  
def main ():
  
  maxNum = 1001

  for i in range(1,maxNum):
    print getWordsForNumber(i)
  
  
  pass

if __name__ == '__main__':
  main()
