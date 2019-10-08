# Paper Trail
**50 points**
## Description
> Something is suspicious about defund's math papers. See if you can find anything in the network packets we've intercepted from his computer.
---
## Writeup
Use Wireshark to open `paper_trail.pcapng`.

Under protocal IRC 85 request or 144 response are some information (at trailer). I went through all of them and put the flag back together.

![Image of IRC data](image0.PNG)

There must be a faster way. Perhaps `scapy`?

flag: actf{fake_math_papers}