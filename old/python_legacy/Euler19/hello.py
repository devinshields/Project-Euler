from datetime import date

x=0
for year in range(1901,2001):
  for month in range(1,13):
    y = date.weekday(date(year, month, 1))
    print year,month,y
    if y == 6:
      x = x + 1
      print '       ',year,month,y,x

print x
