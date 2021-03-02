<h1><b>SHA1</b></h1>
<pre>
Dalam kriptografi, SHA-1 adalah fungsi hash kriptografi yang mengambil input dan menghasilkan nilai hash 160-bit yang dikenal sebagai intisari pesan - biasanya dirender sebagai bilangan heksadesimal, panjangnya 40 digit.

Flag : CTFR{(SHA1 dari "CTFR")}
</pre>
<h3><b>Solution</b></h3>
<p>Decrypt Hash SHA1</p>

```python3
import hashlib

flag = 'CTFR'
hashing = hashlib.sha1(flag.encode('utf-8'))
print(hashing.hexdigest()) #CTFR{725912ce4ff578c4a9ece9821e7da02103276150}

```
<h3><b>Flag</b></h3>
<pre>
CTFR{725912ce4ff578c4a9ece9821e7da02103276150}
</pre>
