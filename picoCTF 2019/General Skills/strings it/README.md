# strings it
**100 points**
## Description
> Can you find the flag in [file]() without running it? You can also find the file in /problems/strings-it_4_e276260a1b64a734b4178a280d25b754 on the shell server.
## Hints
[strings](https://linux.die.net/man/1/strings)
---
## Writeup
```shell
$ strings strings | grep "pico"
picoCTF{5tRIng5_1T_c611cac7}
```

flag : picoCTF{5tRIng5_1T_c611cac7}