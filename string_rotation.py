"""
Python
onpyth
o/p: 2

python
python
o/p:0

python
learning
o/p:no match
"""



"""str1 = input()
str2 = input()
cut = str1[0:2]
index = str2.find(cut)

if(index != -1):
    new = str2[index:] + str2[0:index]
    #print(new)
    
    if(str1 == new):
        print(index)
    else:
        print("No Match")
else:
    print("No Match")
 """   
#################### try new method with for loop slicing and compare string
str1 = input()
str2 = input()

len_s2 = len(str2)

for i in range(len_s2):
    new = str2[i:] + str2[0:i]
    if(new == str1):
        print(i)
        break
else:
    print("No Match")














