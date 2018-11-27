import datetime
from time import gmtime, strftime,sleep
import optparse
import time
import re

global b, time2, resv_h,bool
global key
time2=0
file = open('test2.txt','r+')
string = file.read()
pattern = r'[0-1]'

def resv_switch_time(b,time2,resv_h):
    bool = re.search(pattern,string)
    key = int(bool.group()) #This is the key which a user can't open this file two time
    while not key:
        h = int(strftime ("%I",gmtime()))
        m = int(strftime ("%M",gmtime()))
        s = int(strftime ("%S",gmtime()))
        c_time = strftime ("%I:%M:%S",gmtime())
        #the time that specified for a user, who select a switch for configuration
        global end_h
        global end_m
        global end_s
        if b:
            end_h = h + int(resv_h)
            end_m = m
            end_s = s
            time2 = datetime.time((end_h),int(m),int(s))
        print("The current time is "+ c_time +", and your expire time is "+ str(time2))
        n=3
        if h == end_h and m == end_m and s == end_s:
            #should being end
            print("it''s Work")
            exit(0)
        b=False
        sleep(1800)
        resv_switch_time(b,time2)

#main(b,time2,resv_h)



#method of device selection
def show_devices():
    with open("swip.txt","r") as f:
        l = f.readlines()
        i=1
        for line in l:
            output=re.findall("[a-zA-Z]\w+",line)
            print (str(i)+") "+output[0])
            i+=1

#def select_device(device_name):
#    """Comming Soon"""
#    pass

def Main():
    parser = optparser.OptionParser('usage %prog '+\
    'Is [Option]... [Device Name]'+\
            'This program is used for itgeeks pc labs for manitoring networking devices'+\
            'Mandatory argument to long optns are mandatory for short options too.'+\
            '-c', '--connect                 You can select only one device for a while.'+\
            '-r','--reserve                  Reserve a device for a while for using it.',+\
            '-s', '--showOp                  Show type of selectable device for users',
            version='%prog 1.0')
    parser.add_option('-c','--connect', dest='connect',type='string',\
    help = 'Specify a network device name to connect to console of that device')

    parser.add_option('-r','--reserve', dest='resv',type='int',\
    help = 'Specify a time for your configuration, that no one can''t disturb you')

    parser.add_option('-s','--show-devices', dest='show',\
    help='Show you type of networkingdevice in the network')

    parser.add_option('-h','--help',dest='help',\
    help='Show you the usage of the prgram')

    (options, args) = parser.parse_args()

    #without -c or --connect (empty)
    if (options.connect == None):
        print(parser.usage)

    elif (options.connect !=None and device_reserve == 1):
        print("you should specify a time for your duration")


    #%prog -c device_name -r (reserver a time) (selected)
    #elif (options.connect !=None and options.resv !=None):
    #    device_name=options.connect
    #    #should specify a time for using of switch
    #    resv_switch_time(time2,options.resv)
    #    print ("[+] Please wait a minute that program connect you to "+str(device_name))
    #    select_device(device_name)

        #%prog -c device name (but not specify reservation time)

        #reserve a time for his(her) configuration period
        #%prog (don't use a device name) -r 10 (but specify a time for non device)

    # %prog -s (--show)
    #if (options.show):
    #    print ("It's work")
        #if it work
    #    input("There are type of devices which you can select for your configuarion"+\
#        "type name one of them after -c to connect to that device")
#        show_devices()
    # %prog -h (--help)
    #if (options.help):



Main()
