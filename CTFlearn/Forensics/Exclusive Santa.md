<h1><b>Exclusive Santa</h1></b>
<pre>
Dear Santa,
Hey! There are so many toys that I want, but I just don't have the money. 
I don't care which toy I get as long as it's one or the other, but not both!

- CTFlearn
<a href='https://ctflearn.com/challenge/download/851'>Exclusive_Santa.rar</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 2 file image PNG, jika dicheck dengan binwalk salah satu file terdapat 2 file image PNG, ekstrak file tersebut dengan foremost</p>

```console
root@Python:/home/venom/Downloads# binwalk 3.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1200 x 875, 8-bit/color RGBA, non-interlaced
78            0x4E            Zlib compressed data, default compression
52406         0xCCB6          PNG image, 1280 x 720, 8-bit/color RGBA, non-interlaced
52447         0xCCDF          Zlib compressed data, compressed

root@Python:/home/venom/Downloads# foremost 3.png 
Processing: 3.png
|*|
root@Python:/home/venom/Downloads# cd output/png/
root@Python:/home/venom/Downloads/output/png# ls
00000000.png  00000102.png
root@Python:/home/venom/Downloads/output/png# 
```
<p>Lakukan operasi xor pada file 00000102.png dengan 1.png dan flip hasilnya</p>

```python
import cv2


img1 = cv2.imread("00000102.png")
img2 = cv2.imread("1.png")
img_xor = cv2.bitwise_xor(img1,img2)
img_flip = cv2.flip(img_xor, 1)
cv2.imwrite("image_xor.jpg",img_flip)
```
<p>Hasil XOR dan flip image</p>

<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/image_xor.jpg'>
</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{Santa_1s_C0ming}
</pre>
