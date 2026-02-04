<h1>john_pollard</h1>
<h3>Description</h3>
<pre>
Sometimes RSA <a href='https://challenge-files.picoctf.net/c_fickle_tempest/1856eb14e19d22938afedaf8af8bc267f94616566c1f7b6e9c34d0c890e4908f/cert'>certificates</a> are breakable
</pre>
<h3>Solution</h3>
<label>Diberikan file public key</label>

```python3
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import requests

with open("cert", "rb") as f:
    cert = x509.load_pem_x509_certificate(f.read(), default_backend())

pub = cert.public_key().public_numbers()

print("n =", pub.n)
print("e =", pub.e)

url = f"http://factordb.com/api?query={pub.n}"
r = requests.get(url).json()
print("q =",r["factors"][0][0])
print("p =",r["factors"][1][0])
print("Flag : picoCTF{"+r["factors"][1][0]+","+r["factors"][0][0]+"}")
```
<h3>Flag</h3>
<pre>
picoCTF{73176001,67867967}
</pre>
