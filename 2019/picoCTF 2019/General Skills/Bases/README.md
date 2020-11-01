# Bases
**100 points**
## Description
> What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.
## Hints
> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
---
## Writeup
This should be encoded with Base64. Base64 encodes binary to ASCII string format using `=` as padding.

```shell
$ echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
l3arn_th3_r0p35
```

flag : picoCTF{l3arn_th3_r0p35}