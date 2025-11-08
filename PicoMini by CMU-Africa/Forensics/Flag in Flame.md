<h1>Flag in Flame</h1>
<h3>Description</h3>
<label>The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log. Download the encoded data here: <a href='https://challenge-files.picoctf.net/c_amiable_citadel/5d0fa1b1244c39428b2d5ca4f966fce8772038c43b9bd56f1c9890cb733c807f/logs.txt'>Logs Data</a>. Be prepared—the file is large, and examining it thoroughly is crucial .</label>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cat logs.txt| base64 -d | head -n 1
�PNG
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cat logs.txt| base64 -d > image.png
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file image.png                       
image.png: PNG image data, 896 x 1152, 8-bit/color RGB, non-interlaced
```
<label>Decode base64 ke image type png, dan buka</label>

```python3
import pytesseract
from PIL import Image

img = Image.open('image.png')
text = pytesseract.image_to_string(img).split('\n')
for str_ in text:
    if len(str_) >= 10:
        print(bytes.fromhex(str_.replace(' ','')).decode())
```

<h3>Flag</h3>
<pre>
picoCTF{forensics_analysis_is_amazing_2561a194}
</pre>
