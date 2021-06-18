'''
7
0 2
1 3
2 1
5 0
3 6
4 7
6 -9
5
0 1
2 4
3 0
1 0
4 -5
'''



n = int(input())
dict_n = dict()
for i in range(0,n):
    power,coeff = map(int,input().split())
    #print(power,coeff)
    dict_n[power]  = coeff

m = int(input())
dict_m = dict()
for i in range(0,m):
    power,coeff = map(int,input().split())
    #print(power,coeff)
    dict_m[power]  = coeff
################################
if(len(dict_n) > len(dict_m)):
    dic_len = len(dict_n) 
else:
    dic_len = len(dict_m)
#print(dic_len)
################################
dic_new = dict()
for i in range(0,dic_len):
    if(i >= len(dict_m)):
        dict_m[i] = 0
    if(i >= len(dict_n)):
        dict_n[i] = 0
    dic_new[i] = dict_n[i] + dict_m[i]
#print(dic_new)
###############################
keys_list = []
for i in sorted(dic_new.keys(),reverse = True):
    keys_list.append(i)
#print(keys_list)
###############################
new_string = ""
poly_list = []
for i in keys_list:
    coeff = dic_new[i]
    power = i
    if(power == 0):
        if(coeff == 0):
            pass
        elif (coeff == 1):
            poly = coeff
            poly_list.append(poly)
        else:
            poly = str(coeff)
            poly_list.append(poly)
    elif(power == 1):
        if(coeff == 0):
            pass
        elif (coeff == 1):
            poly = "x"
            poly_list.append(poly)
        elif(coeff == -1):
            poly = "-" + "x"
            poly_list.append(poly)
        else:
            poly = str(coeff) + "x"
            poly_list.append(poly)
    else:
        if(coeff == 0):
            pass
        elif (coeff == 1):
            poly = "x^" + str(power)
            poly_list.append(poly)
        elif(coeff == -1):
            poly = "-" + "x^" + str(power)
            poly_list.append(poly)
        else:
            poly = str(coeff) + "x^" + str(power)
            poly_list.append(poly)
        
#####################################

def findnegative(polynomial):
    index = polynomial.find("+ -")
    len_index = len("+ -")
    end_index = index + len_index
    polynomial = polynomial[:index] + "- "  + polynomial[end_index:]
    
    index = polynomial.find("+ -")
    if(index == -1):
        print(polynomial)
    else:
        findnegative(polynomial)
##########################################

#print(poly_list)
length_of_list = len(poly_list)
if(length_of_list == 0):
    print(0)
else:
    polynomial = " + ".join(poly_list)
    index = polynomial.find("-")
    #print(polynomial)
    if(index != -1 and index != 0):
        findnegative(polynomial)
    else:
        print(polynomial)
