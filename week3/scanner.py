#!/bin/python3

import sys # allows us tho eneter cp,,amdline arguments
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])#translate a host name to IPV4
else:
	print("ivalid amout of arguments.")
	print("sytax : python3 scanner.py <ip>")
	
