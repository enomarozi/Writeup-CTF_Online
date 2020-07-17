<h1><b>NOOBHOME</b></h1>
<pre>
This year, n00b finally decided to design some ctf challenges on his own, and has made his first simple challenge. 
He takes regular compressed backups of his home folder (as is good practice), but he forgot to secure the backup. 
Can you find the flag that he has hidden in the challenge?

http://static.beast.sdslabs.co/static/NOOBHOME/noobhome.tar.gzHint: Look everywhere
</pre>
<b><h3>Solution</h3></b>
<p>Tak ambil ribet, ekstrak file lalu eksekusi perintah strings dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# tar xvf noobhome.tar.gz 
noobhome.ext4
root@Python:/home/venom/Downloads# strings -a noobhome.ext4 | grep -i ctf{
CTF{h1dden_h1story_c4n_b3_f0und}
root@Python:/home/venom/Downloads# 
```

<b><h3>Flag</h3></b>
<pre>
CTF{h1dden_h1story_c4n_b3_f0und}
</pre>
