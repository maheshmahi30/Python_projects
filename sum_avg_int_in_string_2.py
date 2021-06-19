'''
"I am 25 years and 10 months old
op: sum of int and avg
35
17.5


Anjali25 is python4 Expert
1time3 %times4
'''
"""
string = input().split()
sum = 0
count = 0
for i in string:
    if(i.isdigit()):
        #print(i)
        sum = sum + int(i)
        count = count + 1
print(sum)
print(round((sum/count),2))
"""
#################################try with split each item and loop to find the integer in the string if the 
## string has an integer and continuos with a string or a space then the integer is considered
string = input().split()
sum = 0
count = 0


def isdigit_fun(word):
    digit = 0
    for c in word:
        if(c.isdigit()):
            digit = digit*10 + int(c)
    return digit


#print(string)
digi_list = []
for word in string:
    digit = isdigit_fun(word)
    if(digit != 0):
        digi_list.append(digit)
#print(digi_list)

count = len(digi_list)

for i in digi_list:
    sum = sum + i
print(sum)
print(sum/count)















