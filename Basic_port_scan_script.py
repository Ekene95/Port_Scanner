#!/bin/python3

import socket  #Importing the socket library for connecting to the internet
from IPy import IP #Library for resolving IP addresses

ipaddress = input('[+] Enter Target to scan:')  # To enable us insert the web address to scan
port=80  #stating the port we will be checking or running
try:
    sock=socket.socket()  #This code creates the socket object we are storing (the variables, which is the webaddress and port)
    sock.connect((ipaddress, port)) #Parameter of what to scan
    print('[+] Port 80 is open')  #string command. Information to display when run 
except:
    print('[-] Port 80 is closed')    #same as line 11
