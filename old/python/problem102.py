#!/usr/bin/python -tt
#
# problem 102: http://projecteuler.net/problem=102
#
def p_in_p(x, y, poly):
  '''
  function sourced from: http://www.ariel.com.au/a/python-point-int-poly.html
  '''
  n = len(poly)
  inside =False
  p1x,p1y = poly[0]
  for i in range(n+1):
    p2x,p2y = poly[i % n]
    if y > min(p1y,p2y):
      if y <= max(p1y,p2y):
        if x <= max(p1x,p2x):
          if p1y != p2y:
            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
          if p1x == p2x or x <= xinters:
            inside = not inside
    p1x,p1y = p2x,p2y
  return inside

# my code
rows = [map(float, l.strip().split(',')) for l in open('triangles.txt', 'r')]
points = [((r[0], r[1]), (r[2], r[3]), (r[4], r[5])) for r in rows]

res = filter(lambda p: p_in_p(0,0,p), points)
print '\nAnswer: {0}'.format(len(res))
