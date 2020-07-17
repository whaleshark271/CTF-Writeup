# vault-door-6
**350 points**
## Description
> This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](VaultDoor6.java)
## Hints
> If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.
---
## Writeup
xor myBytes with `0x55`

flag: picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_57c2892}