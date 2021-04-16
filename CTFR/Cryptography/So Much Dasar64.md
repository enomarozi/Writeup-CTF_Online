<h1><b>So Much Dasar64</b></h1>
<pre>
Kali ini, banyak sekali Dasar64 yang terenkripsi. Coba bantu decode dong

Challenge --> <a href='https://mega.nz/file/0lZzHIya#nWQWU1MbZemV-n-YIQNMB7UyZCf-TDI42XAHl5wPKws'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan encode pesan base64, decode pesan tersebut dengan base64 atau hex ke text hingga mendapatkan flag</p>

```python3
import base64

file = open('somuchdasar64.txt','r').read()
list_decode = [base64.b64decode(file)]
for i in range(1,25):
    try:
        by2hex = bytes.fromhex(str(list_decode[-1])[2:-1])
        list_decode.append(by2hex)
    except ValueError:
        b64d = base64.b64decode(list_decode[-1])
        list_decode.append(b64d)
print(list_decode[-1].decode('ascii'))#CTFR{ju5t_d3c0d3_1t_n0th1n9_3ls3}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{ju5t_d3c0d3_1t_n0th1n9_3ls3}
</pre>
