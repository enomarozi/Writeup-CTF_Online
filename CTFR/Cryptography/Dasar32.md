<h1><b>Dasar32</b></h1>
<pre>
Belum bisa menyelesaikan First Flag ? Silahkan cari tau bagaimana mengkonversi flag ini menjadi teks yang bisa di baca

Flag : INKEMUT3OMYW24DMGNPWENDTGNPTGMT5BI======
</pre>
<h3><b>Solution</b></h3>
<p>Decode base32 pada script berikut</p>

```python
from base64 import b32decode as decode

encode = "INKEMUT3OMYW24DMGNPWENDTGNPTGMT5BI======"
print(decode(encode).decode('ascii'))
```
<h3><b>Flag</b></h3>
<pre>
CTFR{s1mpl3_b4s3_32}
</pre>
