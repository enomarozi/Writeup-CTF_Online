<h1><b>XOR</b></h1>
<pre>
XOR adalah dua syarat logis, yang menghasilkan true hanya jika kedua masukan sama. XOR juga biasanya digunakan sebagai enkripsi untuk menjaga keamanan data. Nah coba Decode hasil XOR Enkripsi ini dengan Key "FLAG".

Flag : 051807153d347135197d3218273b72347621243a
</pre>
<h3><b>Solution</b></h3>
<p>Lakukan operasi xor dari Enkripsi Flag dengan Key=FLAG</p>

```python
flag = bytes.fromhex('051807153d347135197d3218273b72347621243a')
key = 'FLAG'*10
for i,j in zip(flag,key):
    print(chr(i^ord(j)),end='') #CTFR{x0r_1s_aw3s0me}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{x0r_1s_aw3s0me}
</pre>
