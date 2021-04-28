<h1><b>Kocheng Poteh</b></h1>
<pre>
Kocheng poteh sedang diangkat sama hooman. Bantu turunkannnn :(

Challenge --> <a href='https://mega.nz/#!Z540ESCY!IcvLsaR-kgHKkEkrLcFp7u33TvH0JF5dSuK6qd1_Drw'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Terdapat file image PNG pada file PNG, ikuti command dibawah</p>

```console
root@Python:/home/venom/Downloads# binwalk kochengpoteh.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 750 x 500, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, best compression
451340        0x6E30C         PNG image, 804 x 442, 8-bit/color RGB, non-interlaced
451431        0x6E367         Zlib compressed data, compressed

root@Python:/home/venom/Downloads# foremost kochengpoteh.png 
Processing: kochengpoteh.png
|*|
root@Python:/home/venom/Downloads# mv output/png/00000881.png .             
root@Python:/home/venom/Downloads# eog 00000881.png 
```
<p align='center'>
    <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/kocheng_putih.png'>
</p>

```python3
import cv2
import pytesseract

img = cv2.imread('kocheng_putih.png')
print(pytesseract.image_to_string(img)) #CTFR{d1_d4l4m_g4mb4r_4d4_g4mb4r}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{d1_d4l4m_g4mb4r_4d4_g4mb4r}
</pre>
