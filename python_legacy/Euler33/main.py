#!/usr/bin/python -tt
 
def main():
  fracs = []
  for i in range(10,100):
    for j in range(i,100):
      
      if str(i)[1] == '0':continue
      if str(j)[1] == '0':continue
      if i == j:continue


      # get the actual fraction 
      frac = float(i)/float(j)

      # if the digits match
      if str(i)[1] == str(j)[0]:
        # and it cancels numerically 
        if float(str(i)[0])/int(str(j)[1]) == frac:
          fracs.append(frac)
          
  print reduce(lambda x,y:x*y,fracs,1)


if __name__ == '__main__':
  main()
