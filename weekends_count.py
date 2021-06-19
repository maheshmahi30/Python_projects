from datetime import datetime,timedelta
week = {"Mon":1,"Tue":2,"Wed":3,"Thr":4,"Fri":5,"Sat":6,"Sun":7}

input1 = input()
input2 = input()

dt1 = datetime.strptime(input1,"%d %b %Y")
'''
4 Dec 2020
1 Jan 2021
op:
Saturday: 4
Sunday: 4

25 Jan 2021
14 Feb 2021
op:
Saturday: 3
Sunday: 3

25 May 2019
22 Dec 2021
op:
Saturday: 135
Sunday: 135
'''


dt2 = datetime.strptime(input2,"%d %b %Y")

day1 = dt1.strftime("%a")
day2 = dt2.strftime("%a")
day1 = str(day1)
sub_val = week[day1]
#print(day1,day2)

gap_date = dt2 - dt1
#print(str(gap_date))
gap_date = str(gap_date)
#print(gap_date)
    
days_index = gap_date.find(" day")

days = int(gap_date[:days_index])
days = days + sub_val
days = days//7
if(day2 == "Sat"):
    print("Saturday: {}".format(days+1))
    print("Sunday: {}".format(days))
elif(day2 >= "Sun" or day2 <= "Sun"):
    print("Saturday: {}".format(days))
    print("Sunday: {}".format(days))

#print(days)
