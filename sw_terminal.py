import time
import serial

device_name = input('select device name: ')
#ser = serial.Serial(  # open a serial port with following detail
#    port='/dev/ttyS0',# location of serial port(differ in other OS like windows)
#    baudrate=9600,    # port 9600 the default port of cisco device connection
#    parity=serial.PARITY_ODD,
#    stopbits=serial.STOPBITS_TWO,
#    bytesize=serial.SEVENBITS
#)
#ser.isOpen() # is the connectio is open?

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')

input=1
while 1 :
    # get keyboard input

    input = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)
        if out !='':
            print (">>" + out)
