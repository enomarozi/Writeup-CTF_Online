<h1><b>Bobby Toe's iPad</h1></b>
<pre>
Here is a pic of my friend Bobby Toe. while he's happy to give you his iPad, he's not as willing to give you the flag. 
can you get it from him? here is an image of Bobby Toe: 
https://mega.nz/#!iWAm2KJL!2uRVDKrHOWryZkZNW6leV0sQMh-b0-AYQksa3i-A3Eg
</pre>
</b><h3>Solution</h3></b>
<p>Check dengan stegsolve pada mode red plane 0, disana terdapat encryptext</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Boby_solve1.jpg'>
</p>

```console
root@Python:/home/venom/Downloads# zsteg bobbytoesipad.png 
[?] 5889 bytes of extra data after image end (IEND), offset = 0x101a0
extradata:0         .. file: JPEG image data
    00000000: ff d8 ff e0 00 63 6f 6e  67 72 61 74 73 20 79 6f  |.....congrats yo|
    00000010: 75 20 66 6f 75 6e 64 20  6d 65 21 20 79 6f 75 20  |u found me! you |
    00000020: 77 69 6e 20 61 6e 20 69  50 61 64 21 10 4a 46 49  |win an iPad!.JFI|
    00000030: 46 00 01 01 01 00 41 00  41 00 00 ff db 00 43 00  |F.....A.A.....C.|
    00000040: 03 02 02 03 02 02 03 03  03 03 04 03 03 04 05 08  |................|
    00000050: 05 05 04 04 05 0a 07 07  06 08 0c 0a 0c 0c 0b 0a  |................|
    00000060: 0b 0b 0d 0e 12 10 0d 0e  11 0e 0b 0b 10 16 10 11  |................|
    00000070: 13 14 15 15 15 0c 0f 17  18 16 14 18 12 14 15 14  |................|
    00000080: ff db 00 43 01 03 04 04  05 04 05 09 05 05 09 14  |...C............|
    00000090: 0d 0b 0d 14 14 14 14 14  14 14 14 14 14 14 14 14  |................|
    000000a0: 14 14 14 14 14 14 14 14  14 14 14 14 14 14 14 14  |................|
    *
    000000c0: 14 14 14 14 14 ff c2 00  11 08 00 71 00 96 03 01  |...........q....|
    000000d0: 11 00 02 11 01 03 11 01  ff c4 00 1c 00 00 01 04  |................|
    000000e0: 03 01 00 00 00 00 00 00  00 00 00 00 00 00 01 03  |................|
    000000f0: 04 06 02 05 07 08 ff c4  00 19 01 01 00 03 01 01  |................|
meta Software       .. text: "www.inkscape.org"
imagedata           .. file: firmware 0 v0 (revision 0) \377 , 0 bytes or less, at 0x0 0 bytes , at 0x0 0 bytes
root@Python:/home/venom/Downloads# 
```
<p>Setelah dilakukan analisa dengan zsteg ternyata terdapat file JPG pada file PNG, file JPG tidak terdeteksi oleh tool foremost dan binwalk karena pada file terdapat header yang salah/incomplete
, Tambahkan header kedalam file</p>
<p>Sebelum</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Boby_fix1.jpg'>
</p>
<p>Sesudah</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Boby_fix2.jpg'>
</p>
<p>Hasil recovery signature header JPG berhasil, dapat dicheck dengan binwalk dan ekstrak dengan foremost lalu tampilkan gambar</p>

```console
root@Python:/home/venom/Downloads# binwalk recovery.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1000 x 1000, 8-bit/color RGBA, non-interlaced
115           0x73            Zlib compressed data, default compression
65996         0x101CC         JPEG image data, JFIF standard 1.01

root@Python:/home/venom/Downloads# foremost recovery.png 
Processing: recovery.png
|*|
root@Python:/home/venom/Downloads# cd output/jpg/
root@Python:/home/venom/Downloads/output/jpg# eog 00000128.jpg 

```
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/keyed.jpg'>
</p>
<p>Decrypt encryptext yang didapatkan dengan stegsolve dan key pada vigenere cipher pada <a href='http://rumkin.com/tools/cipher/vigenere.php'>website</a>
<pre>
encryptext = zpv_tigqylhbafmeoesllpms
key = bbbabydonthurtmewhatislove
decryptext = you_thinkyougotskillshuh
</pre>
</b><h3>Flag</h3></b>
<pre>
you_thinkyougotskillshuh
</pre>
