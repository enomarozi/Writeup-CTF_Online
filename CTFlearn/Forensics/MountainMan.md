<h1><b>MountainMan</h1></b>
<pre>
Don't be fooled by two 0xffd9 markers. xor is your friend.

<a href='https://ctflearn.com/challenge/download/888'>MountainMan.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Sesuai soal, hasil identifikasi file terdapat 2 EOF(End Of File) pada JPG, dan kita diminta untuk melakukan operasi XOR terhadap EOF yg kedua</p>
<pre>
EOF --> 88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6
</pre>
<p>Jika kita ketahui format flag yaitu "CTFlearn" yang nilai hexanya --> 43 54 46 6c 65 61 72 6e</p>
<p>Dan jika kita lalukan reversing dengan operasi xor</p>

```python
flag_enc = "88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6".split(" ")
key = "43 54 46 6c 65 61 72".split(" ")
for i,j in zip(flag_enc,key):
    print(hex(int(i,16)^int(j,16)),end=" ")
```
<p>maka didapatkan nilai hexa --> cb cb cb cb cb cb cb</p>
<p>Jadi key untuk flag yaitu 0xcb atau 203 dalam desimal</p>

```python
flag_enc = "88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6".split(' ')
key = 'CB CB'.split(" ")*len(flag_enc)
for i,j in zip(flag_enc,key):
    print(chr(int(i,16)^int(j,16)),end='')
```

</b><h3>Flag</h3></b>
<pre>
CTFlearn{Ubuntu_r0ck5}
</pre>
