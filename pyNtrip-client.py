#!/usr/bin/env python

import socket
import base64
import sys

bs = "bs1"

# Definition of one or multiple NTRIP base stations
if bs=="bs1":
    server = "ip"
    port = "2101"
    mountpoint = "MNTPOINT"
    username = "uname"
    password = "passw"

def getHTTPBasicAuthString(username,password):
    inputstring = username + ':' + password
    pwd_bytes = base64.encodebytes(inputstring.encode("utf-8"))
    pwd = pwd_bytes.decode("utf-8").replace('\n','')
    return pwd

pwd = getHTTPBasicAuthString(username,password)

header =\
"GET /{} HTTP/1.0\r\n".format(mountpoint) +\
"User-Agent: NTRIP u-blox\r\n" +\
"Accept: */*\r\n" +\
"Authorization: Basic {}\r\n".format(pwd) +\
"Connection: close\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,int(port)))
s.sendto(header.encode('utf-8'),(server,int(port)))
resp = s.recv(1024)

if resp.startswith(b"STREAMTABLE"):
    print("Invalid or No Mountpoint")
    exit()
elif not resp.startswith(b"HTTP/1.1 200 OK"):
    print("All good")

try:
    while True:
        # There are some length bytes at the head here but it actually
        # seems more robust to simply let the higher level RTCMv3 parser
        # frame everything itself and bin the garbage as required.

        #length = s.recv(4)

        #try:
        #    length = int(length.strip(), 16)
        #except ValueError:
        #    continue
        
        data = s.recv(1024)
        
        if not data:
            exit()
        
        print(data)
        #print >>sys.stderr, [ord(d) for d in data]
        sys.stdout.flush()

finally:
    s.close()



