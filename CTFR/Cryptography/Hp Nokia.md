<h1><b>Hp Nokia</b></h1>
<pre>
Hp Nokia dulu sempat naik daun sampai dipakai dimana-mana, Dan tentunya untuk mengklik B saja harus klik nomor "2" 2 kali, Nah kali ini enkripsi yang dipakai pada challenge ini hanya sekedar Tap-Tap saja, Contohnya "Ayam" akan menjadi "2 999 2 6". Nah coba decode Hasil Tap-Tap

Flag : CTFR{8 2 7 8 2 7 6 2 66 8 2 7}.
</pre>
<h3><b>Solution</b></h3>
<p>Perhatikan tombol HP nokia lama, sesuaikan angka dan huruf yang dihasilkan</p>

```python
enc = "C T F R { 8 2 7 8 2 7 6 2 66 8 2 7 }".split(" ")
table_dtmf = {2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}
for i in enc:
    try:
        if int(i) == 0:
            print(" ",end="")
        elif int(i) != 0:
            a = len(i)
            print(table_dtmf[int(i[:1])][a-1],end="")
    except:
        print(i,end='')#CTFR{TAPTAPMANTAP}
```
<h3><b>Flag</b></h3>
<pre>
CTFR{TAPTAPMANTAP}
</pre>
