<h1><b>Balik Gambar</b></h1>
<pre>
Mimin disuruh balik gambar, cuman enggk bisa dibuka :(. Katanya "File Korup" Kok bisa korup yaa, padahal mimin enggak pernah apa-apain ini file. Coba bantu di cek deh yaa

Challenge --> <a href='https://mega.nz/#!hl5gzCyY!xKNSvGyjtpwaLU4Q9aLvoHK-XLkWWspitQ6Cr3KVv8s'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Buka file dengan binary data seperti bless atau xxd, yang hasilnya header dari file yaitu DNEI. Itu merupakan EOF dari file PNG</p>

```console
root@Python:/home/venom/Downloads# xxd balikgambarnya.png | head -5
00000000: 8260 42ae 444e 4549 0000 0000 eaef b7f7  .`B.DNEI........
00000010: 5c02 a247 005f ff7f f65a 7d52 533d 0eee  \..G._...Z}RS=..
00000020: ee06 5843 84d4 8579 be9e 83c8 8421 8245  ..XC...y.....!.E
00000030: 262a 7ce2 2a25 9fc7 c2a2 e30d 00cb 0876  &*|.*%.........v
00000040: 9feb d251 ecf3 c588 4304 8f46 2afb 492e  ...Q....C..F*.I.
root@Python:/home/venom/Downloads# 
```
<p>Balikan binary data dari file PNG tersebut</p>

```python3
import pytesseract
import cv2

file_open = open('balikgambarnya.png','rb').read()[::-1]
file_save = open('gambar_fix.png','wb')
file_save.write(file_open)
file_save.close()

image = cv2.imread('gambar_fix.png')
ret, thresh = cv2.threshold(image,1,255,cv2.THRESH_BINARY)
print(pytesseract.image_to_string(thresh))#CTFR{ r3v3rs3_1m4g3_h3x }
cv2.imshow('flag',thresh)
cv2.waitKey(0)
```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/gambar_fix_terbalik.png'>
</p>
<h3><b>Flag</b></h3>
<pre>
CTFR{ r3v3rs3_1m4g3_h3x }
</pre>
