<h1><b>Easy1</h1></b>
<pre>
The one time pad can be cryptographically secure, but not when you know the key. 
Can you solve this? We've given you the encrypted flag, key, and a table 
to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this <a href='https://2019shell1.picoctf.com/static/30d4405c34cf6490b082e6cf8f56ac56/table.txt'>table</ac> to solve it?.
</pre>
</b><h3>Solution</h3></b>
<p>Decrypt vigenere cipher</p>
<pre>
Encode = UFJKXQZQUNB
Key = SOLVECRYPTO
Message/Flag = CRYPTOISFUN
</pre>
</b><h3>Flag</h3></b>
<pre>
picoCTF{CRYPTOISFUN}
</pre>
