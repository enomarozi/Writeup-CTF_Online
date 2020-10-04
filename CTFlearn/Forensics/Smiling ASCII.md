<h1><b>Smiling ASCII</h1></b>
<pre>
Find the flag on the smiling face.

<a href='https://ctflearn.com/challenge/download/903'>smiling.png</a>
</pre>
</b><h3>Solution</h3></b>
<p>Dengan tool zsteg kita sudah bisa mendapatkan hint dan flag</p>

```console
root@Python:/home/venom/Downloads# zsteg smiling.png -a
[?] 104 bytes of extra data after image end (IEND), offset = 0xe6cd
extradata:0         .. text: "RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg=="
b3,abgr,lsb,xy      .. file: very old 16-bit-int little-endian archive
b1,rgba,lsb,yx      .. file: AIX core file
b1,abgr,lsb,yx      .. file: AIX core file fulldump 32-bit
b8,g,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
b8,a,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
b4,r,lsb,yx,prime   .. file: AIX core file fulldump 32-bit
b4,g,lsb,yx,prime   .. file: AIX core file 32-bit
b8,g,lsb,yx,prime   .. text: "Flancixla"
b8,a,lsb,yx,prime   .. text: "Flancixla"
```
<p align='justify'>Disana terdapat hint berupa base64 yang jika didecode hasilnya "Did you know that pixels are, like the ascii table, numbered from 0 to 255?", yang terkait dengan LSB stego</p>
<p>Dan disana juga terdapat flag dari LSB green byte 1 s/d 8</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{ascii_pixel_flag}
</pre>
