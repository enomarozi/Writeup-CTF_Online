<h1><b>File Korup</b></h1>
<pre>
Bantu mimin perbaiki file korup dong, soalnya ada gambar privasi mimin

Challenge --> <a href='https://mega.nz/#!U8AGnRYR!F_Q7Rr9SsFKzMR5S9acWje3S5F2VehheqlJA0-e3emo'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Periksa file PNG dengan zsteg, disana terdapat error pada byte header</p>

```console
root@Python:/home/venom/Downloads# zsteg file_korup.png 
[!] #<ZPNG::NotSupported: Unsupported header "\x00\x00\x00\x00\x00\x00\x00\x00" in #<File:file_korup.png>>
root@Python:/home/venom/Downloads# 
```
<p align='justify'>Sedangkan header untuk file PNG yaitu <b>89 50 4E 47 0D 0A 1A 0A</b>, ganti header yang error ke header asli file dengan binary edit tool seperti ghex atau bless, atau dengan script python dibawah</p>

```python3
import cv2
import pytesseract

file = open('file_korup.png','rb').read()
PNG_head = b'\x89PNG\x0d\x0a\x1a\x0a'
file = PNG_head+file[8:]
outF = open('file_recovery.png','wb')
outF.write(file)
outF.close()

image = cv2.imread('file_recovery.png')
print(pytesseract.image_to_string(image)) #CTFR{f1l3_cOrrupt_h4s_b33n_f1x3d}
```

<p align='center'><img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/file_recovery.png'/></p>
<h3><b>Flag</b></h3>
<pre>
CTFR{f1l3_cOrrupt_h4s_b33n_f1x3d}
</pre>
