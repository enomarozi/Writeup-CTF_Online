<h1><b>Help Me to Decode</b></h1>
<pre>
Ada sebuah code berbahasa Python dan disana memiliki teks yang sangat rahasia, akan tetapi kami tidak dapat membaca teks tersebut. Apakah kalian bisa bantu kami untuk mengdecode hasil enkripsi tersebut ?

Download : <a href='http://rasyidmf.com/assets/challenge/pg/helpmetodecode/a'>Decode This</a>
</pre>
<h3><b>Solution</b></h3>
<p align='justify'>Kita diminta untuk decrypt flag yang sudah diencrypt, kelemahan encryptnya terdapat dari operasinya yaitu pengurangan(-) yang bisa diganti menjadi penambahan(+)</p>

```python
flag = ">OAMva,mnoZo,h.Z.i^mtkoZ,iZktoc+i:x"
Flag = ""
for x in flag:
    Flag += chr(ord(x) + 0x0000000005 % 0xFFFFFFFFFFF)

print(Flag) #CTFR{f1rst_t1m3_3ncrypt_1n_pyth0n?}
```

<h3><b>Flag</b></h3>
<pre>
CTFR{f1rst_t1m3_3ncrypt_1n_pyth0n?}
</pre>
