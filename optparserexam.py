#!/usr/bin/env python

from optparse import OptionParser
from time import sleep
import time
from re import findall,search
import os
import serial



def device():
	# configure the serial connections (the parameters differs on the device you are connecting to)
	ser = serial.Serial(
		port='/dev/ttyS0',
		baudrate=9600,
		parity=serial.PARITY_ODD,
		stopbits=serial.STOPBITS_TWO,
		bytesize=serial.SEVENBITS
	)

	#ser.open()

	print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

	input=1
	bool = ''
	print("[+] Device is booting, please wait a moment...")
	time.sleep(1)
	print("[+] Device is getting ready for you...")

	while 1 :
		# get keyboard input
		input = raw_input(str(bool))
		# Python 3 users
		# input = input(">> ")
		if input == 'exit':
			ser.close()
			exit()
		else:
			# send the character to the device
			# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
			ser.write(input + '\r')
			out = ''
			# let's wait one second before reading output (let's give device time to answer)
			time.sleep(1)
			while ser.inWaiting() > 0:
				out += ser.read(1)
				bool = out
			if out != '':
				#print ">>" + out
				pass

def reset_device():
	#function that reset a selected device!
	ser = serial.Serial(
	        port = '/dev/ttyS0',
	        baudrate = 9600,
	        parity = serial.PARITY_ODD,
	        stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS
	)

	#ser.close()
	print("[!] checking your device availability...")
	sleep(2)
	if ser.isOpen() : #chech if the serial port was open
	    print("[+] Device availability: Ok!")
	    sleep (2)
	    ser.write("\r\n\r\n")
	    ser.write("\nend\n")
	    ser.write("\nen\n")
	    print("[+] Your connected to device!")
	    sleep (2)
	    print("[!] Trying to erase startup configuraion")
	    ser.write("\nerase startup-config\n\n")
	    sleep (2)
	    ser.write("\r\r\n\n")
	    print("[+] Ok")
	    sleep (2)
	    print ("[!] Erasing nvram...")
	    ser.write("\nerase /all nvram:\n\r\n")
	    sleep (2)
	    print("[+] Ok")
	    ser.write("\n\n")
	    ser.write("\n\n")
	    ser.write("\nyes\n")
	    sleep (2)
	    print ("[!] Deleting Flash vlan data...")
	    ser.write("\n\n")
	    ser.write("delete flash:vlan.dat")
	    sleep (2)

	    ser.write("\n\n")
	    ser.write("\nyes\n")
	    print ("[+] Ok")
	    print ("[+] Program reload your device")
	    sleep (1)
	    ser.write("\nreload\n\n")
	    ser.write("\nyes\n")
	    ser.write("\n\n")

	else:
	    print ("[-] Device is not available")


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

def device_reserves(device_name): #method for decide whether a device selected or not
    usr=os.getlogin()
    if int(data) != 1: #if device is not reserved
        print(device_name+" reserved by "+str(usr))
		#print("Device have reserved!")
        f = open('test2.txt','w+')
        f.write('bool$1:\nName:'+device_name+'\nUser:'+usr+"\n")
    elif (int(data) == 1): #if the device have been selected by a user
	# a way for user can't
        usr = open_file("test2.txt","r+",'U\w+:.+')
        print('Sw1 is currently using by '+str(usr))

def login(device_name):
    if int(data) == 1:
        #print('Yes')
        device()
    else:
        print('[-] Please reserve a device for configuration\n'+\
        'Type lab.py -r <device_name> ^ type -h or --help for more instructions ')


def main():

	parser = OptionParser(usage="""usage: %prog [options] device_name
	This program is used for itgeeks pc labs for manitoring networking devices
	Mandatory argument to long optns are mandatory for short options too.
	'-c', '--connect                 You can select only one device for a while.
	'-r','--reserve                  Reserve a device for a while for using it.
	'-s', '--showOp                  Show type of selectable device for users""",
	                     version="%prog 1.0")

	parser.add_option("-c", "--connect",
	                  #action="connect_to_device",
	                  dest="connect",
	                  choices=["sw1",'sw2','sw3','sw4','router-1','router-2','router-c'],
	                  help="connect you to an available network device in lab")

	parser.add_option("-r", "--researve",
	                  #action="reserve a device for configuraion purpose", # optional because action defaults to "store"
	                  dest="resv",
	                  type="string",
	                  #default=True, # if don't specify the device for release
	                  help="reserve a device for configuraion purpose")

	parser.add_option("-l","--leave",
	                  dest = "leave",
	                  type="string",
	                  help = "leave the device that your currently using")

	parser.add_option("-t","--time",
	                  dest="time",
	                  type="int",
	                  default=2,
	                  help = "Specify the time that you want to use it.\n%prog [option] -t <time in hour>(defaul = 2 hour)")

	parser.add_option("-u","--unset-device",
					 dest = "unset",
					 type = "string",
					 #chosie = ["sw1",'sw2','sw3','sw4','router-1','router-2','router-c']
					 #default=False,
					 help = "To save the configurtion to first day",
					 )
	(options, args) = parser.parse_args()
	temp = open_file('test2.txt','r+','s\w+')


	#if user leave the program without any arguments
	#lab.py
	if (options.resv == None and options.connect == None and options.leave == None and options.unset == None):
	    print(parser.usage)
	    print("\n[+] Eample:\nlab.py -c sw1 -r -t 3")


	#lab.py -r <device_name>
	elif (options.resv != None):
		device_name = options.resv
		if (int(data) == 0):
			device_reserves(device_name)
		else:
			device_reserves(device_name)


	#if user wants to leave the switch
	#lab.py -l <device_name>
	elif(options.leave != None):
		#print(temp)

		if int(data) == 1 and options.leave == temp:
			rf = open('test2.txt','r+')
			rf.write('bool$0:\nName:sw1\nuser: Device is free'+"\n")
			rf.close()
			print("[+] You leave "+options.leave)
		else:
			print('[-] Your not currently in use of '+options.leave+"\nYou can do following:")
			print("lab.py -r <device_name> or Type lab.py -h or lab.py --help")

	# option for reset a selected device
	# %prog -s device_name
	elif (options.unset != None and int(data) == 1):
		if (options.unset == temp):
			reset_device()
		else:
			print("[-] You don't reserve this device\n[!] Reserved Device is: "+temp)
		#reset_device()


	#if user want to connect to the device that he/she reserved
	elif (options.connect != None and int(data) == 1):
	    #pass
		if (options.connect == temp):
			login(options.connect)
		else:
			print('You don''t reserved '+options.connect)
	else:
		#print('no:>')
		login(options.connect)




#if __name__ == "main":

main()
