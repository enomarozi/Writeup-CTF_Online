<h1><b>TEST</h1></b>
<pre>
This is a test challenge to get you aquainted with flags. 
The flag for this challenge is the SHA-256 hash of 'very_simple_flag'
</pre>
<h3><b>Solution</b></h3>
sha256(very_simple_flag)

```python3
import hashlib

text = "very_simple_flag".encode('utf8')
hash_text = hashlib.sha256(text).hexdigest()
print(hash_text)

```
<h3><b>Flag</b></h3>
<pre>
e9dab8f2bc7384b23ee4515c997cc534ef5827762bd3b15339cee2aa5552973d
</pre>
