<h1><b>Check Comment</b></h1>
<pre>
Pada sebuah file gambar, bisa kita tambahkan komentar juga loh, Nah coba cari tahu komentar yang di tambahkan pada gambar dibawah ini

Challenge --> <a href='https://mega.nz/#!R84V2KrA!3GQ8jFTglK_ObMeJx_oXRGJ5SCmMDy7gBUzGZ6NgWeM'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Dengan tool Exiftool</p>

```console
root@Python:/home/venom/Downloads# exiftool kepiting.jpg | grep -i comment
XP Comment                      : CTFR{c0mm3nt_1n_1m4g3_d3t41ls}
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
CTFR{c0mm3nt_1n_1m4g3_d3t41ls}
</pre>
