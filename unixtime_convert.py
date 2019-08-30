#!/usr/bin/env python3

###convert unix team to human readable time. This works if the unix time is in milliseconds. 

from datetime import datetime,timedelta 


def milltohuman():
    time = input("Enter the Cyclone event time to be converted: ")

#convert to seconds 
    fix = int(time) / 1000

    value = datetime.datetime.fromtimestamp(fix)
     #return the human readable format
    return value.strftime('%Y-%m-%d %H:%M:%S')





date = datetime.now()
test = "2019/08/29 12:13:00"


## prototyping two ways to convert a standard human readable time to unix time in milliseconds.

#This way uses input from the user
def range(time):
    starttime = datetime.strptime(time, "%Y/%m/%d %H:%M:%S") - timedelta(hours = 1)
    roundback = starttime.replace(minute=0,second=0,microsecond=0)
    current = datetime.strptime(time, "%Y/%m/%d %H:%M:%S").replace(minute=0,second=0,microsecond=0)
    return roundback, current


#call the function and print the result. I am also mulitplying the result to get the milliseconds from seconds. 
#print(int(range(date).strftime('%s')))
print("Start time in unix milliseconds time " + str(int(range(test)[0].strftime('%s'))* 1000))
print("Start time in unix milliseconds time " + str(int(range(test)[1].strftime('%s'))* 1000))


#This was is more Pythonic and uses the current time from the host machine.
def range1(time):
    starttime = time - timedelta(hours = 1)
    roundback = starttime.replace(minute=0,second=0,microsecond=0)
    current = time.replace(minute=0,second=0,microsecond=0)
    return roundback, current

#call the function and print the result. I am also mulitplying the result to get the milliseconds from seconds. 
print("Start time in unix milliseconds time " + str(int(range1(date)[0].strftime('%s'))* 1000))
print("Start time in unix milliseconds time " + str(int(range1(date)[1].strftime('%s'))* 1000))
