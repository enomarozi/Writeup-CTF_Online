<h1><b>haXORed</b></h3>
<pre>
Legends say a single byte is the key to unlocking this mystery

<a href="http://static.beast.sdslabs.co/static/haXORed/flag.enc">flag.enc</a>
</pre>
<h3><b>Solution</b></h3>
<p>Bruteforce encoding dengan 1 byte key menggunakan operasi xor</p>

```python
def xoor(n):
    encode = "23 29 24 22 3e 27 37 30 31 76 1a 23 75 37 26 76 1a 74 36 1a 24 1a 26 2d 71 37 28 38".split(" ")
    flag = ""
    for i in encode:
        flag += chr(int(i,16)^n)
    if "flag" in flag:
        print(flag)

for j in range(100):
    xoor(j)
    
```
<h3><b>Flag</b></h3>
<pre>
flag{brut3_f0rc3_1s_a_ch4rm}
</pre>
