<h1><b>MD5</b></h1>
<pre>
Dalam kriptografi, MD5 adalah fungsi hash kriptografik yang digunakan secara luas dengan hash value 128-bit. Pada standart Internet, MD5 telah dimanfaatkan secara bermacam-macam pada aplikasi keamanan, dan MD5 juga umum digunakan untuk melakukan pengujian integritas sebuah berkas.

Flag : CTFR{(MD5 dari "CTFR")}
</pre>
<h3><b>Solution</b></h3>
<p>Decrypt Hash MD5</p>

```python
import hashlib

flag = 'CTFR'
hashing = hashlib.md5(flag.encode('utf-8'))
print(hashing.hexdigest()) #d69faaea338ac0073602593fc9416f77
```
<h3><b>Flag</b></h3>
<pre>
CTFR{d69faaea338ac0073602593fc9416f77}
</pre>
