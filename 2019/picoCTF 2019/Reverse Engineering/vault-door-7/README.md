# vault-door-7
**400 points**
## Description
> This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](VaultDoor7.java)
## Hints
> Use a decimal/hexademical converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
>
> You will also need to consult an ASCII table such as this one: https://www.asciitable.com/
---
## Writeup
Do exactly the reverse of what the minion did.
```
#1 Find the binary of the integers
1096770097 -> 1000001010111110110001000110001
1952395366 -> 1110100010111110011000001100110
1600270708 -> 1011111011000100011000101110100
1601398833 -> 1011111011100110110100000110001
1716808014 -> 1100110010101000110100101001110
1734304870 -> 1100111010111110110010001100110
895891557  -> 110101011001100011100001100101
1681142832 -> 1100100001101000011010000110000

#2 Split the binaries into 8 bits a block (add 0 at front if less than 32 bits)
01000001 01011111 01100010 00110001
01110100 01011111 00110000 01100110
01011111 01100010 00110001 01110100
01011111 01110011 01101000 00110001
01100110 01010100 01101001 01001110
01100111 01011111 01100100 01100110
00110101 01100110 00111000 01100101
01100100 00110100 00110100 00110000

#3 Transfrom to ascii
A_b1t_0f_b1t_sh1fTiNg_df5f8ed440
```

flag: picoCTF{A_b1t_0f_b1t_sh1fTiNg_df5f8ed440}