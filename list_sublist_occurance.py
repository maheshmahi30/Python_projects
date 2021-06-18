input_list = ['orange', 'mango', 'apple', 'orange', 'mango', 'apple',['orange', 'mango', 'apple','orange', 'mango', 'apple',['orange', 'mango', 'apple',],'apple', 'orange', 'mango', 'apple'],'orange', 'mango', 'apple']

new_list = []

#print(type(input_list) == "<class 'list'>")

def islist(input):
    for item in input:
        if(type(item) == type(input)):
            #print(item)
            islist(item)
            
        else:
            new_list.append(item)
           
        
islist(input_list)
print(new_list)

dict_a = dict()
list_a = list(set(new_list))

for i in list_a:
    count = 0
    for j in new_list:
        if(i == j):
            count = count +1
            dict_a[i] = count

print(dict_a)
