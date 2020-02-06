# where_is_the_file
**200 points**
## Description
> I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0.
## Hints
> What command can see/read files?
>
> What's in the manual page of ls?
---
## Writeup
```shell
beershark@pico-2019-shell1:~$ cd /problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0
beershark@pico-2019-shell1:/problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0$ ls
beershark@pico-2019-shell1:/problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0$ ls -a
.  ..  .cant_see_me
beershark@pico-2019-shell1:/problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0$ cat .cant_see_me
picoCTF{w3ll_that_d1dnt_w0RK_a88d16e4}
```

flag : picoCTF{w3ll_that_d1dnt_w0RK_a88d16e4}