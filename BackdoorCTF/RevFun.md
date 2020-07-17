<h1><b>RevFun</b></h1>
<pre>
n00b had written his password down weirdly in the source code...
but then he lost the source and only has the <a href="http://static.beast.sdslabs.co/static/REVFUN/revfun">binary</a>... help him out...

nc hack.bckdr.in 16016
</pre>
<h3><b>Solution</b></h3>
<p>Eksekusi perintah string pada file dan lihat, disana terdapat string terbalik <b>dlr0w_s1h7_s1_yz4rC</b>, yang sepertinya mencurigakan, jalankan netcat <b>nc hack.bckdr.in 16016</b>,
ternyata di-netcat ada form permintaan password. reverse string yang didapatkan tadi dan gunakan sebagai password pada form netcat</p>

```console
root@Python:/home/venom/Downloads# echo "dlr0w_s1h7_s1_yz4rC" | rev | nc hack.bckdr.in 16016
Password: The Flag is: CTF{murder_for_a_jar_of_red_rum}
root@Python:/home/venom/Downloads# 
```

<h3><b>Flag</b></h3>
<pre>
CTF{murder_for_a_jar_of_red_rum}
</pre>
