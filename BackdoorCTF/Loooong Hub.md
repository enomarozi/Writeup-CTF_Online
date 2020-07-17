<h1><b>Loooong Hub</b></h1>
<pre>
Hey, I am h4ck3y3. My original name and github account will help you in the way!
</pre>
<h3><b>Solution</b></h3>
<p>Sesuai pada soal, itu merupakan hint yaitu github account dan creater name. Check seluruh repositorinya maka disana terdapat repository mencurigakan pada alamat</p>
<pre>
https://github.com/Aniket21mathur/Looking-For-Something-
</pre>
<p>Download repositori dan eksekusi perintah grep</p>

```console
root@Python:/home/venom/Downloads# git clone https://github.com/Aniket21mathur/Looking-For-Something-
Cloning into 'Looking-For-Something-'...
remote: Enumerating objects: 64, done.
remote: Total 64 (delta 0), reused 0 (delta 0), pack-reused 64
Unpacking objects: 100% (64/64), 1.92 MiB | 891.00 KiB/s, done.
root@Python:/home/venom/Downloads# grep -iR flag
Looking-For-Something-/README.md:find something like flag{} :) :)
Looking-For-Something-/_sass/ext/_fonts.scss: /*flag{th3r3_y0u_g0_n00b}*/
Looking-For-Something-/.git/hooks/fsmonitor-watchman.sample:		# return the fast "everything is dirty" flag to git and do the
```
<p>Dan flag didapatkan pada direktori file Looking-For-Something-/_sass/ext/_fonts.scss</p>
<h3><b>Flag</b></h3>
<pre>
flag{th3r3_y0u_g0_n00b}
</pre>
