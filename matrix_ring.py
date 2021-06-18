"""
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
a = [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
"""

n,m = map(int,input().split())
a = []
for i in range(n):
    mat = list(map(int,input().split()))
    a.append(mat)

count = int(input())

for k in range(count):
    a_len = len(a)
    top = 0
    right = a_len
    bottom = a_len-1
    left = 0
    #top line
    while(bottom > top and right > left):
        prev = a[top+1][top]
        for i in range(top,right):
            cur = a[top][i]
            a[top][i] = prev
            prev = cur
        #right line
        for i in range(top+1,right):
            cur = a[i][right-1]
            a[i][right-1] = prev
            prev = cur
        #bottom line
        for i in range(bottom-1,top-1,-1):
            cur = a[bottom][i]
            a[bottom][i] = prev
            prev = cur
        #left line
        for i in range(bottom-1,top,-1):
            cur = a[i][left]
            a[i][left] = prev
            prev = cur
        
        top += 1
        right -= 1
        bottom -= 1
        left += 1


for i in a:
    s = ""
    for j in i:
        s += str(j) + " "
    print(s)
