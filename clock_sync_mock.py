from time import ctime
import time , calendar , os, sys, logging, datetime 
from  clock_lib.dateutil import relativedelta 
from clock_lib import ntplib
from subprocess import Popen, PIPE


#reference points 
#<timeserver> will need to be changed to your time server url 
#https://stackoverflow.com/questions/12664295/ntp-client-in-python
#https://stackoverflow.com/questions/6574329/how-can-i-produce-a-human-readable-difference-when-subtracting-two-unix-timestam
def test():
    c = ntplib.NTPClient()   #create a object of the class 
    response = c.request('<timeserver>')
    isntp =response.tx_time

    sub= "@"
    sub1 = sub + str(isntp)

    isOS = calendar.timegm(time.gmtime()) #why use this when you can call time.time() ? --hel

    dt1 = datetime.datetime.fromtimestamp(isntp) # 1973-11-29 2i2:33:09
    dt2 = datetime.datetime.fromtimestamp(isOS) # 1977-06-07 23:44:50
    rd = relativedelta.relativedelta(dt2, dt1)

    # 3 years, 6 months, 9 days, 1 hours, 11 minutes and 41 secondsi

    #logging config 

    validate = rd.minutes

    if validate < -1 :
    #    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
    #    print("Time is out of sync & self correctng ")
        code =Popen(["date", "-s", sub1])   
        code.communicate()
        logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
        logging.info('The clock was out of sync with the NTP server by -%s minutes ' , validate)

    elif validate > 1 :
    #    print(" %d hours, %d minutes and %d seconds" % (rd.hours, rd.minutes, rd.seconds))
    #    print("Time is out of sync & self correctng ")
        log = rd
        code =Popen(["date", "-s", sub1])                               
        code.communicate()
        logging.basicConfig(format='%(asctime)s %(message)s',filename='clocksync-natprov.log',level=logging.INFO)
        logging.info('The clock was out of sync with the NTP server by %s minutes' , validate)
    else:
        print("Time is synced")
