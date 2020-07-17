<h1><b>BATMAN</h1></b>
<pre>
Link <a href="http://hack.bckdr.in:11004/">here</a> takes you to Batman shop. Can you take the flag from batman? 
Submit sha-256 of the flag obtained.
</pre>
<h3><b>Solution</b></h3>
<p>Requests dan cari flag dari semua list direktori website</p>
<pre>
http://hack.bckdr.in:11004/?st=<b>1</b>
http://hack.bckdr.in:11004/?st=<b>2</b>
http://hack.bckdr.in:11004/?st=<b>3</b>
http://hack.bckdr.in:11004/?st=<b>...</b>
http://hack.bckdr.in:11004/?st=<b>n-1</b>
</pre>

```python
import requests
import re

url = "http://hack.bckdr.in:11004/?st="
for i in range(20):
    ress = requests.get(url+str(i)).text
    ress = re.findall('Flag is "(.*?)"<',ress)
    if len(ress) != 0:
        print(ress[0], "Terdapat pada list direktori ke-"+str(i))
```
<h3><b>Flag</b></h3>
<pre>
y0u_4r3_b47m4n
</pre>
