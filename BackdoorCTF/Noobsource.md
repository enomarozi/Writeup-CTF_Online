<b><h1>Noobsource</b></h1>
<pre>
Haxor hid the flag on his website's source code, but kokil is unable to view it. 
Can you help him?

<a href="http://static.beast.sdslabs.co/static/noobsource/index.html">Link</a>
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita buka halaman web, kita tidak diberikan secara langsung untuk melihat source view halaman. dan Disini kita akan melakukan get request sekaligus mencetak content pada halaman</p>

```python
import requests

req = requests.get("http://static.beast.sdslabs.co/static/noobsource/index.html").text
print(req)
```
<p>Periksa seluruh content, disana terdapat string encode base64 <b>Q1RGe2NsaWVudF9mYWNpbmdfY29kZV9pc19uZXZlcl9zZWN1cmV9</b>, decode string untuk mendapatkan flag</p>
<h3><b>Flag</b></h3>
<pre>
CTF{client_facing_code_is_never_secure}
</pre>
