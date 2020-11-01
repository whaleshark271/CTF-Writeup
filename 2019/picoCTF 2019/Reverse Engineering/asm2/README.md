# asm2
**250 points**
## Description
> What does asm2(0xd,0x1e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm2_5_19a47cfa109e75480bcd052744a7a816.
## Hints
> assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
---
## Writeup
```
|      ...       | <= high address
|      0x1e      | # function parameter, ebp + 0xC
|      0xd       | # function parameter, ebp + 0x8
| return address | 
|   saved ebp    | <= ebp
...
<local variables>
...
|                | <= esp, low address
```

The assembly code can be translated to this:
```c++
int a = 30;
int b = 13;

while(b <= 26536){
    a += 1;
    b += 250;
}

return a;
```
`a` should be 137, which is 0x89.

flag: picoCTF{0x89}