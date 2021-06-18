'''mahi is the best man in the world'''
s = list(input().split())

slen = len(s)
new_list = []
for i in range(0,slen-1):
    for j in range(i+2,slen):
        lists = [s[i],s[j]]
        lists.sort()
        lists = " ".join(lists)
        new_list.append(lists)


new_list = list(set(new_list))
new_list.sort()
l = len(new_list)
if l:
    for i in range(len(new_list)):
        print(new_list[i])
else:
    print("No Combinations")
