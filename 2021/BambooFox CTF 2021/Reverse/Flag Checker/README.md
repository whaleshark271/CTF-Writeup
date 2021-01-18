# Flag Checker
## Description
> [upload](upload)
>
> author: CSY54
---
## Writeup
Ah...Verilog...My biggest enemy >:(

So the code basically takes each character of the flag (8 bits) and run it through the magic function 4 times, then check if the output is equal to the target.

I initially wanted to reverse the function, but I didn't know how to reverse the case value since it requires the input value. I decided to make a mapping table that maps characters through magic functions to the target value (see [table.V](table.V)). I then manually assemble the flag characters from the given target values. I'm sure there is a smarter way though.

Beware that some characters are mapped to the same value, like both `1` and `_` are mapped to 245.

flag : flag{v3ry_v3r1log_f14g_ch3ck3r!}