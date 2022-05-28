#!/bin/python3

import socket
from IPy import IP

def scan_port(ipaddress, port):
   try:
       sock = socket.socket()
       sock.settimeout(0.5)
       sock.connect((ipaddress, port))
       print('[+] Port' + str(port) + 'is open')
   except:
       print('[-] Port' + str(port) + 'is closed')
       
ipaddress = input('[+] Enter Target to scan:')
for port in range(1,50):
    scan_port(ipaddress(ipaddress, port)
