<h1><b>now you don't</h1></b>
<pre>
We heard that there is something hidden in this <a href="https://2018shell.picoctf.com/static/f518f4ed24443251697079e17a17e93a/nowYouDont.png">picture</a>. Can you find it?
</pre>
</b><h3>Solution</h3></b>
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/nowYouDont.png">
</p>
<p>Gunakan tools stegsolve, lihat pada shift red plane 1, tetapi itu terlalu simple</p>
<p>Kita bisa lihat seluruh nilai RGB dengan opencv-python pada image itu hanya terbagi 2 nilai, yaitu [146,32,32] dan [145,32,32], 
dan diketahui mata manusia tidak dapat melihat perbedaan warna yang sangat kecil itu. disini kita akan convert salah satu RGB ke [255,255,255] yaitu ke warna putih</p>

```python
import cv2

img = cv2.imread("nowYouDont.png")

height, width, channels = img.shape
red = [32,32,145]
black = [255,255,255]

for x in range(0,width):
    for y in range(0,height):
        channels_xy = img[y,x]
        if all(channels_xy == red):    
            img[y,x] = black
            
cv2.imwrite('solve_youdont.png',img)

```
<p>Hasilnya</p>
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/now%20you%20don.png">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{n0w_y0u_533_m3}
</pre>
