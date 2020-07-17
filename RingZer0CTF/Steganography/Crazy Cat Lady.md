<h1><b>Crazy Cat Lady</h1></b>
<p align="center">
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/RingZer0CTF/Steganography/Images/6981cdaa2a3e327811985683a596c916.png">
</p>
</b><h3>Solution</h3></b>
<p>Analisa image dengan zsteg, maka didapatkan beberapa frame yang menampilkan flag yaitu image binary 00000111</p>

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('stego.png')
data = np.array(img)
extracted = (data[...,0] ^ data[...,1] ^ data[...,2]) & 0x07
plt.imshow(extracted)
plt.show()
```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/RingZer0CTF/Steganography/Images/CAT.png">
</p>
</b><h3>Flag</h3></b>
<pre>
FLAG-cYNUSHmeSBWvyNw9fe1iyhsaYZivCJLj
</pre>
