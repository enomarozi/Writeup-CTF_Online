<h1><b>My TV ded</h1></b>
<pre>
My TV was broadcasting something about SC4R, but died midway. 
Still, there must be something we could get out out of it. 
NOTE- This challenge may seem quite vague but if you've done other challenges of this ctf, 
you already have a hint(not in the other flags)

<a href="http://static.beast.sdslabs.co/static/My%20TV%20ded/random.png">random.png</a>
<a href="http://static.beast.sdslabs.co/static/My%20TV%20ded/result.png">result.png</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan 2 file image PNG</p>
<p>File image-1</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/My%20TV%20ded.png">
</p>
<p>File image-2</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/My%20TV%20ded1.png">
</p>
<p>xor RGB image-1 dan image-2 dengan tool stegsolve, atau dengan script dibawah ini</p>

```python
import cv2
import numpy as np

img1 = cv2.imread("My TV ded1.png")
img2 = cv2.imread("My TV ded.png")

dest_and = cv2.bitwise_xor(img1,img2,mask=None)
cv2.imshow('',dest_and)
cv2.waitKey(0)
```
<p>Hasil xor RGB</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/MyTVdad_solve.bmp">
</p>
<h3><b>Flag</b></h3>
<pre>
flag{SC4R_w4tch35_b0ku_n0_pic0}
</pre>
