<h1><b>Find Differ3nt</b></h1>
<pre>
Cari perbedaan dari kedua teks dibawah ini

Challenge --> <a href='https://mega.nz/#!spoG1ZqY!yE0v9D3-GMRKEUQCnw-ofqhD0QKItlYEyA41V6dlakg'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Buat script looping untuk mencari perbedaannya</p>

```python3
file_apple = open('apple.txt','r').read()
file_coconut = open('coconut.txt','r').read()
for i,j in zip(file_apple,file_coconut):
    if i != j:
        print(i,end='')#CTFR{y0u_4r3_n0w_c4n_s33_th3_d1ff3r3nt}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{y0u_4r3_n0w_c4n_s33_th3_d1ff3r3nt}
</pre>
