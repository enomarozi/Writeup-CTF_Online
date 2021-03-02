<h1><b>MD4</b></h1>
<pre>
MD4 Message-Digest Algorithm adalah fungsi hash kriptografi yang dikembangkan oleh Ronald Rivest pada tahun 1990. Panjang intinya adalah 128 bit. Algoritme telah mempengaruhi desain selanjutnya, seperti algoritma MD5, SHA-1 dan RIPEMD. Initialism "MD" adalah singkatan dari "Message Digest."

Flag : CTFR{(MD4 dari "CTFR")}

</pre>
<h3><b>Solution</b></h3>
<p>Decrypt Hash MD4</p>

```python
from Crypto.Hash import MD4

init = MD4.new()
init.update('CTFR')
print('CTFR{'+init.hexdigest()+'}') #CTFR{bcab8f1da86a260ce0fb2a2c027a0d6f}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{bcab8f1da86a260ce0fb2a2c027a0d6f}

</pre>
