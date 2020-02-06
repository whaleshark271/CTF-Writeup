# Based
**200 points**
## Description
> To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc 2019shell1.picoctf.com 29594`.
## Hints
> I hear python can convert things.
>
> It might help to have multiple windows open
---
## Writeup
I used several online tools to help completing this challenge. Just search 'Binary/Oct/Hex to text'.

```shell
$ nc 2019shell1.picoctf.com 29594
Let us see how data is stored
lamp
Please give the 01101100 01100001 01101101 01110000 as a word.
...
you have 45 seconds.....

Input:
lamp
Please give me the  163 157 143 153 145 164 as a word.
Input:
socket
Please give me the 736c75646765 as a word.
Input:
sludge
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_e67b1990}
```

flag : picoCTF{learning_about_converting_values_e67b1990}