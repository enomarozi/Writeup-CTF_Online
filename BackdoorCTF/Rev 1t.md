<h1><b>Rev 1t</b></h1>
<pre>
Python is an interesting language. 
SC4R is quite confident that you will not be able to rev it. Disprove him.

http://static.beast.sdslabs.co/static/noob/index.pyc
</pre>
<h3><b>Solution</b></h3>
<p>Merupakan file execute python, decompile file dengan uncompyle6</p>

```console
root@Python:/home/venom/Downloads# pip3 install uncompyle6
Requirement already satisfied: uncompyle6 in /usr/local/lib/python3.8/dist-packages (3.7.2)
Requirement already satisfied: xdis<5.1.0,>=4.7.0 in /usr/local/lib/python3.8/dist-packages (from uncompyle6) (5.0.1)
Requirement already satisfied: spark-parser<1.9.0,>=1.8.9 in /usr/local/lib/python3.8/dist-packages (from uncompyle6) (1.8.9)
Requirement already satisfied: click in /usr/lib/python3/dist-packages (from spark-parser<1.9.0,>=1.8.9->uncompyle6) (7.0)
root@Python:/home/venom/Downloads# uncompyle6 index.pyc > decompile.py
root@Python:/home/venom/Downloads# idle-python3.8 decompile.py 
```
<p>Hasil decompile</p>

```python
# uncompyle6 version 3.7.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.3 (default, May 14 2020, 11:03:12) 
# [GCC 9.3.0]
# Embedded file name: index.py
# Compiled at: 2020-01-07 13:27:49
import string
interesting = ['uudacjkllpuqngqwbujnbhopx_kdkp_',
 'f_ncegcqevyxmauuhthijbwbvalnhnm',
 'dsadfqqwxaqtstghrfbxzp_o_kzqxck',
 'mdmeqs_tfxbwisprcjutkrsrmijtcls',
 'kvpfsbdddqcyuzrgdomvnmlnlbegnur',
 'oykggmfa_cmroybxsgwktlzgagwxawu',
 'ewxhbxogihhmknjcpbymdxqsspnvzfv',
 'izjiwevjzooutelioqrbggaqfcuzwin',
 'xtbjifb_vzsilvyjmyqsxdkwyyiu_vb',
 'watkartiplxa_ktzn_ouwznfutffyzd',
 'rqzlhdgfhdnbpmomakleqfptpwpobgj',
 'qggmdzxprwisr_vkkipgftuizlc_pbz',
 'jernzhlnsegcaqzathfpuufakdtceqw',
 'lbvolyyrugffgrwo_v_zrqvchqrrljq',
 'aiwpuuhzbszvfpidwwkl_wyjbsbhfox',
 'vmhqrizxtiegxdxsqcdoiyxloudwtxg',
 'tffrjnabob_jbf_qiszdsemhnjysmah',
 'zrqskppvynlkelnevngwlkhuthoagtt',
 'yl_toojyafwoqccbedijmigkdzglq_f',
 'cksuy_skctjlyxktuzchvstvcvabomc',
 'ppcvxleeguvhvhengmvac_bzqohjuei',
 '_clwmaicjrrzhwd_fescyaeyefxyihy',
 'hhuxpvwsmjtpjiffzatyhjrdwnsidyo',
 'sjeyvtrmkkk_zjalxrxfovjxjx_pskp',
 'gnyznwuuqypddbsylparpccmimqmvdl',
 'bxi_tcmhnmanwuhvjxnqeoiegrmkjra']
flag = raw_input('N00b enter something : ').lower()
flag = flag.lower()
if len(flag) != len(interesting[0]):
    print 'No No No No'
    exit(0)
for f in range(len(flag)):
    for r in interesting:
        if flag[f] not in string.lowercase + '_' or flag[f] == r[f]:
            print 'No......No'
            exit(0)

my_flag = ''
for f in range(len(flag)):
    my_flag += flag[f]

print ' You did it !\nflag{' + my_flag + '}\n'
# okay decompiling index.pyc
```
<p>Jika kita perhatikan disana terdapat list string, dan fungsi statment yang mengembalikan nilai True jika panjang flag sama dengan satu index list. Selanjutnya 
pada looping dibawahnya yaitu pengecekan jika pada satu indexs list tidak terdapat string string.lowercase+"_" maka program exit(0). Dan terakhir itu jika flag bernilai True</p>
<p>Oke, kita akan me-reversing operasi pada program</p>

```python
import string

letter = string.ascii_lowercase+"_"

interesting = ['uudacjkllpuqngqwbujnbhopx_kdkp_','f_ncegcqevyxmauuhthijbwbvalnhnm',
 'dsadfqqwxaqtstghrfbxzp_o_kzqxck','mdmeqs_tfxbwisprcjutkrsrmijtcls',
 'kvpfsbdddqcyuzrgdomvnmlnlbegnur','oykggmfa_cmroybxsgwktlzgagwxawu',
 'ewxhbxogihhmknjcpbymdxqsspnvzfv','izjiwevjzooutelioqrbggaqfcuzwin',
 'xtbjifb_vzsilvyjmyqsxdkwyyiu_vb','watkartiplxa_ktzn_ouwznfutffyzd',
 'rqzlhdgfhdnbpmomakleqfptpwpobgj','qggmdzxprwisr_vkkipgftuizlc_pbz',
 'jernzhlnsegcaqzathfpuufakdtceqw','lbvolyyrugffgrwo_v_zrqvchqrrljq',
 'aiwpuuhzbszvfpidwwkl_wyjbsbhfox','vmhqrizxtiegxdxsqcdoiyxloudwtxg',
 'tffrjnabob_jbf_qiszdsemhnjysmah','zrqskppvynlkelnevngwlkhuthoagtt',
 'yl_toojyafwoqccbedijmigkdzglq_f','cksuy_skctjlyxktuzchvstvcvabomc',
 'ppcvxleeguvhvhengmvac_bzqohjuei','_clwmaicjrrzhwd_fescyaeyefxyihy',
 'hhuxpvwsmjtpjiffzatyhjrdwnsidyo','sjeyvtrmkkk_zjalxrxfovjxjx_pskp',
 'gnyznwuuqypddbsylparpccmimqmvdl','bxi_tcmhnmanwuhvjxnqeoiegrmkjra']

flag_part = ""
for i in range(31):
    for j in range(26):
        flag_part += interesting[j][i]
    for part in letter:
        if part not in flag_part:
            print(part,end="")
    flag_part = ""

```
<h3><b>Flag</b></h3>
<pre>
flag{noob_know_decompyle_and_reverse}
</pre>
