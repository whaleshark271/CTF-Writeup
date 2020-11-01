# waves over lambda
**300 points**
## Description
> We made alot of substitutions to encrypt this. Can you decrypt it? Connect with `nc 2019shell1.picoctf.com 21903`.
## Hints
> Flag is not in the usual flag format
---
## Writeup
A lot of substitutions is basically just one substitution. I used [this solver](https://www.guballa.de/substitution-solver) to break the cipher.

```
-------------------------------------------------------------------------------
xjamelgy uses wy hjbe zvlm - zesdbsaxh_wy_x_jcse_vltpnl_cvaualyygt
-------------------------------------------------------------------------------
fs fses ajg tbxu tjes gula l dblegse jz la ujbe jbg jz jbe yuwo gwvv fs ylf use ywak, lan gusa w banseygjjn zje gus zweyg gwts fulg fly tslag ph l yuwo zjbansewam wa gus ysl.  w tbyg lxkajfvsnms w uln ulenvh shsy gj vjjk bo fusa gus ysltsa gjvn ts yus fly ywakwam; zje zejt gus tjtsag gulg gush elguse obg ts wagj gus pjlg gula gulg w twmug ps ylwn gj mj wa, th usleg fly, ly wg fses, nsln fwguwa ts, olegvh fwgu zewmug, olegvh fwgu ujeeje jz twan, lan gus gujbmugy jz fulg fly hsg pszjes ts.
```

```
congrats here is your flag - frequency_is_c_over_lambda_vlnhnasstm
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.
```

flag : picoCTF{frequency_is_c_over_lambda_vlnhnasstm}