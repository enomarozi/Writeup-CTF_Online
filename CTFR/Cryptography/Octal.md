<h1><b>Octal</b></h1>
<pre>
Oktal atau sistem bilangan basis delapan adalah sebuah sistem bilangan berbasis delapan. Simbol yang digunakan pada sistem ini adalah 0,1,2,3,4,5,6,7. Konversi Sistem Bilangan Oktal berasal dari Sistem bilangan biner yang dikelompokkan tiap tiga bit biner dari ujung paling kanan.

Flag : 103 124 106 122 173 60 143 164 64 154 137 61 163 137 144 61 146 146 137 167 61 164 150 137 144 63 143 61 155 64 154 175
</pre>
<h3><b>Solution</b></h3>
<p>Conversikan Octal ke Ascii Text</p>

```python
octal = '103 124 106 122 173 60 143 164 64 154 137 61 163 137 144 61 146 146 137 167 61 164 150 137 144 63 143 61 155 64 154 175'.split(' ')
for i in octal:
    print(chr(int(i,8)),end='')#CTFR{0ct4l_1s_d1ff_w1th_d3c1m4l}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{0ct4l_1s_d1ff_w1th_d3c1m4l}
</pre>
