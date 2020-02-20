
def pascals(myrange):
    triangle = [[1]]
    for x in range(1, myrange):
        temp = [1]
        for n in range(0, x-1):
            temp.append(triangle[x-1][n]+triangle[x-1][n+1])
        temp.append(1)
        triangle.append(temp)
    return triangle
            
def menu():
    x = pascals(int(raw_input('how many rows? ')))
    print x[-1][len(x[-1])/2]

print 'This program makes pascal\'s triangle up to a given amount of rows.\n'

def main():
  menu()

main()
