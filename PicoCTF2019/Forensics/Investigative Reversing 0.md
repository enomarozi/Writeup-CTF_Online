<h1>Investigative Reversing 0</h1>
<h3>Description</h3>
<label>We have recovered a <a href='https://challenge-files.picoctf.net/c_fickle_tempest/273ec6d35c80adde1b9b4e3eadb98151e731e38fb28add3dd11704103977fe44/mystery'>binary</a> and an <a href='https://challenge-files.picoctf.net/c_fickle_tempest/273ec6d35c80adde1b9b4e3eadb98151e731e38fb28add3dd11704103977fe44/mystery.png'>image</a>. See what you can make of it. There should be a flag somewhere.</label>
<h3>Solution</h3>
<label>Pengetahuan Forensic dan Reversing (file mystery digunakan untuk menyembunyikan pesan ke mystery.png)</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/PicoCTF]
└─# zsteg -a mystery.png 
[?] 26 bytes of extra data after image end (IEND), offset = 0x1e873
extradata:0         .. 
    00000000: 70 69 63 6f 43 54 4b 80  6b 35 7a 73 69 64 36 71  |picoCTK.k5zsid6q|
    00000010: 5f 62 33 65 61 33 31 39  39 7d                    |_b3ea3199}      |
imagedata           .. text: "PPP@@@@@@@@@@@@"
```

```python3
local_54 = 6
part1 = "picoCT"
print(part1,end='')
text = '70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 62 33 65 61 33 31 39 39 7d'.split(' ')
for i in range(local_54, 0xf):
    print(chr(int(text[i],16)-0x5),end='')
print("?",end='')
local_50 = 0x10
for i in range(local_50, 0x1a):
    print(chr(int(text[i],16)),end='')
```
<h3>Flag</h3>
<pre>
picoCTF{f0und_1t_b3ea3199}
</pre>
