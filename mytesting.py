

from time import sleep
import serial


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












# from optparse import OptionParser
# parser = OptionParser(usage="""usage: %prog [options] device_name
# This program is used for itgeeks pc labs for manitoring networking devices
# Mandatory argument to long optns are mandatory for short options too.
# '-c', '--connect                 You can select only one device for a while.
# '-r','--reserve                  Reserve a device for a while for using it.
# '-s', '--showOp                  Show type of selectable device for users""",
#                      version="%prog 1.0")
# parser.add_option("-c", "--connect",
#                   #action="connect_to_device",
#                   dest="connect",
#                   choices=["sw1",'sw2','sw3','sw4','router-1','router-2','router-c'],
#                   help="connect you to an available network device in lab")
# parser.add_option("-r", "--researve",
#                   #action="reserve a device for configuraion purpose", # optional because action defaults to "store"
#                   dest="resv",
#                   type="string",
#                   #default=True, # if don't specify the device for release
#                   help="reserve a device for configuraion purpose")
# parser.add_option("-l","--leave",
#                   dest = "leave",
#                   type="string",
#                   help = "leave the device that your currently using")
# parser.add_option("-t","--time",
#                   dest="time",
#                   type="int",
#                   default=2,
#                   help = "Specify the time that you want to use it.\n%prog [option] -t <time in hour>(defaul = 2 hour)")
#
# (options, args) = parser.parse_args()
#
# if (options.resv == None and options.connect == None and options.leave == None):
#     print(parser.usage)
#     print("\n[+] Eample:\nlab.py -c sw1 -r -t 3")
#
# elif (options.resv != None):
#     if (int(data) == 0):
#         device_reserves()
#     else:
#         device_reserves()
# elif(options.leave != None):
#     print ('yes')
# elif (options.connect != None and int(data) == 1):
#     #pass
#     device()
# else:
#     my_device()
