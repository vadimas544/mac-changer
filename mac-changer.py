import subprocess

#A module that allows us parse a arguments from user
#Ex: python3 mac-changer.py --interface=wlan0 --newmac=00:11:22:33:44:55

import optparse

#This is a simple mac-changer for Linux and Mac

#Create a parser object (instance of a class OptionParser)
parser = optparse.OptionParser()
#Option that parser is expect from user
parser.add_option("-i", "--interface", dest="interface", help="Interface to change is MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

#Options contain a variables: wlan0, 00:11:22:33:44:55
#Arguments contain: --interface, --mac

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC-address for " + interface + " to " + new_mac)

 #subprocess.call("ifconfig " + interface + " down", shell=True)

 #Securely run command - put them into a list
 #subprocess.call(["ifconfig", interface, "down"])

 #subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
 #subprocess.call("ifconfig wlan0 up", shell=True)