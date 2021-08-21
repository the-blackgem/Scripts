#!/usr/bin/env python
#use sudo python change_mac_address.py -i [name of interface] -m [new value of MAC address]

import subprocess
import optparse
from optparse import OptionParser

parser: OptionParser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to Change MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="Introduce new MAC address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing Mac Address for Interface " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#For Mac
#subprocess.call(["ifconfig", interface, "ether", new_mac])
subprocess.call(["ifconfig", interface, "up", new_mac])

print ("Done!")
subprocess.call("ifconfig " + interface, shell=True)
