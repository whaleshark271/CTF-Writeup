# For Beginner
## Description
>BnUhxCM7ETtcx0oaIDUavFMbvCY0y1Yby2QhAD1HNDwlwW99
>
>Dvoxlnv gl gsv yzojh XGU. Qfhg szev ufm!
---
## Writeup
Clearly we have to solve the cipher in the description.

First look at the second line. It looks like a substitution cipher. Let's search for some decoders online and try it out. Unfortunately, the text is too short to generate a fully readable text (It is possible to guess some words though). I have tried cracking the cipher on my own until I found a [decoder](https://cryptii.com/pipes/alphabetical-substitution) that just so happens to have the same key, which is `zyxwvutsrqponmlkjihgfedcba`. So now the cipher text can be translated to "YmFscXN7VGgxc0lzRWFzeUNyeXB0b1Byb2JsZW1SMWdodD99" and "Welcome to the balqs CTF. Just have fun!"

The first line should be a flag, but it doesn't look like one yet. Let's try a Base64 decoder and found the flag.

flag : balqs{Th1sIsEasyCryptoProblemR1ght?}