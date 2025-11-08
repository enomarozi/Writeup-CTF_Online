<h1>Corrupted file</h1>
<h3>Description</h3>
<label>This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life? Download the file <a href='https://challenge-files.picoctf.net/c_amiable_citadel/bdd976098377529fe779dbd31b424f69e51327b5ba68fd247dfcc074f0684141/file'>here</a>.</label>
<h3>Solution</h3>
<label>Perbaiki 2 byte header</label>
<pre>
5c 78 --> FF D8
</pre>
<label>Rename file ke file.jpg</label>

```python3
from PIL import Image
import pytesseract

img = Image.open('file.jpg')
w, h = img.size
img = img.resize((w * 8, h * 8))
text = pytesseract.image_to_string(img, config='--psm 7')
print(text)
```
<h3>Flag</h3>
<pre>
picoCTF{r3st0r1ng_th3_by73s_249e4e3c}
</pre>
