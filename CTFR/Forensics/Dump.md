<h1><b>Dump</b></h1>
<pre>
Pada gambar ini terdapat flag yang disembunyikan di dalam hex tersebut. Tolong carikan yaah :(
Hint: Pakai Hexdump untuk menyelesaikan Challenge ini

Challenge --> <a href='https://mega.nz/#!llQi1LCB!8qybw_QiJsiVB7xMCXyRMMGcJBGshSxTohTdvsRO8xE'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Periksa file dengan tool zpng atau zsteg, dan disana terdapat extra dapa pada offest ke 0x69400=431104 setelah EOF</p>

```console
root@Python:/home/venom/Downloads# zsteg kocheng_dipukul.png 
[?] 55 bytes of extra data after image end (IEND), offset = 0x69400
extradata:0         .. 

    00000000: 43 00 54 00 46 00 52 00  7b 00 68 00 33 00 78 00  |C.T.F.R.{.h.3.x.|
    00000010: 5f 00 64 00 75 00 6d 00  70 00 5f 00 31 00 6e 00  |_.d.u.m.p._.1.n.|
    00000020: 5f 00 31 00 6d 00 34 00  67 00 33 00 5f 00 66 00  |_.1.m.4.g.3._.f.|
    00000030: 31 00 6c 00 33 00 7d                              |1.l.3.}         |
b3,b,lsb,xy         .. text: "y\\V\n'*f1"
b4,g,lsb,xy         .. text: "#%2\"\"\"$ETDDDDDv5R2#4#V\n"
b4,b,lsb,xy         .. text: "WvgegUfT52! 7G"
b4,bgr,msb,xy       .. text: "1 11(9\\c"
```
<p>Script Python</p>

```python3
file = open('kocheng_dipukul.png','rb').read()
for i in file[431104:431159]:
    print(chr(i),end='')#CTFR{h3x_dump_1n_1m4g3_f1l3}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{h3x_dump_1n_1m4g3_f1l3}
</pre>
