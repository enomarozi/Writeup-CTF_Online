<h1><b>Is it a secure strings?</h1></b>
<pre>
I found an encrypted password and the key. Recover the pass!

Password:
76492d1116743f0423413b16050a5345MgB8AEEAYQBNAHgAZQAxAFEAVAB
IAEEAcABtAE4ATgBVAFoAMwBOAFIAagBIAGcAPQA9AHwAZAAyADYAMgA2AD
gAMwBlADcANAA3ADIAOQA1ADIAMwA0ADMAMwBlADIAOABmADIAZABlAGMAM
QBiAGMANgBjADYANAA4ADQAZgAwADAANwA1AGUAMgBlADYAMwA4AGEAZgA1
AGQAYgA5ADIAMgBkAGIAYgA5AGEAMQAyADYAOAA=


Key:
(3,4,2,3,56,34,254,222,205,34,2,23,42,64,33,223,1,34,2,7,6,5,35,12)
</pre>
</b><h3>Solution</h3></b>
<p>Kita diberikan suatu ciphertext dan key, jika dilihat dari panjang key yaitu 24 bytes merupakan salah satu encryption block cipher yaitu AES</p>
<p>Dan untuk ciphertext, decode base64 pada soal, pada base64 itu split antara MD5 dan base64 lalu decode, dan hasilnya</p>
<pre>
2|AaMxe1QTHApmNNUZ3NRjHg==|d262683e74729523433e28f2dec1bc6c6484f0075e2e638af5db922dbb9a1268
</p>
<p>Disini kita medapatkan IV dan ciphertextnya, yang artinya itu merupakan AES mode CBC, lanjut decrypt ciphertext AES-CBC</p>

```python
import base64
from Crypto.Cipher import AES
import hashlib

key = [3,4,2,3,56,34,254,222,205,34,2,23,42,64,33,223,1,34,2,7,6,5,35,12]
data = "2|AaMxe1QTHApmNNUZ3NRjHg==|d262683e74729523433e28f2dec1bc6c6484f0075e2e638af5db922dbb9a1268".split("|")

key_dec = ''.join([hex(i)[2:].rjust(2,"0") for i in key])
key_dec = bytes.fromhex(key_dec)
IV = base64.b64decode(data[1].encode('utf8'))
encryption = bytes.fromhex(data[2])
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(str(decrypt).replace("\\x00",""))
```
<p>Hasil</p>
<pre>
FLAG-5tguasm48\x04\x04\x04\x04
</pre>
<p>Pada flag terdapat padding 4 bytes</p>
</b><h3>Flag</h3></b>
<pre>
FLAG-5tguasm48
</pre>
