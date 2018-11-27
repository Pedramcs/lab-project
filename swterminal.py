

sw_list = ['sw1','sw2','sw3']
in1 = input("Enter a switch name: ")

if in1 in sw_list:
    inp = input(in1 +'>')
    if (inp == "enable" or inp == "en"):
        inp1 = input(in1+"$")
    if inp1 == "configuration terminal" or inp1 == "conf t" or inp1 == "conf ter":
        inp2 = input(in1 +"(config)$")
