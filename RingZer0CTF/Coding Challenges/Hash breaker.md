<h1><b>Hash breaker</b></h1>
<pre>
----- BEGIN HASH -----
63d0e5111cab6ee169b598ef1fba59b19059da90
----- END HASH -----
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk break hash sha1 diatas untuk mendapatkan clear-text dalam waktu 3 detik, dan requests ke link https://ringzer0ctf.com/challenges/56/[clear-text]</p>

```python3
import requests
import re
import hashlib


with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    r = session.get("https://ringzer0ctf.com/challenges/56")
    challenge = re.findall('----- BEGIN HASH -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END HASH -----', r.text)[0]
    for i in range(10000):
        check = hashlib.sha1(str(i).encode('utf8')).hexdigest()
        if check == challenge:
            submit = i
    resp = session.get("https://ringzer0ctf.com/challenges/56/"+str(submit))
    flag = re.findall('<div class="alert alert-info">(.*?)</div>',resp.text)[0]
    print(flag)
```

<h3><b>Flag</b></h3>
<pre>
FLAG-G1095M88Tk837G9AC0EA6q3N
</pre>
