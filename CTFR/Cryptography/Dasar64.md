<h1><b>Dasar64</b></h1>
<pre>
Belum bisa menyelesaikan First Flag ? Silahkan cari tau bagaimana mengkonversi flag ini menjadi teks yang bisa di baca

Flag : Q1RGUntzMW1wbDNfYjRzM182NH0=
</pre>
<h3><b>Solution</b></h3>
<p>Decode base64 pada script python dibawah</p>

```python3
from base64 import b64decode as decode

encode = "Q1RGUntzMW1wbDNfYjRzM182NH0="
print(decode(encode).decode('ascii'))

```
<h3><b>Flag</b></h3>
<pre>
CTFR{s1mpl3_b4s3_64}
</pre>
