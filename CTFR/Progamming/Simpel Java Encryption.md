<h1><b>Simpel Java Encryption</b></h1>
<pre>
Mimin ada code java nih, Coba deh di decode

```java
String flag = "CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|";
String encrypt = "";
for(int i = 0; i < flag.length(); i++) {
    if ((i % 10) == 0) 
    { 
      break; 
    }
    if ((i & 2) == 0) 
    { 
      break; 
    } 
    encrypt += new Character((char)((int)flag.charAt(i) - (i % 10))).toString();
    if ((i * 5) == 0) 
    { 
      break; 
    }
}
```
</pre>
<h3><b>Solution</b></h3>
<p align='justify'>Diberikan script encryption java, metode dari encryption-nya yaitu setiap ord character dikurangi -1 hingga -10 secara berulang kali, berikut script penyelesaiannya</p>

```python3
enc_flag = 'CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|'
key_flag = [i for i in range(-9,1)][::-1]*4
for i,j in zip(enc_flag,key_flag):
    print(chr(ord(i)-j),end='')#CTFR{j4v4_3ncrypt10n_1s_g00d???}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{j4v4_3ncrypt10n_1s_g00d???}
</pre>
