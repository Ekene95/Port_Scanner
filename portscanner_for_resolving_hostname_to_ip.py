#!/bin/python3

import socket   #socket library
from IPy import IP       #ip library

def check_ip(ip):  #defining function for checking the IP address against hostname
   try:
       IP(ip)
       return(ip) 
   except ValueError:
       return socket.gethostbyname(ip)
       
def scan_port(ipaddress, port):   
   try:
       sock=socket.socket()       #parameter to connect to the internet
       sock.settimeout(0.5)       #parameter stating the amount of time used in scanning each port
       sock.connect((ipaddress, port))
       print('[+] Port' +  str(port)  + 'is open')
   except:
       print('[-] Port' +  str(port)  + 'is closed')
       
ipaddress = input('[+] Enter Target to scan:')   #information on what port to scan
converted_ip = check_ip(ipaddress)    #defining value

for port in range(1,50):     #for loop and stating the port ranges to scan
    scan_port(converted_ip, port)                
