<h1><b>XORFUN</b></h1>
<pre>
Cipher = DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa
Decrypt it.

This might be helpful: http://static.beast.sdslabs.co/static/XORFUN/cry.py
Hint:XOR(XOR(text,key),text) = key.
cipher = b64encode(XOR(msg2,key))
</pre>
<h3><b>Solution</b></h3>
<p>Disini kita diminta untuk menjadi cryptanalys untuk me-reverse dari ciphertext ke plaintext tanpa key dan hanya mempunyai beberapa clue dan program untuk meng-encrypt-nya</p>

```python
def XOR(A, B):
	return ''.join(chr(ord(A[i])^ord(B[i%len(B)])) for i in range(len(A)))

cipher = "DRcGGQBfGw1QEA4XBUURCA0MDQdGBlFTCTo7MxwJUhgAXBQa".decode('base64')
grep = "n00bCTF"
text = ""
for i in range(28):
	for j in range(i,i+7):
		text += cipher[j]
	x = XOR(grep,text)
	if x.isalnum():
		print 'Key: ' + x
		print 'Flag: CTF{%s}' % XOR(cipher,x)
	text = ""
```
<p>Hasil</p>
<pre>
Key: y5usKYJ
Flag: CTF{t"sjKQtee}\\h=xF^d&zqbye<'kK^c}
Key: hackyou
Flag: CTF{every0ne1senj0yingth3n00bCTFth1sy3ar}
</pre>
<h3><b>Flag</b></h3>
<pre>
CTF{every0ne1senj0yingth3n00bCTFth1sy3ar}
</pre>
