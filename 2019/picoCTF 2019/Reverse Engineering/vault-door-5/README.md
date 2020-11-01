# vault-door-5
**300 points**
## Description
> In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](VaultDoor5.java)
## Hints
> You may find an encoder/decoder tool helpful, such as https://encoding.tools/
>
> Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.
---
## Writeup
* [base64 wiki](https://en.wikipedia.org/wiki/Base64)
* [URL encoding wiki](https://en.wikipedia.org/wiki/Percent-encoding)
* [base64 online tool](https://www.base64decode.org/)
* [URL encoding online tool](https://www.urldecoder.org/)

```
JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTY2JTMzJTMwJTM5JTY0JTM0JTMw
=== base64 decode ===
%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%30%66%33%30%39%64%34%30
=== URL decode ===
c0nv3rt1ng_fr0m_ba5e_64_0f309d40
```

flag: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0f309d40}