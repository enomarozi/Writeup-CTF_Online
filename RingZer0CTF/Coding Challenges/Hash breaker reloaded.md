<h1><b>Hash breaker reloaded</b></h1>
<pre>
----- BEGIN HASH -----
9f8b97482b55081cb357587d9820fce3f4620d07
----- END HASH -----

----- BEGIN SALT -----
f1f1376df0122b756c0332a2eb7b10664d7fdfa5c3f44022173f797305a09eac
----- END SALT -----
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk break hash sha1+salt diatas untuk mendapatkan clear-text dalam waktu 3 detik, dan requests ke link https://ringzer0ctf.com/challenges/57/[clear-text]</p>

```python3
import hashlib
import itertools
import string
import requests
import re


digit = string.digits
bruteforce = itertools.product(digit,repeat=4)
with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    r = session.get("https://ringzer0ctf.com/challenges/57")
    the_hash = re.findall('----- BEGIN HASH -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END HASH -----', r.text)[0]
    the_salt = re.findall('----- BEGIN SALT -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END SALT -----', r.text)[0]
    for i in bruteforce:
        message = ''.join(i)
        hash_function = hashlib.sha1((message+the_salt).encode('utf8')).hexdigest()
        if hash_function == the_hash:
            clear_text = message
    resp = session.get("https://ringzer0ctf.com/challenges/57/"+clear_text)
    flag = re.findall('<div class="alert alert-info">(.*?)</div>',resp.text)[0]
    print(flag)
```

<h3><b>Flag</b></h3>
<pre>
FLAG-XJg5635WZ16F63IcE5ychgNm
</pre>
