<h1><b></h1></b>
<pre>
<a href="https://ringzer0ctf.com/challenges_page/tv_091091d3cfcf927ea012e773b60f9010.html">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Save as image, dan itu merupakan file gif. Disini kita diberi soal tentang visual crypto</p>
<p>Diketahui bahwa file gif memiliki frame, Ekstrak seluruh frame gif</p>

```python
import cv2

cam = cv2.VideoCapture("tv.gif")
frm = 0
while 1:
    frame = cam.read()[1]
    cv2.imwrite("frame_"+str(frm)+".png",frame)
    frm += 1
```
<p>Disini kita akan check setiap frame, dan melakukan xor dengan tool stegsolve. Dan ternyata setiap frame 1 dan 2 atau lainnya jika di-xor menghasilkan image yang berbeda,
 Jadi disini kita akan coba bruteforce seluruh frame dengan operasi xor image</p>
 
 ```python
 import cv2
 
 for i in range(31):
    for j in range(31):
        img1 = cv2.imread("frame_"+str(i)+".png")
        img2 = cv2.imread("frame_"+str(j)+".png")
        img_xor = cv2.bitwise_xor(img1,img2)
        cv2.imwrite("Result_xor/image_xor"+str(i)+"_"+str(j)+".png",img_xor)
 ```
<p>Hasil beberapa xor image yang memuat gambar dan pesan flag</p>
<p align='left'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/RingZer0CTF/Steganography/Images/image_xor27_13.png" width=300>
</p>
<p align='left'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/RingZer0CTF/Steganography/Images/image_xor25_17.png" width=300>
</p>
<p align='left'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/RingZer0CTF/Steganography/Images/image_xor29_18.png" width=300>
</p>
<p align='left'>
  <img src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/RingZer0CTF/Steganography/Images/image_xor30_16.png" width=300>
</p>

</b><h3>Flag</h3></b>
<pre>
FLAG-AcsW3fK9NxJMn2
</pre>
