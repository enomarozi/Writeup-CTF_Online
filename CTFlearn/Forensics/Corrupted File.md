<h1><b>Corrupted File</h1></b>
<pre>
Help! I can't open this file. Something to do with the file header… Whatever that is. 
https://mega.nz/#!aKwGFARR!rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file gif corrupt, perbaiki header file dengan menambahkan GIF8 atau hexa(47 49 46 38)</p>
<p>Sebelum</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Recovery_gif.jpg">
</p>
<p>Sesudah</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Recovery_gif1.jpg">
</p>
<p>Jika file sudah fix, ektrak semua frame file gif, disana hanya terdapat 4 frame. Tetapi disini saya mengconvert terlebih dahulu ke format MP4 atau jenis video lainnya
karna opencv python tidak bisa membaca file gif sebagai video</p>

```python

import cv2

cam = cv2.VideoCapture("recovery_gif.mp4")
value = 0
while 1:
    frame = cam.read()[1]
    cv2.imwrite("frame"+str(value)+".jpg",frame)
    cv2.waitKey(1)
    value += 1
    if value == 4:
        break
cam.release()
cv2.destroyAllWindows()
```
<p>Dan hasilnya</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/frame0.jpg' width=200>
</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/frame1.jpg' width=200>
</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/frame2.jpg' width=200>
</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/frame3.jpg' width=200>
</p>

```console
root@Python:/home/venom/Downloads# echo 'ZmxhZ3tnMWZfb3JfajFmfQ==' | base64 -d
flag{g1f_or_j1f}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
flag{g1f_or_j1f}
</pre>
