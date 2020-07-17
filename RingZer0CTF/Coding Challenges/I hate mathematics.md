<h1><b>I hate mathematics</b></h1>
<pre>
----- BEGIN MESSAGE -----
1347 + 0x784 - 1111010000101 = ?
----- END MESSAGE -----
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk melakukan penjumlahan dan pengurangan dari bilangan desimal + hexa - biner, dan requests jawabannya ke link https://ringzer0ctf.com/challenges/32/[answer] dalam waktu 2 detik</p>

```python3
import requests
import re


with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    r = session.get("https://ringzer0ctf.com/challenges/32")
    challenge = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', r.text)[0]
    text = challenge.replace(" ","").split("+")
    desimal = text[0]
    hexa = text[1].split("-")[0][2:]
    binary = text[1].split("-")[1][:-2]
    compute = int(desimal)+int(hexa,16)-int(binary,2)
    resp = session.get("https://ringzer0ctf.com/challenges/32/"+str(compute))
    flag = re.findall('<div class="alert alert-info">(.*?)</div>',resp.text)[0]
    print(flag)
```

<h3><b>Flag</b></h3>
<pre>
FLAG-JsxIhjHJekAiVaxJlNe2PAYZ
</pre>
