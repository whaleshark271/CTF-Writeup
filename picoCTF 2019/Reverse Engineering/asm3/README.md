# asm3
**300 points**
## Description
> What does asm3(0xcdc485c1,0xd6bd5e88,0xe4c1548d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S) located in the directory at /problems/asm3_5_b1d8dd18dc6e01e760acc4919af96707.
## Hints
> more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)
---
## Writeup
```
|      ...       | <= high address
|   8d 54 c1 e4  | # function parameter, ebp + 0x10
|   88 5e bd d6  | # function parameter, ebp + 0xC
|   c1 85 c4 cd  | # function parameter, ebp + 0x8
| return address | 
|   saved ebp    | <= ebp
...
<local variables>
...
|                | <= esp, low address
```

```asm
push   ebp
mov    ebp,esp
xor    eax,eax                # 0x00000000
mov    ah,BYTE PTR [ebp+0x8]  # 0x0000c100
shl    ax,0x10                # 0x00000000
sub    al,BYTE PTR [ebp+0xe]  # 0x00000043
add    ah,BYTE PTR [ebp+0xc]  # 0x00008843
xor    ax,WORD PTR [ebp+0x10] # 0x0000dcce
nop
pop    ebp
ret
```
The result of each instruction is commented above.

Remember that the parameters are stored in little endian. So `BYTE PTR [ebp+0x8]` should be 0xc1 and `WORD PTR [ebp+0x10]` should be 0x548d.