<h1><b>babyrev</b></h1>
<pre>
Link: babyrev

Hint 1: https://ghidra-sre.org/

HInt 2: https://en.wikipedia.org/wiki/XOR_cipher
</pre>
<h3><b>Solution</b></h3>
<p>Decompiler file dengan ghidra, maka terdapat string dan key untuk operasi xor sesuai pada hint 2</p>
<p>String encoding</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/babyrev.jpg" width=900>
</p>
<p>Key xor</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/babyrev1.jpg" width=900>
</p>

```python
encode = [0xc2, 0x32, 0xd6, 0xe5, 0x88, 0xde, 0x89,  0x7, 0xb5, 0xde, 0x6b,
          0xc6, 0x6c, 0xa0, 0x9e, 0x8a, 0x43, 0xb3, 0xfc, 0x73, 0x2e, 0xcd,
          0x83, 0xf4, 0x94, 0x63, 0xd9, 0x0]
key = [0xa4, 0x5e, 0xb7, 0x82, 0xf3, 0xac, 0xbd, 0x71, 0x86, 0xac, 0x18, 0xf7,
       0x2, 0xc7, 0xc1, 0xf2, 0x73, 0xc1, 0xa3, 0x1a, 0x5d, 0x92, 0xe6, 0xc0,
       0xe7, 0x1a, 0xa4, 0x0]
for i,j in zip(encode,key):
    print(chr(i^j),end="")

```
<h3><b>Flag</b></h3>
<pre>
flag{r4v3rs1ng_x0r_is_e4sy}
</pre>
