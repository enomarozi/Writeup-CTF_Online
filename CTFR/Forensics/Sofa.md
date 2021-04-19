<h1><b>Sofa</b></h1>
<pre>
Sofa adalah tempat duduk yang nyaman, Semakin empuk semakin nyaman h3h3

Hint : Cari arti dari S0F0, Kemudian ambil 16 Byte / 32 Bit. Pastikan, Jangan ambil Size dari offset tersebut. Hasil tadi, kalkukasi dengan XOR yang sudah di berikan. Good Luck and Enjoy :D

S0F0 : ???

Download : <a href='https://mega.nz/#!w8Yz2YgY!GE2tgYFnNqDs64XfPPqJoFi-fQjS9Q3z464H2Yn2Mdo'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>SOF0 merupakan bagian SOS maker file JPEG, SOF0 diawali 0xC0 dan diakhiri 0xFF. Langsung saja ambil bytes SOF0 dari file Image.jpeg</p>
<pre>
C0 00 11 08 01 80 02 00 03 01 11 00 02 11 01 03 11 01 FF
</pre>
<p>Sesuai soal, jangan ambil panjang frame dari SOF0 tersebut yang jadinya</p>
<pre>
08 01 80 02 00 03 01 11 00 02 11 01 03 11 01 FF
</pre>
<p>Berikut script python penyelesaiannya</p>

```python3
file = open('sofa.jpg','rb').read()
sofo_file = [i for i in file[0x9e:0xae]][::-1]
for i in range(20):
    sofo_file.append(0)
enc_flag = "43 54 46 52 7b 78 30 72 5f 77 31 74 68 5f 73 30 66 5f 63 34 64 62 f5 6e 34 77 32 4e 73 32 4e 66 33 21 65 82".split(' ')
for i,j in zip(enc_flag,sofo_file[::-1]):
    print(chr(int(i,16)^j),end='')
```
<h3><b>Flag</b></h3>
<pre>
CTFR{x0r_w1th_s0f_c4lcul4t3_s0_g00d}
</pre>
