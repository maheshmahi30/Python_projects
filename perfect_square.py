'''
4
16
op:
4

5
8
op:
No Perfect Square
'''

import math
n = int(input())
m = int(input())

for i in range(n,m+1):
    j = math.sqrt(i)
    j = round(j)
    #print(j)
    j = j**2
    if(i == j):
        print(i)
        break
else:
    print("No Perfect Square")
