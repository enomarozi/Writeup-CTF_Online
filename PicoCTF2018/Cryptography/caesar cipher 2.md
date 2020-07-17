<h1><b>caesar cipher 2</h1></b>
<pre>
Can you help us decrypt this <a href=https://2018shell.picoctf.com/static/dc2ed8be2af39097fcbc671f08b9ffa0/ciphertext">message</a>? We believe it is a form of a caesar cipher. 
You can find the ciphertext in /problems/caesar-cipher-2_4_23c82ed24f4436e96acc1f9f22dc8799 on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p>Lakukan penambahan disetiap orde character, disini saya melakukan bruteforce</p>

```python
def xoor(n):
    data = "d]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q"
    flag = ""
    for i in data:
        flag += chr(ord(i)+n)
    if "pico" in flag:
        print("Key :",n,"Flag is :",flag)
for j in range(100):
    xoor(j)
```
<p>Hasil program</p>
<pre>
Key : 12 Flag is : picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
</pre>
<p>Jadi kuncinya, disetiap orde ditambah 12</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{cAesaR_CiPhErS_juST_aREnT_sEcUrE}
</pre>
