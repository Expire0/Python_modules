#!/usr/bin/env python3

###convert unix team to human readable time. This works if the unix time is in milliseconds. 

import datetime 


time = input("Enter the Cyclone event time to be converted: ")

#convert to seconds 
fix = int(time) / 1000

value = datetime.datetime.fromtimestamp(fix)

print(value.strftime('%Y-%m-%d %H:%M:%S'))



from datetime import datetime,timedelta

date = datetime.now()
test = "2019/08/29 12:13:00"


## prototyping two ways to convert a standard human readable time to unix time in milliseconds.

#This way uses input from the user
def range(time):
    starttime = datetime.strptime(time, "%Y/%m/%d %H:%M:%S") - timedelta(hours = 1)
    roundback = starttime.replace(minute=0,second=0,microsecond=0)
    current = datetime.strptime(time, "%Y/%m/%d %H:%M:%S").replace(minute=0,second=0,microsecond=0)
    return roundback, current



#print(int(range(date).strftime('%s')))
print("Start time in unix milliseconds time " + str(int(range(test)[0].strftime('%s'))))
print("Start time in unix milliseconds time " + str(int(range(test)[1].strftime('%s'))))


#This was is more Pythonic and uses the current time from the host machine.
def range1(time):
    starttime = time - timedelta(hours = 1)
    roundback = starttime.replace(minute=0,second=0,microsecond=0)
    current = time.replace(minute=0,second=0,microsecond=0)
    return roundback, current


print("Start time in unix milliseconds time " + str(int(range1(date)[0].strftime('%s'))))
print("Start time in unix milliseconds time " + str(int(range1(date)[1].strftime('%s'))))
