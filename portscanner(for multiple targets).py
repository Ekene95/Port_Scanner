#!/bin/python3

import socket
from IPy import IP       #ip library

def scan(target):
      converted_ip = check_ip(target)
      print('\n' + '[-_scanning Target]' + str(target))
      for port in range(1,500):     
          port_scan(converted_ip, port) 
    
def check_ip(ip): 
     try:
        IP(ip)
        return(ip) 
     except ValueError:
        return socket.gethostbyname(ip)
       
def get_banner(s):
      return s.recv(1024)       
       
def port_scan(ipaddress, port):
     try:
         sock = socket.socket()       #parameter to connect to the internet
         sock.settimeout(0.5)       #parameter stating the amount of time used in scanning each port
         sock.connect((ipaddress, port))
         try:
             banner = get_banner(sock)
             print('[+] Open port' + str(port) + ' : ' + str(banner.decode().strip('\n')))        
         except:        
             print('[+] Open Port' +  str(port))
     except:
           pass
 
       
if __name__ == "__main__":   
     targets = input('[+] Enter Target/s to Scan(split multiple targets with,):')
     if ',' in targets:
            for ip_add in targets.split(','):
                  scan(ip_add.strip(' '))
     else:
         scan(targets)
 
 
