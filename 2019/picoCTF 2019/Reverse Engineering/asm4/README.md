# asm4
**400 points**
## Description
> What will asm4("picoCTF_d7243") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm4_1_20b49d5dfd7aa7eceb32a78d2468fea1.
## Hints
> Treat the Array argument as a pointer
---
## Writeup
After trying it with pen and paper I decided to just compile it. With the help from [Jason Turley's writeup](https://jasonturley.xyz/picoctf-asm4-writeup/) I finally managed to compiled it in kali linux.

First, modify the format in the assembly file. Add `.intel_syntax noprefix` since we're not adding prefix `%` and add jumping labels.
```asm
.intel_syntax noprefix
.global asm4
	
asm4:
	push   ebp
	mov    ebp,esp
	push   ebx
	sub    esp,0x10
	mov    DWORD PTR [ebp-0x10],0x244
	mov    DWORD PTR [ebp-0xc],0x0
	jmp    asm4_27
asm4_23:
	add    DWORD PTR [ebp-0xc],0x1
asm4_27:
	mov    edx,DWORD PTR [ebp-0xc]
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,edx
	movzx  eax,BYTE PTR [eax]
	test   al,al
	jne    asm4_23
	mov    DWORD PTR [ebp-0x8],0x1
	jmp    asm4_138
asm4_51:
	mov    edx,DWORD PTR [ebp-0x8]
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,edx
	movzx  eax,BYTE PTR [eax]
	movsx  edx,al
	mov    eax,DWORD PTR [ebp-0x8]
	lea    ecx,[eax-0x1]
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,ecx
	movzx  eax,BYTE PTR [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	mov    edx,eax
	mov    eax,DWORD PTR [ebp-0x10]
	lea    ebx,[edx+eax*1]
	mov    eax,DWORD PTR [ebp-0x8]
	lea    edx,[eax+0x1]
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,edx
	movzx  eax,BYTE PTR [eax]
	movsx  edx,al
	mov    ecx,DWORD PTR [ebp-0x8]
	mov    eax,DWORD PTR [ebp+0x8]
	add    eax,ecx
	movzx  eax,BYTE PTR [eax]
	movsx  eax,al
	sub    edx,eax
	mov    eax,edx
	add    eax,ebx
	mov    DWORD PTR [ebp-0x10],eax
	add    DWORD PTR [ebp-0x8],0x1
asm4_138:
	mov    eax,DWORD PTR [ebp-0xc]
	sub    eax,0x1
	cmp    DWORD PTR [ebp-0x8],eax
	jl     asm4_51
	mov    eax,DWORD PTR [ebp-0x10]
	add    esp,0x10
	pop    ebx
	pop    ebp
	ret
```

Then write a `run.c` to run the file.
```c
#include <stdio.h>
#include <stdlib.h>

int asm4(char *);

int main(void)
{
	printf("picoCTF{0x%x}\n", asm4("picoCTF_d7243"));
	return 0;
}
```

Before compiling, remember to get 32-bit libraries or else the c file can't be compiled in 32-bit.
* `sudo apt-get update`
* `sudo apt-get install gcc-multilib`

Then do the following steps to get the flag.
* `gcc -masm=intel -m32 -c asm4.S -o asm4.o`
* `gcc -m32 -c run.c -o run.o`
* `gcc -m32 asm4.o run.o -o main`
* `./main`

flag: picoCTF{0x1d2}