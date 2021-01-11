<h1><b>Upin Ipin</b></h1>
<pre>
Upin ipin sedang pergi kepasar, kemudian menemukan 2 angka yaitu 1 dan 4. Kemudian Upin bertanya kepada Ipin,
Upin : "Pin, kau tau tak angka apa nie"
Ipin : "Tak laa, tapi ipin nemu teks lagi ni GXJV{4jj1r3_g1tl3v_ea3w0q3}"
Upin : "Keknye, kite harus kasih tau opah, Mungkin opah tau maksud dari huruf dan teks tadi nie"
Ipin : "Jom"
</pre>
<h3><b>Solution</b></h3>
<p>Decode Cipher Shiffer pada website <a href='http://rumkin.com/tools/cipher/caesar.php'>Shift</a>, atau dengan script berikut</p>

```python
flag = "GXJV{4jj1r3_g1tl3v_ea3w0q3}"
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
<p>Output Program</p>
<pre>
CTFR{4ff1n3_c1ph3r_aw3s0m3} ,Key = 22
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{4ff1n3_c1ph3r_aw3s0m3}
</pre>
