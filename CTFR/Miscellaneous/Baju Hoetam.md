<h1><b>Baju Hoetam</b></h1>
<pre>
Coba cari teks pada Baju Hoetam dibawah ini

Challenge --> <a href='https://mega.nz/#!UsgAVCiA!6lrmO410iG2cXgLhBsdjY4Wyi-3ixdH9l9_MZyEvosA'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Buka file dengan matplotlib python untuk melihat RGB dari masing pixel</p>
<p align='center'>
   <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/bajuhitam.png'>
</p>
<p align='justify'>Disana terdapat beberapa RGB yang menunjukan [0,0,0] yang sementara RGB sekitarannya [1,1,1]. Maka lakukan Thresholding binary dari image 0 dan 255</p>

```python3
import matplotlib.pyplot as plt
import pytesseract
import cv2

img = cv2.imread('bajuhoetam.png')
imgplot = plt.imshow(img)
plt.show()

ret,image_thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
cv2.imshow('flag',image_thresh)
cv2.waitKey(0)
cv2.imwrite('flag.jpg',image_thresh)
print("Flag :",pytesseract.image_to_string(cv2.imread('flag.jpg')))
```
<p align='center'>
   <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/flag_hitam.png'>
<p>
<h3><b>Flag</b></h3>
<pre>
CTFR{yOu_c4nt_s33_m3}
</pre>
