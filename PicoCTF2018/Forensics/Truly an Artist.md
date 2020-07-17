<h1><b>Truly an Artist</h1></b>
<pre>
Can you help us find the flag in this <a href="https://2018shell.picoctf.com/static/9b8863e30054675ce78328df28c601db/2018.png">Meta-Material</a>? 
You can also find the file in /problems/truly-an-artist_4_cdd9e325cf9bacd265b98a7fe336e840.
</pre>
</b><h3>Solution</h3></b>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/2018.png">
</p>
<p>Eksekusi perintah exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool 2018.png | grep pico
Artist                          : picoCTF{look_in_image_13509d38}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{look_in_image_13509d38}
</pre>
