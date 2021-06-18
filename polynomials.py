"""
input values
5
0 -2
3 6
4 7
1 -3
2 -1
"""

n = int(input())
dict_n = {}
for i in range(n):
    p,n = map(int,input().split())
    dict_n[p] = n
new_dict = {}
for i in sorted(dict_n.keys(),reverse = True):
    new_dict[i] = dict_n[i]

string = ""
first = True
for i in new_dict.keys():
    key = i
    value = new_dict[key]
    if(value == 0):
        string += ""
    elif(value < 0):
        if(value == -1):
            if first:
                if(key == 0):
                    string += "-" 
                else:
                    if(key == 0):
                        string += "-"  + "x"
                    else:
                        string += "-"  + "x^" + str(key)
                first = False
            else:
                if(key == 0):
                    string += " - " 
                else:
                    if(key == 1):
                        string += " - "  + "x"
                    else:
                        string += " - "  + "x^" + str(key)
                        ################
        else:
            if first:
                if(key == 0):
                    string += "-" + str(value * -1)
                else:
                    if(key == 0):
                        string += "-" + str(value * -1) + "x"
                    else:
                        string += "-" + str(value * -1) + "x^" + str(key)
                first = False
            else:
                if(key == 0):
                    string += " - " + str(value * -1)
                else:
                    if(key == 1):
                        string += " - " + str(value * -1) + "x"
                    else:
                        string += " - " + str(value * -1) + "x^" + str(key)
    else:
        if(value == 1):
            if first:
                if(key == 0):
                    string += str(value)
                else:
                    if(key == 1):
                        string += "x"
                    else:
                        string +=  "x^" + str(key)
                first = False
            else:
                if(key == 0):
                    string += " + " + str(value)
                else:
                    if(key == 1):
                        string += " + " + "x"
                    else:
                        string += " + " + "x^" + str(key)
        else:    
            if first:
                if(key == 0):
                    string += str(value)
                else:
                    if(key == 1):
                        string += str(value) + "x"
                    else:
                        string += str(value) + "x^" + str(key)
                first = False
            else:
                if(key == 0):
                    string += " + " + str(value)
                else:
                    if(key == 1):
                        string += " + " + str(value) + "x"
                    else:
                        string += " + " + str(value) + "x^" + str(key)

print(string)
