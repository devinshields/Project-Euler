def Cat(filename):
  f = open(filename,'rU')
  lines = f.read()
  lines = lines.split('\n')
  d = []
  for line in lines[0:-1]:
    x = line.split(' ')
    y = []
    for i in x:
      y.append(int(i))
    d.append(y)
  return d

def get_rightof(i,j,d):
  try:
    return d[i][j]*d[i][j+1]*d[i][j+2]*d[i][j+3]
  except:
    return 0

def get_downof(i,j,d):
  try:
    return d[i][j]*d[i+1][j]*d[i+2][j]*d[i+3][j]
  except:
    return 0

def get_rightdiag(i,j,d):
  try:
    return d[i][j]*d[i+1][j+1]*d[i+2][j+2]*d[i+3][j+3]
  except:
    return 0

def get_leftdiag(i,j,d):
  try:
    return d[i][j]*d[i+1][j-1]*d[i+2][j-2]*d[i+3][j-3]
  except:
    return 0




def main():
  d = Cat('data.txt')

  print d

  ot = []
  for i in range(0,len(d)):
    for j in range(0,len(d[0])):
      ot.append(get_rightof(i,j,d))
      ot.append(get_downof(i,j,d))
      ot.append(get_rightdiag(i,j,d))
      ot.append(get_leftdiag(i,j,d))
  print max(ot)



main()
