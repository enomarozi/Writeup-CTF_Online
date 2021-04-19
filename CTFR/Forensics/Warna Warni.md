<h1><b>Warna Warni</b></h1>
<pre>
Mimin diberi sebuah gambar Warna warni alias acak. Tapi mimin enggk paham maksud dari gambar ini, Dan juga mimin diberikan sebuah hint yang mengatakan "Maksimal 127", Coba para hacker bantu mimin translated kan :(

Challenge --> <a href='https://mega.nz/file/woYXmSSJ#3Nb1tOTW1SLR6ImwNmquFwQiiiYCxyCrXc1as-BGgJo'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Periksa semua nilai RGB baik, yang flagnya terdapat pada G(green) dan nilainya kurang dari 127. Berikut script penyelesaiannya</p>

```python3
import cv2

image = cv2.imread('warnawarni.png')
for i in image[:2]:
    for j in i:
        for k in j:
            if k<127:
                print(chr(k),end='')#CTFR{r34d_r9b_1n_1m4g3_1s_aw3s0m3}

```
<h3><b>Flag</b></h3>
<pre>
CTFR{r34d_r9b_1n_1m4g3_1s_aw3s0m3}
</pre>
