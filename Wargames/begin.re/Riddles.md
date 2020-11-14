# Preparation Assignments
## 1 - Welcome!
1. What is foo in the following example? How much space does it occupy in memory?
```assembly
.data
    foo DW 1,1,2,3,5
```
An array of 5 2-byte values, initialized to 1 1 2 3 5

2. What is the value stored in EAX by the end of this code?
```assembly
mov eax,0x2 # eax = 0x2
mov ebx,eax # ebx = 0x2
shl eax,0x2 # eax = 0x8
add eax,ebx # eax = 0xa
and eax,0x8 # eax = 0x8, 1010 and 1000
```
eax = 0x8

3. Bonus: what should be the value of EAX at the beginning of the following code, such that by the end of it, EAX = 0?
```assembly
xor eax eax
```
Any value will do.

## 2 - The Call Stack & Ollydbg
1. Which register holds the address of the top of the stack?

ESP

2. Suppose the function multiply(x, y) creates 2 local variables - tmp1 and tmp2 - during its execution. What instruction do you expect seeing that allocates memory for these variables?
```assembly
sub ESP, 0x8
```

Emphasis on "allocates memory"

3. In what order will multiply’s parameters, x and y, be pushed onto the stack before the call to multiply?

First y then x. Function parameters are pushed in reverse order.

4. How can each of them be accessed during the function execution? Write the exact expressions.
```assembly
[ebp+0x8] for x, [ebp+0xC] for y
```

Don't forget about return address.

```assembly
|    y    | # ebp - 0xC
|    x    | # ebp - 0x8
| ret adr |
|   ebp   |
```

## 3 - Last Prep, YOOHOO!
1. Figure out whether your computer is running a 32-bit or a 64-bit version of windows.
2. What does the following code print? If you have no idea what these percent-signs stand for, take a look here.
```c 
int num = 2;
int *ptr = &num;
char c = ‘b’;
char *ptr2 = &c;
char mid[] = “|| !”;

printf(“%d %c %s %d %c”, *ptr, c, mid, num, *ptr2);
```

2 b || ! 2 b