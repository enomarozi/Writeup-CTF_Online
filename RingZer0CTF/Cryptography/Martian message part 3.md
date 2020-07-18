<h1><b>Martian message part 3</h1></b>
<pre>
RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS
</pre>
</b><h3>Solution</h3></b>
<p>Decode base64, dan xor 1 bytes disetiap character</p>

```python
import base64

encode = "RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS"
text = base64.b64decode(encode)

def brute_ascii(n,text):
    flag = ""
    for i in text:
        flag += chr(i^n)
    if "FLAG" in flag:
        print("Key is "+str(n)+" and "+flag)
for j in range(100):
    brute_ascii(j,text)
```
<p>Hasil program</p>
<pre>
Key is 3 and FLAG-4jdr782jha62jaLL38972Q
</pre>
</b><h3>Flag</h3></b>
<pre>
FLAG-4jdr782jha62jaLL38972Q
</pre>
