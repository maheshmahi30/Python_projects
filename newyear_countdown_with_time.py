"""
Dec 31 2020 11:43 PM
op:0 hours 17 minutes

Dec 30 2020 02:43 PM
op:33 hours 17 minutes

Jan 31 2020 04:43 AM
op:8059 hours 17 minutes
"""
from datetime import datetime,timedelta
input_date = input()
#print(input_date)
old_date = datetime.strptime(input_date,"%b %d %Y %I:%M %p")
#print(old_date)
new_date = datetime(2021,1,1,0,0)
#print(new_date)
dt_time = new_date - old_date
#print(dt_time)
dt_time = str(dt_time)
index = dt_time.find(" day")
#print(index)
if(index != -1):
    len_date = len(" day")
    days = dt_time[:index]
else:
    days = ""
#print("days",days)
index = dt_time.find(", ")
rem_time = dt_time[index+2:]
#print(rem_time)
index = rem_time.find(":")
hr = rem_time[0:index]
if(hr.find(":") != -1):
    hr = hr[:-1]
#print(hr)
min_ = rem_time[index:index+3]
#print(min_)
if(min_.find(":") != -1):
    if(min_[0] == ":"):
        min_ = min_[1:]
    else:
        min_ = min_[:-1]
if(len(hr)):
    hr = int(hr)
if(len(min_)):
    min_ = int(min_)
if(len(days)):
    days = int(days)
len_date = len(" day")
#print(days,hr,min_)
hours = hr + (days*24)
if(hours == ""):
    hours = "0"
print("{} hours {} minutes".format(hours,min_))
