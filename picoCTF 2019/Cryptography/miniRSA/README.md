# miniRSA
**300 points**
## Description
> Lets decrypt this: [ciphertext](ciphertext)? Something seems a bit small
## Hints
> RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
> 
> How could having too small an e affect the security of this 2048 bit key?
> 
> Make sure you dont lose precision, the numbers are pretty big (besides the e value)
---
## Writeup
> [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA): When encrypting with low encryption exponents (e.g., e = 3) and small values of the m, (i.e., m < n ^ 1/e) the result of m^e is strictly less than the modulus n. In this case, ciphertexts can be easily decrypted by taking the eth root of the ciphertext over the integers.

The [reason](https://crypto.stackexchange.com/questions/33561/cube-root-attack-rsa-with-low-exponent) why this attack works.

So all we have to do is take cube root of `c` and then convert it to ascii.

flag : picoCTF{n33d_a_lArg3r_e_ff7cfba1}