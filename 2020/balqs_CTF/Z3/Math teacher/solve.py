from pwn import *
from z3 import *

ip = "ctf.balqs.nctu.me"
port = 9001
r = remote(ip,port)

while True:
	eq1 = r.recvline(keepends=False)
	q1 = eq1.replace('=','==')
	print(eq1)
	eq2 = r.recvline(keepends=False)
	q2 = eq2.replace('=','==')
	print(eq2)

	x = Int('x')
	y = Int('y')
	s = Solver()
	s.add(eval(q1))
	s.add(eval(q2))
	assert s.check() == sat
	m = s.model()
	print(m)
	r.recvuntil('x = ')
	r.sendline(str(m[x]))
	r.recvuntil('y = ')
	r.sendline(str(m[y]))


