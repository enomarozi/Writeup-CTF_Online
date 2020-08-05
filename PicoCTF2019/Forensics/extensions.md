<h1><b>extensions</h1></b>
<pre>
This is a really weird text file <a file='https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt'>TXT</a>? Can you find the flag?
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file, dan ternyata itu berupa file PNG, change header TXT ke PNG file</p>

```console
root@Python:/home/venom/Downloads# file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
root@Python:/home/venom/Downloads# mv flag.txt flag.png
root@Python:/home/venom/Downloads# eog flag.png
```
<p align='center'> 
<img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2019/Forensics/Images/flag.png'>
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{now_you_know__about_extensions}
</pre>
