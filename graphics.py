import os
import socket

class graphics_startup():

    def menu():
        IP = '1.1.1.1'
        DeviceID = socket.gethostname()
        os.system('cls')
        print("""
        
        
________  ________  ________  ________  ___  ________  ________  _________   
|\   ____\|\   __  \|\   __  \|\   ___ \|\  \|\   __  \|\   __  \|\___   ___\ 
\ \  \___|\ \  \|\  \ \  \|\  \ \  \_|\ \ \  \ \  \|\ /\ \  \|\  \|___ \  \_| 
 \ \_____  \ \   ____\ \  \\\  \ \  \ \\ \ \  \ \   __  \ \  \\\  \   \ \  \  
  \|____|\  \ \  \___|\ \  \\\  \ \  \_\\ \ \  \ \  \|\  \ \  \\\  \   \ \  \ 
    ____\_\  \ \__\    \ \_______\ \_______\ \__\ \_______\ \_______\   \ \__
   |\_________\|__|     \|_______|\|_______|\|__|\|_______|\|_______|    \|__|
   \|_________|                    


    Welcome                   Device Name: {0}            IP:{1}
        """.format(DeviceID, IP))
        pass
    def reqirements():
        Operating_Sys = sys.platform("Windows","Linux")
        import urllib2

        def internet_on():
            try:
                urllib2.urlopen('http://216.58.192.142', timeout=1)
                return True
            except urllib2.URLError as err: 
                return False
                pass


