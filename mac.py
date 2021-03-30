#!/usr/bin/env python3
'''change MAC address help to increase annonymity,impersonate other devices,bypass filters
	
'''

'''		|	|	|       __
			|	|	   /  /		_____
			|	|     /  /   	|	\
			|	|    /  /		|	 \              /---\
			|	|	/  /		|   __\_           /     \
			|	|  /  /			|	|             /		  \        /
			|	| /  /			|	|            /	 /	\  \      /
			|	|/  /			|	| 		    /   /    \  \    /
			|	|\  \			|	|          /   /      \  \  /
			|	| \  \			|	|		  /   /		   \  \/
			|	|  \  \			|	|		 /   /          \
			|	|   \  \		|	|		/   /            ---
			|	|	 \__\		|	|      /   /

	
	'''


import subprocess
import optparse#allows to get aggument from the user and run them 

def get_argument():

	parser = optparse.OptionParser()

	parser.add_option("-i", "--interface", dest="interface", help="Interface to chage it MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

	(options, arguments) = parser.parse_args()
	if not options.interface:
		#code to handle error
		parser.error("[-] Please specify an interface, user --help for more info.")

	elif not options.new_mac:
		#code to handle error
		parser.error("[-] Please specify an new mac, user --help for more info.")

	return options




def change_mac(interface, new_mac):

	print("[+]Changing MAC address for " + interface + " to " + new_mac)

	subprocess.call("ifconfig "+ interface + " down ", shell=True)
	subprocess.call("ifconfig "+ interface + " hw ether "+ new_mac, shel=True)
	subprocess.call("ifconfig "+ interface + " up ", shell=True)



#interface = options.interface
#new_mac = options.new_mac
options = get_argument()

change_mac(options.interface, options.new_mac)





#python3 mac.py --interface wlan0 --mac 00:11:33:44:22
