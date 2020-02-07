# Tapping
**200 points**
## Description
> Theres tapping coming in from the wires. What's it saying `nc 2019shell1.picoctf.com 45168`.
## Hints
> What kind of encoding uses dashes and dots?
>
> The flag is in the format PICOCTF{}
---
## Writeup
```shell
$ nc 2019shell1.picoctf.com 45168
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ...-- ....- ---.. ---.. ---.. --... .---- ----- ..... }
```

This is clearly morse code.

flag : PICOCTF{M0RS3C0D31SFUN348887105}