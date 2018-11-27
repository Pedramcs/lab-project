import re
import datetime
from time import gmtime, strftime,sleep
#input = input("enter a hour: ")
tim=strftime("%a,%d %b %Y %H:%M:%S + 0000 ",gmtime(10))
"""%a <is name of the week in abbreviated>
   %d <is the day of the month>
   %b <is the name of the mount in abbreviated>
   %Y <Year>
   %H <Hour>
   %M <Minute>
   %S <Second>
   """
global b, time2
global key
time2=0
b=True
file = open('test2.txt','r+')
string = file.read()
pattern = r'[0-9]'
def main(b,time2):
    bool = re.search(pattern,string)
    key = int(bool.group()) #This is the key which a user can't open this file two time
    if not key:            #for one log-in
        file.close()
        h = int(strftime ("%I",gmtime()))
        m = int(strftime ("%M",gmtime()))
        s = int(strftime ("%S",gmtime()))
        c_time = strftime ("%I:%M:%S",gmtime())
        #the time that specified for a user, who select a switch for configuration
        global end_h
        global end_m
        global end_s
        if b:
            end_h = h+1
            end_m = m
            end_s = s
            time2 = datetime.time((end_h),int(m),int(s))
            f = open('test2.txt','w+')
            f.write('bool$1')
            f.close()
        print("The current time is "+ c_time +", and your expire time is "+ str(time2))

        if h == end_h and m == end_m and s == end_s:
            r = int(h) + 1
            print(r)
            print("it''s Work")
            exit(0)
        b=False
        sleep(1)
        main(b,time2)

    else:
        print ('Your currently in use of a device')

main(b,time2)
#def time1(time):




#test = "Switch1$192.168.20.1"
#pattern=r'[0-9]\w+.+'
#output = re.findall(pattern,test)
#print (output)
