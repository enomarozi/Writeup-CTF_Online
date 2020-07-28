<h1><b>The Data Scientist</h1></b>
<pre>
My friend is a data-scientist and he spends his days using Excel or cool python libraries like numpy, 
pandas, or opencv. But this morning he was feeling grumpy and hid my flag in a CSV.

The only thing he told me is that the real hint will be given when you find what the columns mean.

<a href='https://ctflearn.com/challenge/download/919'>the_data_scientist.csv</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Jika dilihat dari jumlah baris yaitu 256 dan kolom yaitu 53, pertama saya duga itu nanti akan mencetak suatu string, jadi disini saya akan menjumlahkan seluruh field
dari masing-masing column dan dibagi 255 yg nantinya akan menjadi nilai desimal yang memunkinkan memuat ASCII</p>

```python
import pandas as pd

data = pd.read_csv("the_data_scientist.csv")
jumlah = 0
for j in data:
    for i in data[j]:
        jumlah += i
    print(chr(int(jumlah//255)),end="")
    jumlah = 0
```
<p>Output Program</p>
<pre>
SET ALL VALUES BETWEEN 64 AND 65 TO BLACK AND SCAN IT
</pre>
<p>Hasil dari program itu ternyata clue, jadi kita akan replace semua nilai antara 64-65 menjadi black</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Untitled.png'>
</p>
<p>Ternyata didapatkan yaitu Encode QR-Code, decrypt QR-Code dengan website <a href='https://webqr.com/'>online</a>, atau dengan script dibawah </p>

```python
from pyzbar import pyzbar
import cv2

img_path = 'Untitled.png'

img = cv2.imread(img_path)

barcodes = pyzbar.decode(img)
print(barcodes)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    print("[INFO] found {} barcode {}".format(barcodeType, barcodeData))

```
<p>Output Program</p>
<pre>
[Decoded(data=b'CTFlearn{m4ch1n3_l34rn1n9_rul35}', type='QRCODE', rect=Rect(left=11, top=7, width=988, height=618), polygon=[Point(x=11, y=621), Point(x=999, y=625), Point(x=994, y=7), Point(x=12, y=8)])]
[INFO] found QRCODE barcode CTFlearn{m4ch1n3_l34rn1n9_rul35}
</pre>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{m4ch1n3_l34rn1n9_rul35}
</pre>
