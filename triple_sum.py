"""
0 1 2 3 5 7 13 17 19 19
50

0 1 2 3 5 7 13 17 19 19
29

13 13 13 13 13
39
"""

s = list(map(int,input().split()))
n = int(input())
new_order = []
for i in range(len(s)):
    a = s[i]
    for j in range(i+1,len(s)):
        new_list = []
        b = s[j]
        c = n - (a+b)
        if(c in s):
            new_list.append(a)
            new_list.append(b)
            new_list.append(c)
            new_list.sort()
            new_order.append(new_list)

newest_order = []

for line in new_order:
    if(line not in newest_order):
        newest_order.append(line)

newest_order.sort()
l = len(newest_order)
if l:
    for line in newest_order:
        line = tuple(line)
        print(line)
else:
    print("No Matching Triplets Found")
