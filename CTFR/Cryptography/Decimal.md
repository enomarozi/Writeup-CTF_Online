<h1><b>Decimal</b></h1>
<pre>
Sistem bilangan desimal/persepuluhan adalah sistem bilangan yang menggunakan 10 macam angka dari 0,1, sampai 9. Setelah angka 9, angka berikutnya adalah 1 1, 1 2, dan seterusnya.

Flag : 67 84 70 82 123 52 115 99 49 49 95 99 48 100 51 125
</pre>
<h3><b>Solution</b></h3>
<p>Decode Desimal to Ascii</p>

```python
desimal = "67 84 70 82 123 52 115 99 49 49 95 99 48 100 51 125".split(' ')
for i in desimal:
    print(chr(int(i)),end='')
```
<h3><b>Flag</b></h3>
<pre>
CTFR{4sc11_c0d3}
</pre>
