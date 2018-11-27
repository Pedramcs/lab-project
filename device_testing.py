

import time
from re import findall,search
import os
#/------------------------------------------------\#
#global users for using of multiple functions
global usr #user store
global data #boolean data
data = ''
def open_file(file,access,keyword): #method for open the main txt file
    data=0                          #that used for multiple purposes
    with open(file,access) as file:
        pattern = keyword
        string = file.read()
        data = search(pattern,string)
        data = data.group()
    return data

data = open_file('test2.txt','r+','[0-1]')
#print (data)

def device_reserves(): #method for decide whether a device selected or not
    usr=os.getlogin()
    if int(data) != 1: #if device is not reserved
        print("Device reserve function is called!\n")
        f = open('test2.txt','w+')
        f.write('bool$1:\nName:sw1\nuser:'+usr+"\n")
    else: #if the device have been selected by a user
        usr = open_file("test2.txt","r+",'u\w+:.+')
        print('Sw1 is currently using by '+str(usr))

def device():
    if int(data) == 1:
        print('Yes')
    else:
        print('[-] Please reserve a device for configuration\n'+\
        'Type lab.py -r <device_name> ^ type -h or --help for more instructions ')

device_reserves()
device()
