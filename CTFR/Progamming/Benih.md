<h1><b>Benih</b></h1>
<pre>
Mimin di berikan benih sama member nih, coba cari tau dari tersebut. Oiya jangan lupa nama benih nya "CTFR"

Challenge --> <a href='https://mega.nz/#!AkByiJiA!HHYR3Zxrh52ueX0i4D2QyPIx4TX2mm1gSX6ztSMsnvY'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p align='justify'>PRNG (Pseudo Random Number Generator) yaitu suatu algoritma yang dapat menampilkan nilai acak yang tidak dapat diprediksi atau diketahui. Seed merupakan
nilai pembangkit dari sebuah nilai acak tersebut. Jadi kelemahan dari encrypt PRNG ini yaitu seed yang sudah diberikan yaitu "CTFR" dan operasi dijadikan pengurangan</p>

```python2
import random

encrypted = open("encrypt.txt", "r").read()
random.seed('CTFR')
flag = ""
for x in encrypted:
    p = random.randint(0, 14)
    flag += chr(ord(x) - p)

print flag
```
<p>Output</p>
<pre>
CTFR merupakan Website Platform Capture The Flag dengan Buatan sendiri. Dan tentunya native yaa :D, Btw nih flagnya : CTFR{b3n1h_ul4r_p1t0n}
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{b3n1h_ul4r_p1t0n}
</pre>
