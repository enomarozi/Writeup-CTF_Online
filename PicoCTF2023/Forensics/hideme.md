<h1>hideme</h1>
<h3>Description</h3>
<p>Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye <a href='https://artifacts.picoctf.net/c/257/flag.png'>here</a>.</p>
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# zsteg -a flag.png 
[?] 3281 bytes of extra data after image end (IEND), offset = 0x9b3b
extradata:0         .. file: Zip archive data, at least v1.0 to extract, compression method=store
    00000000: 50 4b 03 04 0a 00 00 00  00 00 38 10 70 56 00 00  |PK........8.pV..|
    00000010: 00 00 00 00 00 00 00 00  00 00 07 00 1c 00 73 65  |..............se|
    00000020: 63 72 65 74 2f 55 54 09  00 03 8b 78 12 64 8b 78  |cret/UT....x.d.x|
    00000030: 12 64 75 78 0b 00 01 04  00 00 00 00 04 00 00 00  |.dux............|
    00000040: 00 50 4b 03 04 14 00 00  00 08 00 38 10 70 56 f5  |.PK........8.pV.|
    00000050: 23 0b f8 8f 0b 00 00 24  0c 00 00 0f 00 1c 00 73  |#......$.......s|
    00000060: 65 63 72 65 74 2f 66 6c  61 67 2e 70 6e 67 55 54  |ecret/flag.pngUT|
    00000070: 09 00 03 8b 78 12 64 8b  78 12 64 75 78 0b 00 01  |....x.d.x.dux...|
    00000080: 04 00 00 00 00 04 00 00  00 00 cd 56 6b 3c d3 0f  |...........Vk<..|
    00000090: 17 ff a1 b4 94 4b e5 9a  88 62 ca c8 90 db 44 35  |.....K...b....D5|
    000000a0: 64 b9 93 6b 26 c6 58 fe  32 94 59 99 4c 35 22 45  |d..k&.X.2.Y.L5"E|
    000000b0: 92 dc af 1b 62 b9 cc 2c  99 7b 62 2e 49 31 94 5c  |....b..,.{b.I1.\|
    000000c0: 1e 95 26 d7 c4 5c 26 f3  78 5e 3e 2f 9e f7 cf 79  |..&..\&.x^>/...y|
    000000d0: 71 be e7 fb 3d e7 bc 3b  e7 7c 4e 82 83 9d a5 a8  |q...=..;.|N.....|
    000000e0: c8 51 11 00 00 44 2f 23  cc 9d 00 40 d0 7d 37 d6  |.Q...D/#...@.}7.|
    000000f0: 91 d8 75 00 37 18 ec ba  0b 7b 30 17 6d 2f 02 00  |..u.7....{0.m/..|
```
<p>Terdapat signature ZIP pada file PNG offset (0x9b3b)</p>

```python3
with open("flag.png","rb")as f:
    f.seek(0x9b3b)
    binary_data = f.read(-1)
    with open("flag.zip","wb") as wzip:
        wzip.write(binary_data)
        wzip.close()
        f.close()
 
```
<p>Ekstrak File zip, dan open file flag.png</p>
<h3>Flag</h3>
<pre>picoCTF{Hiddinng_An_imag3_within_@n_ima9e_dc2ab58f}</pre>
