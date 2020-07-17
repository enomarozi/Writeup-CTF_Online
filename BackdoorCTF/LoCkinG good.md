<h1><b>LoCkinG good</b></h1>
<pre>
Kratos is absolutely sure that this time his encryption scheme is unbreakable. 
Sadly, this time sin3point14 is unavailable so it's up to you to prove him wrong

<a href="http://static.beast.sdslabs.co/static/LoCkinG%20good/flag.enc">flag.enc</a>
<a href="http://static.beast.sdslabs.co/static/LoCkinG%20good/encrypt.py">encrypt.py</a>
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta menjadi cryptanalys untuk mendecrypt ciphertext dengan program encryption yang diberikan, jadi disini kita akan mencoba me-reverse operasi program</a>
<p>Program yang diberikan</p>

```python
from flag import flag
from params import a,b,s

def genlcg(n,s):
    lcg = [s]
    for i in range(1,n):
        lcg.append((a*lcg[-1] + b)%251)
    return lcg

key = genlcg(len(flag),s)

ciphertext = "".join([chr(flag[i]^key[i]) for i in range(len(flag))])

with open('flag.enc','w') as output:
    output.write(ciphertext)
    output.write("###################")
    output.write(str(key[0]))
    output.write("###################")
    output.write(str(key[1]))
    output.write("###################")
    output.write(str(key[2])) 
```
<p>Ciphertext yang diberikan</p>
<pre>
#¤ÉÞ{[ÎE§¤² #FAù###################69###################200###################168
</pre>

<p>Pada program encrypt yang diberikan kita tidak diberikan nilai a, b dan s, disini kita akan melakukan bruteforce untuk memperoleh a, b dan s</p>

```python
def genlcg(n,s):
    lcg = [s]
    for i in range(1,n):
        lcg.append((a*lcg[-1] + b)%251)
    return lcg

for i in range(100):
    for j in range(300):
        for k in range(300):
            a,b,s = i,j,k
            flag = [1,2,3,4]
            key = genlcg(len(flag),s)

            ciphertext = "".join([chr(flag[i]^key[i]) for i in range(len(flag))])
            if key[0] == 69 and key[1] == 200 and key[2]==168: 
                print("a = "+str(i),"b = "+str(j),"s = "+str(k))
```
<p>Hasil</p>
<pre>
a = 17 b = 31 s = 69
a = 17 b = 282 s = 69
</pre>
<p>Sekarang kita mendapatkan dua nilai a, b dan s, kita akan menggunakan nilai yang pertama. lanjut, 
karena format flag yang diminta pada variabel flag yaitu nilai hexa dari masing-masing 1 bytes flag, kita akan convert seluruh ascii flag ke hexadesimal</p>

```python
text = "#¤ÉÞ{[ÎE§¤² #FAù###################69###################200###################168"
for i in text:
    print(hex(ord(i))[2:].rjust(2,"0"),end=' ')
```
<p>Hasil ciphertext dalam hexadesimal</p>
<pre>
23 a4 c9 19 de 7b 5b ce 83 1c 45 a7 18 a4 19 b2 a0 23 10 46 81 41 06 f9 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 36 39 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 32 30 30 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 23 31 36 38 
</pre>
<p>Selanjutnya kita akan decrypt pada bagian hexadesimal flag yaitu 23 a4 c9 19 de 7b 5b ce 83 1c 45 a7 18 a4 19 b2 a0 23 10 46 81 41 06 f9</p>

```python

def genlcg(n,s):
    lcg = [s]
    for i in range(1,n):
        lcg.append((a*lcg[-1] + b)%251)
    return lcg

a,b,s = 17,31,69

flag = "23 a4 c9 19 de 7b 5b ce 83 1c 45 a7 18 a4 19 b2 a0 23 10 46 81 41 06 f9".split(" ")
key = genlcg(len(flag),s)
ciphertext = "".join([chr(int(flag[i],16)^key[i]) for i in range(len(flag))])
print(ciphertext)
    
```
<h3><b>Flag</b></h3>
<pre>
flag{0h_n0_y0u_kn0w_LCG}
</pre>
