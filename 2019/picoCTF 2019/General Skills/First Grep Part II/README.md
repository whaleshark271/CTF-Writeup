# First Grep: Part II
**200 points**
## Description
> Can you find the flag in /problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443/files on the shell server? Remember to use grep.
## Hints
> grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)
---
## Writeup
There are way too much files to check, so I used `grep -r` to recursively read all files under each directory.

```shell
beershark@pico-2019-shell1:/$ cd /problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443/files
beershark@pico-2019-shell1:/problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443/files$ ls
files0  files1  files10  files2  files3  files4  files5  files6  files7  files8  files9
beershark@pico-2019-shell1:/problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443/files$ grep -r "pico"
files6/file23:picoCTF{grep_r_to_find_this_0898e9c9}
```

flag : picoCTF{grep_r_to_find_this_0898e9c9}