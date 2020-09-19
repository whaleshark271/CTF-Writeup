from pwn import *
import re

ip = "ctf.isss.io"
port = 5421
r = remote(ip, port)

r.recvuntil('this service.\n')
string = r.recvline(keepends=False)
nums = [int(s) for s in re.findall(r'\d+', string.decode('utf-8'))]
ans = nums[0] + nums[1]
r.sendline(str(ans))

while True:
	r.recvuntil('Correct!\n')
	string = r.recvline(keepends=False)
	if string == b'Retrieving flag...':
		flag = r.recvline(keepends=False)
		print(flag)
	nums = [int(s) for s in re.findall(r'\d+', string.decode('utf-8'))]
	ans = nums[0] + nums[1]
	print(ans)
	r.sendline(str(ans))