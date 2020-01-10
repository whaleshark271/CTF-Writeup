# How2decompyle
## Description
> What is the file and how to reverse it?
>
> [decompyle](decompyle)
---
## Writeup
Silly me tried to use IDA first instead of checking what file this is. It is a Python 2.7 byte-compiled file. I used `uncompyle6 -o out.py decompyle.pyc` to decompile and got the source code.

``` python
# uncompyle6 version 3.4.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (default, Jul 28 2018, 11:29:29) 
# [GCC 8.1.0]
# Embedded file name: decompyle.py
# Compiled at: 2019-09-22 20:18:03
import string
restrictions = [
 'uudcjkllpuqngqwbujnbhobowpx_kdkp_',
 'f_negcqevyxmauuhthijbwhpjbvalnhnm',
 'dsafqqwxaqtstghrfbxzp_x_xo_kzqxck',
 'mdmqs_tfxbwisprcjutkrsogarmijtcls',
 'kvpsbdddqcyuzrgdomvnmlaymnlbegnur',
 'oykgmfa_cmroybxsgwktlzfitgagwxawu',
 'ewxbxogihhmknjcpbymdxqljvsspnvzfv',
 'izjwevjzooutelioqrbggatwkqfcuzwin',
 'xtbifb_vzsilvyjmyqsxdkrrqwyyiu_vb',
 'watartiplxa_ktzn_ouwzndcrfutffyzd',
 'rqzhdgfhdnbpmomakleqfpmxetpwpobgj',
 'qggdzxprwisr_vkkipgftuvhsizlc_pbz',
 'jerzhlnsegcaqzathfpuufwunakdtceqw',
 'lbvlyyrugffgrwo_v_zrqvqszchqrrljq',
 'aiwuuhzbszvfpidwwkl_wynlujbsbhfox',
 'vmhrizxtiegxdxsqcdoiyxkffloudwtxg',
 'tffjnabob_jbf_qiszdsemczghnjysmah',
 'zrqkppvynlkelnevngwlkhgaputhoagtt',
 'nl_oojyafwoqccbedijmigpedkdzglq_f',
 'cksy_skctjlyxktuzchvstunyvcvabomc',
 'ppcxleeguvhvhengmvac_bykhzqohjuei',
 '_clmaicjrrzhwd_fescyaejtbyefxyihy',
 'hhopvwsmjtpjiffzatyhjrev_dwnsidyo',
 'sjevtrmkkk_zjalxrxfovjsbcxjx_pskp',
 'gnynwuuqypddbsylparpcczqimimqmvdl',
 'bxitcmhnmanwuhvjxnqeoiimlegrmkjra']
capital = [
 0, 4, 9, 19, 23, 26]
flag = raw_input('Please tell me something : ').lower()
flag = flag.lower()
if len(flag) != len(restrictions[0]):
    print 'No......You are wrong orzzzzz'
    exit(0)
for f in range(len(flag)):
    for r in restrictions:
        if flag[f] not in string.lowercase + '_' or flag[f] == r[f]:
            print 'No......You are wrong orzzzzzzzzzzzz'
            exit(0)

cap_flag = ''
for f in range(len(flag)):
    if f in capital:
        cap_flag += flag[f].upper()
    else:
        cap_flag += flag[f]

print 'Yeah, you got it !\nBambooFox{' + cap_flag + '}\n'
```

There are 26 restrictions and each is 33 characters long. The code first checks which character is not in the first character of the 26 restrcitions from a~z and '_', then goes on to check the second character. Therefore, the flag is consists of characters that are not in the restrictions' positions and it should be of length 33. After knowing this, it is simple to write a script to reverse the process.

[My script](solve.py)

flag : BambooFox{You_Know_Decompyle_And_Do_Reverse}