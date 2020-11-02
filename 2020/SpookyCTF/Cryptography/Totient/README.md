# Totient
**300 points**
## Description
> Using two primes for RSA seems like overkill.
>
> I'll just use the same one twice :)
>
> by hukc
---
## Writeup
Since the problem uses the same prime that means n = p^2. The tricky part is totient(p^2) = p^2 - p and not (p-1)^2. See [explanation](https://en.wikipedia.org/wiki/Euler%27s_totient_function#Value_of_phi_for_a_prime_power_argument).

flag: utflag{lol_sqrt_kinda_ez}