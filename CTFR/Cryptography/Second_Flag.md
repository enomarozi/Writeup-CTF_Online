<h1><b>Second Flag</b></h1>
<pre>
Sebelumnya sudah mengenal yang namanya Encode dan Decode Yaah ? Sekarang masih sama, cuman jika kamu melihatnya challenge ini sebagai unik, maka pelajaran bagi anda :D.

Flag : TKWI{j3t0eu_wc4x_n4j_t1gy3i_k3ok}
</pre>
<h3><b>Solution</b></h1>
<p>Decode ROT13 pada website <a href='https://rot13.com/'>ROT13</a> atau dengan script dibawah</p>

```python3
flag = "TKWI{j3t0eu_wc4x_n4j_t1gy3i_k3ok}"
def rot13(n):
    result = ""
    for j in flag:
        if j.isupper():
            result += chr((ord(j)+n-65)%26+65)
        elif j.islower():
            result += chr((ord(j)+n-97)%26+97)
        else:
            result += j
    if "CTFR" in result:
        print(result+" ,Key =",n)
     
for j in range(26):
    rot13(j)
```
<p>Output Program dan Key</p>
<pre>
CTFR{s3c0nd_fl4g_w4s_c1ph3r_t3xt} ,Key = 9
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{s3c0nd_fl4g_w4s_c1ph3r_t3xt}
</pre>
