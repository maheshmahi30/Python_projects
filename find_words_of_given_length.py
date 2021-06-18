'''
find the length of the words
this is not corrects
5
'''

string_list = list(map(str,input().split()))
num = int(input())
new_list = []

count = len(string_list)
for i in range(count):
    item1 = string_list[i]
    length1 = len(item1)
    if(length1 == num):
        new_list.append(item1)
        continue
    else:
        need = num - length1
        if(need > 0):
            j = 1
            for item in string_list:
                if(j == i):
                    break
                else:
                    string = []
                    length2 = len(item)
                    if(length2 == need):
                        item2 = item
                        string.append(item1)
                        string.append(item2)
                        j +=1
                        n_string = "".join(string)
                        new_list.append(n_string)

new_list = set(new_list)
new_list = list(new_list)
new_list.sort()
for item in new_list:
    print(item)
