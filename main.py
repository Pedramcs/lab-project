#Besmellah
import re
from time import sleep
print ("Welcome to *** application!")
select=input("""What do you want to do?
1) Select a switch and go on!
2) What this app do?
3) About\n""")
option=""
IP="" # Global IP Adress used by your selection
if select == "1": #Selecting Switch for configuration
    input("[+] Now you can select a Switch to configure and enjoy, Enter Please\n")
    with open("swip.txt","r") as f:
        l = f.readlines()
        i=1
        for line in l:
            output=re.findall("[a-zA-Z]\w+",line)
            print (str(i)+") "+output[0])
            i+=1
    option=int(input("Which:"))
    while True:
        n=option
        if option == n and option<=7:
            IP = "192.168.30."+str(n)
            print("""[+] The following detail based on Sw"""+str(n)+""":
            [+] IP Address: 192.168.30."""+str(n)+"""
            [+] Username: itgeeks
            [+] Password: 0000\n""")

            ss = input("""[++] What do you want to do?
            1) Connect to main configuration of switch
            2) Reset Configuration of Switch
            3) Save Configuration
            4) Show options
            5) Exit\n""")

            if ss == "1": #connect to switch teminal
                username=input("[?] Username:")
                password=input("[?] Password:")
                Telnet(IP,Username, Password)
            elif ss == "2":
                username=input("[?] Username:")
                password=input("[?] Password:")
                Reset(IP,Username,Password)
            elif ss == "3":
                username=input("[?] Username:")
                password=input("[?] Password:")
                SaveConf(IP,Username,Password)
            elif ss == "4":
                showOp=input("""[+] Show Option [+]
                1) Show running Configuration
                2) Show ip summary
                3) show ....
                4) show ....\n""")
                ShowOptions(showOp)
            elif ss == "5":
                exit(0)
        else:
            print ("Your entry is incorrect, bye :<")
            exit(0)
if select == 2:
    """What this app do?"""
if select == 3:
    """about This app?"""
def ShowOptions(showOp):

    """Show detail of showOptions"""
    return 0;
