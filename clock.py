import datetime
import time
import os

loop = 69
while loop < 420:
    x = datetime.datetime.now()

    print(x.strftime("%Y %B %d"))
    #Date with words
    print(x.strftime("%y %m %d"))
    #Date without words

    print(x.strftime("%I:%M %p"))
    #Numbers

    print(x.strftime("%I:%M:%S %p"))
    #Numbers with seconds

    print(x.strftime("Hours: %I Minutes: %M %p"))
    #Full with words without seconds

    print(x.strftime("Hours: %I Minutes: %M Seconds: %S %p")) 
    #Full with words and with seconds
    time.sleep(1)
    os.system("cls")    