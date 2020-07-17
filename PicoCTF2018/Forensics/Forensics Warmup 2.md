<h1><b>Forensics Warmup 2</h1></b>
<pre>
Hmm for some reason I can't open this <a href="https://2018shell.picoctf.com/static/032d65124629e45f0b5151aad4e7b5b1/flag.png">PNG</a>? Any ideas?
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file, lalu ganti format file PNG ke JPG dan buka</p>

```console
root@Python:/home/venom/Downloads# file flag.png 
flag.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 75x75, segment length 16, baseline, precision 8, 909x190, components 3
root@Python:/home/venom/Downloads# mv flag.png flag.jpg
root@Python:/home/venom/Downloads# eog flag.jpg 
```
<p align="center">
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/Forensics%20Warmup%202.jpg">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{extensions_are_a_lie}
</pre>
