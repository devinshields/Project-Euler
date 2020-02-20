def Cat(filename):
  f = open(filename,'rU')
  lines = f.readlines()
  return lines

def row_sum(a,b):
  for i in range(0,len(a)):
    if b[i] > b[i+1]:
      a[i] = a[i] + b[i]
    else:
      a[i] = a[i] + b[i+1]
  return a

def tri_max(row_num,py):
  if row_num == len(py)-1:
    return py[-1]
  return row_sum(py[row_num],tri_max(row_num + 1,py))

lines = Cat('data.txt')
py = []
for line in lines:
  nums = line[0:-1].split(' ')
  nu_line = []
  for num in nums:
    nu_line.append(int(num))
  py.append(nu_line)

print tri_max(13,py)
