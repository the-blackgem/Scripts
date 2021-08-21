#!/usr/bin/env python

#Intended for Linux

import subprocess

subprocess.call("ifconfig en0 down", shell=True) #Use the network interface you want to change its MAC address
subprocess.call("ifconfig en0 hw ether 00:11:22:33:44:00", shell=True) #The new MAC address can be whatever you decide as long as it is 12 numbers separated by pairs with ":"
subprocess.call("ifconfig en0 up", shell=True)

print ("Done!")
subprocess.call("ifconfig en0", shell=True)
