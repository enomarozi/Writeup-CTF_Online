<h1><b>Kode Biner</b></h1>
<pre>
Kode biner mewakili teks, instruksi prosesor komputer, atau data lainnya menggunakan sistem dua simbol. Sistem dua simbol yang digunakan seringkali "0" dan "1" dari sistem angka biner. Kode biner memberikan pola digit biner, juga dikenal sebagai bit, untuk setiap karakter, instruksi, dll.

Flag : 01000011 01010100 01000110 01010010 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01011111 00110001 01110011 01011111 01100001 01110111 00110011 01110011 00110000 01101101 00110011 01111101
</pre>
<h3><b>Solution</b></h3>
<p>Decode Biner to Ascii</p>

```python
biner = "01000011 01010100 01000110 01010010 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01011111 00110001 01110011 01011111 01100001 01110111 00110011 01110011 00110000 01101101 00110011 01111101".split(' ')
for i in biner:
    print(chr(int(i,2)),end='')
```
<h3><b>Flag</b></h3>
<pre>
CTFR{b1n4ry_1s_aw3s0m3}
</pre>
