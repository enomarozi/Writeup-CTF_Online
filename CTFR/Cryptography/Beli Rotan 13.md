<h1><b>Beli Rotan 13</b></h1>
<pre>
Mama Adi: "Di belikan mama Rotan"
Adi: "Berapa mak ?"
Mama Adi: "13 Aja di Pasar Pahlawan"
Adi: "Uangnya mana mak?"
Mama Adi: "Nih, PGSE{3i3e_u34eq_4obhg_e0g13?}"
Adi: "Siap Mak!"
</pre>
<h3><b>Solution</b></h1>
<p>Decode ROT13 pada website <a href='https://rot13.com/'>ROT13</a> atau dengan script dibawah</p>

```python3
flag = "PGSE{3i3e_u34eq_4obhg_e0g13?}"
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
CTFR{3v3r_h34rd_4bout_r0t13?} ,Key = 13
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{3v3r_h34rd_4bout_r0t13?}
</pre>
