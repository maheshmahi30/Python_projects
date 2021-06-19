'''
"I am 25 years and 10 months old
op: sum of individual digits and avg
8
2.0
'''

string = input()
sum = 0
count = 0
for i in string:
    if(i.isdigit()):
        #print(i)
        sum = sum + int(i)
        count = count + 1
print(sum)
print(round((sum/count),2))
