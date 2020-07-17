<h1><b>SIMPLE-RSA</b></h1>
<pre>
n00b encrypted a message using RSA, decrypt it.
n = 697334695917848011908017064620798769199
e = 11
enc= 589000442361955862116096782383253550042
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan e,c,n dari soal</p>
<pre>
e = 11
n = 697334695917848011908017064620798769199
c = 589000442361955862116096782383253550042
</pre>
<p>Generate p dan q dari faktorial n <a href="factordb">factordb</a></p>
<pre>
p = 24659183668299994531
q = 28278904334302413829
</pre>
<p> Generate privatekey(d) dan lalu Decrypt ciphertext(c)

```python
import gmpy2

e = 11
c = 589000442361955862116096782383253550042
n = 697334695917848011908017064620798769199
p = 24659183668299994531 #factordb
q = 28278904334302413829 #factordb
phi = (p-1)*(q-1) 
d = gmpy2.invert(e,phi)
print(bytes.fromhex(hex(pow(c,d,n))[2:]).decode("ascii"))
```

<h3><b>Flag</b></h3>
<pre>
CTF{RSA_15_k00l}
</pre>

