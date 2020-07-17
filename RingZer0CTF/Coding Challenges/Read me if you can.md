<h1><b>Read me if you can</b></h1>
<p align='center'>
  <img src="https://github.com/enomarozi/RingZer0CTF/blob/master/Coding%20Challenges/Image/image.png">
</p>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk membaca string pada captcha image, dan requests ke link https://ringzer0ctf.com/challenges/17/[Your_string], dalam waktu 2 detik</p>

```python3
import pytesseract
import requests
import re
import urllib
from PIL import Image
import numpy as np


with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    r = session.get("https://ringzer0ctf.com/challenges/17")
    challenge = re.findall('<img src="(.*?)" /><br />', r.text)[0]
    urllib.URLopener().retrieve(challenge,"image.png")
    im = Image.open('image.png')
    converted = np.where(np.array(im) == 255, 0, 255)
    im = Image.fromarray(converted.astype('uint8'))
    gray = im.convert('L')
    thresh = gray.point(lambda x: 0 if x<1 else 255, '1')
    text = pytesseract.image_to_string(thresh)
    resp = session.get("https://ringzer0ctf.com/challenges/17/"+text)
    try:
        flag = re.findall('<div class="alert alert-info">(.*?)</div>',resp.text)[0]
        print(flag)
    except:
        print("Your Slow!, Please Try again")
```

<h3><b>Flag</b></h3>
<pre>
FLAG-a6r6hv938rb7ou5wu1ct8j9loy
</pre>
