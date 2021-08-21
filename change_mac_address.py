#!/usr/bin()/env python

import subprocess

interface = input("enter interface >")
new_mac = input("enter new mac value >")

print("[+] Changing Mac Address for Interface " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#For Mac
#subprocess.call(["ifconfig", interface, "ether", new_mac])
subprocess.call(["ifconfig", interface, "up", new_mac])

print ("Done!")
subprocess.call("ifconfig " + interface, shell=True)
