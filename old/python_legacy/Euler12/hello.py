from math import sqrt
def factors(n):  
    fact=[1,n]  
    check=2  
    rootn=sqrt(n)  
    while check<rootn:  
        if n%check==0:  
            fact.append(check)  
            fact.append(n/check)  
        check+=1  
    if rootn==check:  
        fact.append(check)  
        fact.sort()
    return fact

def main():
  (t,i,num) = (0,1,0)
  while t < 500:
    num = num + i
    t = get_numdivs(num)
    print i,num,'->',t
    i = i+1
  print num,'->',t
  
main()

#http://primes.utm.edu/glossary/xpage/Tau.html
