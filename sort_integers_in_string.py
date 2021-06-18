'''hi iam5 years 11months 4 weeks -6 days old'''


a = input().split()
print(a)
num_list = []
char_list = []

for i in a:
    num = ""
    char = ""
    if(i.isdigit()):
        num_list.append(int(i))
        char_list.append("0")
        char_list.append(" ")
    else:
        for c in i:
            if c.isdigit():
                if char != "":
                    char_list.append(char)
                    char=""
                num += c
            else:
                if num != "":
                    num_list.append(int(num))
                    char_list.append("0")
                    num = ""
                char += c
    if(num != "") and (char == ""):
        num_list.append(int(num))
        char_list.append("0")
        char_list.append(" ")
    if( num =="") and (char != ""):
        char_list.append(char+" ")
    if(num!="") and (char !=""):
        print("malli")
    
num_list.sort(reverse = True)
result = ""
count = 0

for i in char_list:
    if i.isdigit():
        result += str(num_list[count])
        count += 1
    else:
        result += i

print(result)
