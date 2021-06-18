a = [[5,6],
    [7,8]]
    

n = len(a)
m = len(a[0])

dup_a = []
for i in range(m):
    dup = []
    for j in range(n):
        dup.append(0)
    dup_a.append(dup)


k = n-1
for i in range(n):
    for j in range(m):
        dup_a[j][i] = a[k][j]
    k -= 1

a = dup_a
print(dup_a)
