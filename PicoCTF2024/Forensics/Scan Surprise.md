<h1>Scan Surprise</h1>

<h3>Description</h3>
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
You can download the challenge files here:
<a href='https://artifacts.picoctf.net/c_atlas/16/challenge.zip'>File</a>
Additional details will be available after launching your challenge instance.

<h3>Solution</h3>

```python
from qreader import QReader
import cv2

qr = QReader()
image = cv2.cvtColor(cv2.imread("home/ctf-player/drop-in/flag.png"), cv2.COLOR_BGR2RGB)
text = qr.detect_and_decode(image=image)
print(text[0])
```
<h3>Flag</h3>
<p>
  picoCTF{p33k_@_b00_7843f77c}
</p>
