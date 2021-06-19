'''
3 3
1 20 3
30 10 2
5 11 15

op:
1 2 3
5 10 11
15 20 30

0

0
'''

n,m = map(int,input().split())
#print(n,m)


matrix = []
for i in range(n):
    mat = list(map(int,input().split()))
    mat.sort()
    for j in mat:
        matrix.append(j)

matrix.sort()
k = 0
for i in range(n):
    mat = []
    for j in range(m):
        mat.append(str(matrix[k]))
        k = k+1
    print(" ".join(mat))

#print(matrix)
