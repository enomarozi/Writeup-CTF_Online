<h1><b>Noise?</h1></b>
<pre>
Hey! I have intercepted this https://mega.nz/#!SPhCwATa!2i8_wI4t1j3VdnauXDB1OaW60l5hJAr3ylTxo_K9FeY 
from the Center for Interesting Arrangements. 
Out of all the documents the CIA holds, this seems to stand out because I don't see any "interesting arrangement" in this image. 
Pretty sure that this is just a bunch of noise... or is it? Look at this file closely and you'll (definitely) agree with me!
</pre>
</b><h3>Solution</h3></b>
<p>Analisa file image dengan tool zsteg</p>

```console
root@Python:/home/venom/Downloads# zsteg noise.png -a | head -n 5
imagedata           .. text: "PPPNNNGGG\r\r\r\n\n\n"
b4,rgb,lsb,xy       .. text: "DDDDC3\" "
b8,r,lsb,xy         .. file: PNG image data, 250 x 287, 8-bit/color RGB, non-interlaced
b8,rgb,lsb,xy       .. text: "PPPNNNGGG\r\r\r\n\n\n"
b8,rgb,msb,xy       .. text: "PPPXXXPPP"
root@Python:/home/venom/Downloads# 
```
<p>Dapat dilihat disana terdapat file PNG 250x287 pada LSB red. Ekstrak file dengan tool stegsolve seperti pada gambar dibawah ini dan simpan</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/noise.jpg'>
</p>Selanjutnya ulangi langkah pertama pada gambar yang baru didapat dan lakukan terus hingga 13 kali maka flag terdapat pada file terakhir dengan zsteg tool</p>

```console
root@Python:/home/venom/Downloads# ls
10.png  11.png  12.png  13.png  1.png  2.png  3.png  4.png  5.png  6.png  7.png  8.png  9.png  noise.jpg  noise.png
root@Python:/home/venom/Downloads# zsteg 13.png -a| head -n 10                                            |.               |
imagedata           .. text: "GGGooooooddd   jjj"
b4,rgb,lsb,xy       .. text: "DFfDC3\"/"
b8,r,lsb,xy         .. text: "Good job! The flag is: flag{n0t_n0ise_4ft3r_4ll}"
b8,rgb,lsb,xy       .. text: "GGGooooooddd   jjjooobbb!!!   TTThhheee   ffflllaaaggg   iiisss:::   ffflllaaaggg{{{nnn000ttt___nnn000iiissseee___444fffttt333rrr___444llllll}}}"
b8,rgb,msb,xy       .. text: ",,,fff..."
b4,rgb,lsb,xy,prime .. file: MPEG ADTS, layer II, v2,  32 kbps, 24 kHz, 2x Monaural
root@Python:/home/venom/Downloads# 

```
</b><h3>Flag</h3></b>
<pre>
flag{n0t_n0ise_4ft3r_4ll}
</pre>
