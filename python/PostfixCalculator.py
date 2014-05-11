#!/usr/bin/env python


from operator import add, sub, mul, div


class PostfixCalculator(object):
  ''' implementes the RPN calculator described here:
          http://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_algorithm
  '''
  def __init__(self, allowed_digits=tuple(range(1, 10)), allowed_functions=(add, sub, mul, div)):
    self.symbol_stream     = []
    self.stack             = []

    self.allowed_digits    = allowed_digits
    self.allowed_functions = allowed_functions
    self.calc_results      = None

  @property
  def report(self):
    return u'postfix report:\t\t{0}   ===>>>   {1}'.format(self.symbol_stream, self.calc_results)

  def read_symbols_and_run_calculator(self, symbol_stream):
    # ensure the calculator is empty before use
    self.symbol_stream, self.stack = [], []

    # capture the input stream
    self.symbol_stream = list(symbol_stream)

    # start symbol parsing and calculation
    for s in symbol_stream:
      if s in self.allowed_digits:
        self.stack.append(s)
      elif s in self.allowed_functions:
        in0, in1  = self.stack.pop(), self.stack.pop()
        # with integer division, do a modulus check. requires an exact match to work.
        if s == div and in0 % in1:
          raise u'imperfect integer division'
        # run the calculation, store the result
        self.stack.append(s(in0, in1))
      else:
        raise u'unexpected symbol (non-digit and non-function) sent to the the PostfixCalculator'
    
    self.calc_results = self.stack.pop()

    if len(self.stack):
      print
      print self.stack
      print
      raise u'too many values left in the PostFix stack'

    if not isinstance( self.calc_results, int):
      raise u'output is not integer'

    return self


def test_calculator():
  '''  '''
  print

  print PostfixCalculator().read_symbols_and_run_calculator(symbol_stream=[1, 5, add]).report

  print

if __name__ == '__main__':
    test_calculator()
