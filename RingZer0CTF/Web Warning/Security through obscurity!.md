<h1><b></h1></b>
<pre>
You don't have admin access.
</pre>
</b><h3>Solution</h3></b>
<p align='justify'>Perhatikan Session Cookie, disana terdapat encoding base64 dengan name AUTH</p>
<p>Value --> Z3Vlc3QsYzM5YzE3MmFkMGVmNzQ3ZiwxNjA0NzY2MjM4LGZhbHNlOmM2YTMzNjVlZjY1NjhkMjJkZGQyMmUzYzAyN2NiNzg2</p>
<p>Hasil Decode --> guest,c39c172ad0ef747f,1604766238,false:c6a3365ef6568d22ddd22e3c027cb786</p>
<p>Dari hasil decode kita bisa membaginya beberapa list seperti dibawah</p>
<pre>
guest --> user
c39c172ad0ef747f --> random hexa
1604766238 --> unix timestamp
false --> status
c6a3365ef6568d22ddd22e3c027cb786 --> MD5
</pre>
<p align='justify'>Dari beberapa list diatas, user guest ganti menjadi admin, dan unix timestamp ditambahkan saja 36000 (1604766238 + 36000 = 1604802238), lanjut
status false ganti menjadi true, Terakhir ganti MD5nya yaitu hash dari seluruh list</p>
<p>admin,c39c172ad0ef747f,1604802238,true:a043f4246076d72a5d46a3a66231f302 --> YWRtaW4sYzM5YzE3MmFkMGVmNzQ3ZiwxNjA0ODAyMjM4LHRydWU6YTA0M2Y0MjQ2MDc2ZDcyYTVkNDZhM2E2NjIzMWYzMDI=</p>
<p>Ganti base64 pada AUTH dengan base64 yang baru dan reload halaman</p>
</b><h3>Flag</h3></b>
<pre>
FLAG-Feg03OSzWhxO03K94108100f
</pre>
