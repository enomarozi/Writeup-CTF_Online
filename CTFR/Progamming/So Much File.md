<h1><b>So Much File</b></h1>
<pre>
File yang ada pada berangkas .zip ini sangat banyak sekali! Bantu mimin dapatkan arti dari file yang sangat banyak ini!!

Challenge --> <a href='https://mega.nz/#!goQliKLa!VfwsnHSFyEW7C6SHcpUbHAG3BbL-EZAyImKW3RoFUc0'></a>
</pre>
<h3><b>Solution</b></h3>
<p>Buka dan read semua file.txt</p>

```python3
import os

flag = ''
for i in range(0,2025):
    file = open('Searchme/'+str(i)+".txt",'r').read()
    flag += file
    if len(file) > 0:
        print(str(i).ljust(4,' '),":",file)
print('\nFlag IS',flag)
```
<p>Output</p>
<pre>
0    : C
45   : T
90   : F
135  : R
180  : {
225  : p
270  : y
315  : t
360  : h
405  : 0
450  : n
495  : _
540  : 5
585  : c
630  : r
675  : 1
720  : p
765  : t
810  : _
855  : m
900  : 4
945  : k
990  : 3
1035 : _
1080 : y
1125 : o
1170 : u
1215 : _
1260 : 3
1305 : 4
1350 : s
1395 : y
1440 : _
1485 : t
1530 : 0
1575 : _
1620 : s
1665 : 0
1710 : l
1755 : v
1800 : 3
1845 : _
1890 : 1
1935 : t
1980 : }

Flag IS CTFR{pyth0n_5cr1pt_m4k3_you_34sy_t0_s0lv3_1t}
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{pyth0n_5cr1pt_m4k3_you_34sy_t0_s0lv3_1t}
</pre>
