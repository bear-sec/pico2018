import socket

ips = open(r'C:\Users\Gera\Documents\GitHub\pico2018\Forensics\12  - Whats My Name\ips2.txt',
           'r').readlines()
for ip in ips:
    try:
        print socket.gethostbyaddr(ip.strip())
    except:
        print 'not found'
