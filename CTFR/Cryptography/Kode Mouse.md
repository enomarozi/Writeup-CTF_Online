<h1><b>Kode Mouse</b></h1>
<pre>
Mouse juga mempunyai kode untuk melakukan klik pada sebuah komputer, akan tetapi hal ini lah yang membuat komputer dapat bergerak, Tanpa mouse PC / Laptop kita tidak ada guna nya :). salah satunya coba decode ini, Flag Format nya harus tetap di ikuti ya!.

Flag : -.-. - ..-. .-. -- ----- .-. ... ...-- ..--.- -.-. ----- -.. ...-- ..--.- .---- ... ..--.- .- .-- ...-- ... ----- -- ...--
</pre>
<h3><b>Solution</b></h3>
<p>Merupakan morse encode, decode pada website <a href='https://morsedecoder.com/'></a>, atau pada script dibawah</p>

```python
morse ={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.",
        "H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.",
        "O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
        "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","1":".----",
        "2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...",
        "8":"---..","9":"----.","0":"-----","(":"-.--.",")":"-.--.-"}
encode = "-.-. - ..-. .-. -- ----- .-. ... ...-- ..--.- -.-. ----- -.. ...-- ..--.- .---- ... ..--.- .- .-- ...-- ... ----- -- ...--".split(' ')
for i in encode:
    for j in morse.items():
        if i==j[1]:
            print(j[0],end='')
    
```
<p>Output Program</p>
<pre>
CTFRM0RS3C0D31SAW3S0M3
</pre>
<h3><b>Flag</b></h3>
<pre>
CTFR{m0rs3_c0d3_1s_aw3s0m3}
</pre>
