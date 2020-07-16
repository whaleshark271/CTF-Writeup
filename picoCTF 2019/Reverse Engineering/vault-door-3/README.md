# vault-door-training
**200 points**
## Description
> This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java]().
## Hints
> Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
---
## Writeup
```Java
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
```
First for loop puts password[0] ~ password[7] at buffer[0] ~ buffer[7], which is `jU5t_a_s`

```Java
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
```
Second for loop puts password[15] ~ password[8] at buffer[8] ~ buffer[15], so it should be `1mpl3_an`, reverse of `na_3lpm1`

```Java
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
```
```text
# is thrid for loop, * is fourth for loop
* buffer[31] = password[31] = b
# buffer[16] = password[30] = d
* buffer[29] = password[29] = 5
# buffer[18] = password[28] = 3
* buffer[27] = password[27] = f
# buffer[20] = password[26] = 7
* buffer[25] = password[25] = _
# buffer[22] = password[24] = u
* buffer[23] = password[23] = _
# buffer[24] = password[22] = 4
* buffer[21] = password[21] = _
# buffer[26] = password[20] = m
* buffer[19] = password[19] = 4
# buffer[28] = password[18] = r
* buffer[17] = password[17] = g
# buffer[30] = password[16] = 4
```

flag: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_7f35db}