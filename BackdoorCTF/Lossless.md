<h1><b>Lossless</b></h1>
<pre>
d4rth used his dirty methods to hide a secret in a png file. 
He is cleverly trying to divert your focus from challenge, but the force is strong with you. 
Now extract the flag from these images, my young padawan.
http://static.beast.sdslabs.co/static/LOSSLESS/original.png
http://static.beast.sdslabs.co/static/LOSSLESS/encrypted.png
</pre>
<h3><b>Solution</b></h3>
<p>Pertama kita mencari perbedaan ke-2 gambar pada <a href="https://futureboy.us/stegano/compinput.html">stegodiff</a></p>
<p> Gambar 1</p>
<p align="center">
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/original.png">
</p>
<p> Gambar 2</p>
<p align="center">
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/encrypted.png">
</p>
<p> Hasil Perbedaan gambar</p>
<p align="center">
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/diff.png">
</p>
<p>Disana terdapat 343 black dan blue pixel diarea sudut kiri atas, jika kita hitung sesuai column disana terdapat 343 / jumlah column.
<b>343 / 49 = 7</b> yang artinya terdapat 49 string ascii</p> 

```python
import cv2

img = cv2.imread("diff.png",0)
data = ""
for j in range(49):
    for i in range(7):
        if img[i][j] == 95:
            data += "1"
        else:
            data += "0"
    print(chr(int(data,2)),end="")
    data = ""
```
<h3><b>Flag</b></h3>
<pre>
SHA256{d1ff1cul7_t0_f0cu5,wa5n't_i7?}
</pre>
