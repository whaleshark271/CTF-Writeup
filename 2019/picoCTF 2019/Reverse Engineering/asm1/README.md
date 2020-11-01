# asm1
**200 points**
## Description
> What does asm2(0xd,0x1e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm2_5_19a47cfa109e75480bcd052744a7a816.
## Hints
> assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
---
## Writeup
The stack frame should look a bit like this:
```
|      ...       | <= high address
|                | 
|     0x1b4      | # function parameter, ebp + 0x8
| return address | 
|   saved ebp    | <= ebp
...
<local variables>
...
|                | <= esp, low address
```

So this code should execute till <asm1+27>, where eax is 0x1b4 + 0x13 = 0x1c7, and jump to <asm1+60> then return the value of eax.

flag: picoCTF{0x1c7}