# vault-door-8
**450 points**
## Description
> Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](VaultDoor8.java)
## Hints
> Clean up the source code so that you can read it and understand what is going on.
>
> Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.
---
## Writeup
First format the source code so it is readable. Then use switchBits() in a reverse order to gain the flag.

flag: picoCTF{s0m3_m0r3_b1t_sh1fTiNg_471ea5f81}