# Easy1
**100 points**
## Description
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this [table]() to solve it?. 
## Hints
> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
>
> Please use all caps for the message.
---
## Writeup
Use the left characters as key. Find the ciphertext letter in the row, and look up the line to find the plaintext letter.

For example, the first key letter is 'S'. Look at the 'S' row, and find the letter 'U' on that row, then look upward the line to find the letter 'C'. That would be the first letter of the plaintext.

flag : picoCTF{CRYPTOISFUN}