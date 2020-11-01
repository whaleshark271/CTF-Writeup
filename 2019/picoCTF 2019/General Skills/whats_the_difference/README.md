# whats_the_difference
**200 points**
## Description
> Can you spot the difference? [kitters](kitters.jpg) [cattos](cattos.jpg). They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server
## Hints
> How do you find the difference between two files?
>
> Dumping the data from a hex editor may make it easier to compare.
---
## Writeup
```python
kitters = open('kitters.jpg', 'rb').read()
cattos = open('cattos.jpg', 'rb').read()

flag = ""

for i in range(len(kitters)):
	if kitters[i] != cattos[i]:
		flag += chr(cattos[i])

print(flag)
```

flag : picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}