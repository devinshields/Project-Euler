#!/usr/bin/python


# quickly get the first and last two digits
def first2(n):
  while n > 100:
    n /= 10
  return n

def last2(n):
  return n % 100

# used to get polygonal numbers
def get_below(max_val, fn):
  ind,val = 0,0
  while fn(ind) < max_val:
    ind += 1
  return filter(lambda i: len(str(i)) >= 4, [fn(i) for i in range(1,ind)])


# get the polynomial nums for a given num_tup_list
def get_polys(num_tup_list):
  return [num_tup[0] for num_tup in num_tup_list]

def main():

  mat,max_val = {},10**4

  # fill in a matrix with the polynomial tuples
  mat[3] = [(3, num) for num in get_below(max_val, lambda n: n*(n+1)/2)]
  mat[4] = [(4, num) for num in get_below(max_val, lambda n: n**2)]
  mat[5] = [(5, num) for num in get_below(max_val, lambda n: n*(3*n-1)/2)]
  mat[6] = [(6, num) for num in get_below(max_val, lambda n: n*(2*n-1))]
  mat[7] = [(7, num) for num in get_below(max_val, lambda n: n*(5*n-3)/2)]
  mat[8] = [(8, num) for num in get_below(max_val, lambda n: n*(3*n-2))]

  # seed with the octagonal numbers
  cur_tup_list = []
  next_tup_list = [[tup_list] for tup_list in mat[8]]
  
  for itr in range(2,7):
    cur_tup_list = next_tup_list
    next_tup_list = []
    for cand_tup_list in cur_tup_list:
      last_tup = cand_tup_list[-1]
      covered_polys = get_polys(cand_tup_list)

      # loop through the uncovered polys
      for poly in [poly for poly in range(3, 8+1) if poly not in covered_polys]:
        possible_next_tups = filter(lambda tup: last2(last_tup[1]) == first2(tup[1]), mat[poly])
        for tup in possible_next_tups:
          next_tup_list.append(cand_tup_list + [tup])
  
  # next_tup_list now has 6 members
  for cand in next_tup_list:
    if first2(cand[0][1]) == last2(cand[-1][1]):
      print '\nAnswer: {0}'.format(sum(map(lambda tup: tup[1], cand)))

if __name__ == '__main__':
  main()
