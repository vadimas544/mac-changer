import subprocess
import optparse

def get_args():

    # Create a parser object (instance of a class OptionParser)
    parser = optparse.OptionParser()

    # Option that parser is expect from user
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change a MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    # Options contain a variables: wlan0, 00:11:22:33:44:55
    # Arguments contain: --interface, --mac
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_args()
change_mac(options.interface, options.new_mac)