# Diffie
**300 points**
## Description
> You found the following conversation between Alice, a professional cryptocurrency trader, and Bob, a well-known Twitch simp. They bragged that no one can know their secret because they used a super secure secret exchange protocol with "huuuuge" numbers.
>
> Alice: Let's use 999331 and 7.
>
> Bob: Ok
>
> Alice: I got 858076.
>
> Bob: Ok
>
> Alice: What is your number?
>
> Bob: 346579
>
> Alice: Sounds good. Do you know the secret?
>
> Bob: Yes
>
> Bob: Do you know the secret?
>
> Alice: Yes
>
> The flag is the shared secret in decimal form, not surrounded by utflag{}.
>
> --gg
---
## Writeup
This is [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange). The modulus 999331 isn't that big. Try brute-forcing Alice and Bob's secret value.

flag: 364040