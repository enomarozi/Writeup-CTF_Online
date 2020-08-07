<h1><b>c0rrupt</h1></b>
<pre>
We found this <a href='https://2019shell1.picoctf.com/static/3435d990f1d20fe3563cbb897b4c96db/mystery'>file</a>. Recover the flag. 
You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file dari raw_bytes dengan perintah xxd</p>

```console
root@Python:/home/venom/Downloads# xxd mystery | head -n 5
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
```
<p>Kemungkinan besar file merupakan PNG Image, resolve semua kesalahan pada header dan chuck file, reference https://en.wikipedia.org/wiki/Portable_Network_Graphics</p>
<p>Kesalahan pertama terdapat pada signature file, signature panjangannya 8 bytes yang sudah merupakan ketetapan</p>
<pre>
Signature file --> 89 65 4E 34 0D 0A B0 AA
Signature benar --> 89 50 4E 47 0D 0A 1A 0A
</pre>
<p>Ganti signature pada file dengan 89 50 4E 47 0D 0A 1A 0A, dan hasilnya</p>

```console
root@Python:/home/venom/Downloads# xxd mystery | head -n 5
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4322 4452  .PNG........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
```
<p>Check file png dengan pngcheck, maka masih terdapat error pada nama chunk Image header(IHDR)nya, setiap chunk panjanganya 4 bytes dan dilanjutkan type 4 bytes berikutnya</p>

```console
root@Python:/home/venom/Downloads# pngcheck mystery_resolve.png 
mystery_resolve.png:  invalid chunk name "C"DR" (43 22 44 52)
ERROR: mystery_resolve.png
```
<pre>
IHDR chunk salah --> 00 00 00 0D 43 22 44 52
IHDR chunk benar --> 00 00 00 0D 49 48 44 52
</pre>
<p>Dan jika dicheck lagi file PNG signaturenya sudah fix tetapi masih terdapat error CRC chunk pada pHYs</p>

```console
root@Python:/home/venom/Downloads# file mystery_resolve.png 
mystery_resolve.png: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
root@Python:/home/venom/Downloads# 
```
<p>Kesalahan ketiga yaitu aspect ration dari Pixel perunit X dan Y chuck pHYs terdiri dari 9 bytes</p>
<pre>
  Pixels per unit, X axis: 4 bytes (unsigned integer)
  Pixels per unit, Y axis: 4 bytes (unsigned integer)
  Unit specifier:          1 byte
</pre>

```console
root@Python:/home/venom/Downloads# pngcheck -v -f mystery_resolve.png 
File: mystery_resolve.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery_resolve.png
```
<p>Nilai pixel X yang membuat aspect rationya tidak konsisten jika dibandingkan dengan Y --> 00 00 16 25<>
<p>Perbaiki aspect ratio X</p>
<pre>
Pixel unit X (salah) --> AA 00 16 25 (2852132389)
Pixel unit X (betul) --> 00 00 16 25 (5669)
</pre>
<p>Hasil analisa selanjutnya terdapat kesalahan pada chunk IDAT</p>

```console
root@Python:/home/venom/Downloads# pngcheck -v -f mystery_resolve.png 
File: mystery_resolve.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery_resolve.png
```
<p>Perbaiki terlebih dahulu chunk IDAT AB 44 45 54 78 --> 49 44 41 54 78</p>
<p>Selanjutnya kita menganalisa IDAT dengan mencari seluruh chunk IDAT</p>

```console
root@Python:/home/venom/Downloads# binwalk -R "IDAT" mystery_resolve.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
87            0x57            Raw signature (IDAT)
65544         0x10008         Raw signature (IDAT)
131080        0x20008         Raw signature (IDAT)
196616        0x30008         Raw signature (IDAT)
```
<p>Yap, IDAT selanjutnya terdapat pada offset 0x10008, kita perlu mengurangi 4 bytes terlebih dahulu untuk memposisi next length IDAT dikurangi posisi akhir IDAT pertama, dan dikurang 0x4 untuk mengarah ke posisi length IDAT pertama</p>
<p>0x10004 - 0x5B - 0x4 = 0xFFA5 --> 00 00 FF A5, ganti nilai length IDAT pertama dengan nilai yang baru didapatkan</p>
<pre>
length IDAT (Salah) --> AA AA FF A5
length IDAT (Benar) --> 00 00 FF A5
</pre>

```console
root@Python:/home/venom/Downloads# pngcheck mystery_resolve.png 
OK: mystery_resolve.png (1642x1095, 24-bit RGB, non-interlaced, 96.3%).
root@Python:/home/venom/Downloads# 
```
<p>Berikut hasil check terakhir ternyata filenya berhasil di resolve, buka file tersebut</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2019/Forensics/Images/mystery_resolve.jpg'>
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{c0rrupt10n_1847995}
</pre>
