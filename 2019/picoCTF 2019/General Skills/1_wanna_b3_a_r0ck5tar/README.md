# 1_wanna_b3_a_r0ck5tar
**350 points**
## Description
> I wrote you another [song](lyrics.txt). Put the flag in the picoCTF{} flag format
---
## Writeup
This is a continuation of the problem `mus1c`. Running the lyrics on the [website]() doesn't work anymore as it doesn't give any output. So I decompiled the lyrics to python using the [transpiler](https://github.com/yyyyyyyan/rockstar-py).

```python
Rocknroll = True
Silence = False
a_guitar = 19
Tommy = 44
Music = 160
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!)
        Music = 79
        Jamming = 78
        print(Music!)
        print(Jamming!)
        Tommy = 74
        print(Tommy!)
        They are dazzled audiences
        print(it!)
        Rock = 86
        print(it!)
        Tommy = 73
        print(it!)
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break
```

"66 79 78 74 86 73" translates to BONJVI. I'm guessing it should be Bonjovi, the singer. Not sure why it's missing an O.

After deleting a few lines that seems like if else statements, the code directly output 66 79 78 74 79 86 73, which contains the missing O.

Deleted lines:
```python
Listen to the music # input()          
If the music is a guitar # if statement               
Say "Keep on rocking!"                
Listen to the rhythm # input()
If the rhythm without Music is nothing # if statement

Else Whisper "That ain't it, Chief" # else              
Break it down 
```

flag : picoCTF{BONJOVI}