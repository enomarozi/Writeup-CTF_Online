<h1>interencdec</h1>
<p>Can you get the real meaning from this file.
Download the file <a href='https://artifacts.picoctf.net/c_titan/111/enc_flag'>here</a>.</p>
<h3>Solution</h3>

```python
import base64
import string

low = string.ascii_lowercase
big = string.ascii_uppercase
number = string.digits+'{}_-'

def brute(n,enc):
    result = ''
    for i in enc:
        if i not in number:
            if i in low:
                result += chr((ord(i)+n-97)%26+97)
            else:
                result += chr((ord(i)+n-65)%26+65)
        else:
            result += i
    if "picoCTF" in result:
        print(result)
    result = ''
    
file = open('enc_flag','r').read()
decode_1 = base64.b64decode(file).decode().split("'")
decode_2 = base64.b64decode(decode_1[1]).decode()
for i in range(26):
    brute(i, decode_2)

```
<h3>Flag</h3>
<pre>picoCTF{caesar_d3cr9pt3d_890d2379}</pre>
