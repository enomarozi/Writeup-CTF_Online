<h1><b>Hexadecimal</b></h1>
<pre>
Heksadesimal atau sistem bilangan basis enam belas adalah sebuah sistem bilangan yang menggunakan 16 simbol. Berbeda dengan sistem bilangan desimal, simbol yang digunakan dari sistem ini adalah angka 0 sampai 9, ditambah dengan 6 simbol lainnya dengan menggunakan huruf A hingga F.

Flag : 435446527b68337834643363316d346c5f31735f61773373306d337d
</pre>
<h3><b>Solution</b></h3>
<p>Decode Hexa to Ascii</p>

```python
hexa = "435446527b68337834643363316d346c5f31735f61773373306d337d"
print(bytes.fromhex(hexa).decode('ascii'))
```
<h3><b>Flag</b></h3>
<pre>
CTFR{h3x4d3c1m4l_1s_aw3s0m3}
</pre>
