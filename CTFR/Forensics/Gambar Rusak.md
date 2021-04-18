<h1><b>Gambar Rusak</b></h1>
<pre>
Mimin diberikan gambar rusak dari member disini :(, Para heker tentu tau cara perbaiki nya

Challenge --> <a href='https://mega.nz/#!IgB3RajZ!MwljQpZHA3PV0ln-6Qx_EbEjBSnJIn1CaG-nXOjApOA'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Periksa file dengan zpng tool, dan didapatkan error pada CRCnya</p>

```console
root@Python:/home/venom/Downloads# zpng gambarrusak.png 
[.] image size 528x242, 24bpp, COLOR_RGB
[.] uncompressed imagedata size = 382236 bytes
[.] <Chunk #00 IHDR size=    13, crc=93716b7e, color=2, compression=0, depth=8, filter=0, height=242, interlace=0, width=528> CRC OK
[.] <Chunk #01 sRGB size=     1, crc=aece1ce9 > CRC OK
[.] <Chunk #02 gAMA size=     4, crc=0bfc6105 > CRC OK
[.] <Chunk #03 pHYs size=     9, crc=c76fa864 > CRC OK
[.] <Chunk #04 IDAT size= 21255, crc=6981270e > CRC ERROR
[.] <Chunk #05 \x11\xB1\xE6\xE9 size=90007096, crc=     ??? > CRC ERROR
root@Python:/home/venom/Downloads# 
```
<p align='justify'>Setelah dibuka dengan tool file binary seperti bless, terdapat string <b>"REMOVETHISREMOVETHISREMOVETHISREMOVETHIS"</b> yang membuat CRC menjadi error, maka hapus semua string pada file binary</p>

```python3
import pytesseract
import cv2

file_error = open('gambarrusak.png','rb').read()
file_ok = open('gambar_fix.png','wb')
data = file_error.replace(b'REMOVETHISREMOVETHISREMOVETHISREMOVETHIS',b'')
file_ok.write(data)
file_ok.close()

image = cv2.imread('gambar_fix.png')
print(pytesseract.image_to_string(image)) #CTFR{4nd4_lu4r_b14s4}
```
<p align='center'>
   <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/gambar_rusak_fix.png'>
</p>
<h3><b>Flag</b></h3>
<pre>
CTFR{4nd4_lu4r_b14s4}
</pre>
