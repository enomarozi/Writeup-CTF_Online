<h1><b>Zipper</b></h1>
<pre>
Help these gentlemen with their zips

<a href="http://static.beast.sdslabs.co/static/Zipper/JoJo1.jpg">JoJo1.jpg</a>
</pre>
<h3><b>Solution</b></h3>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/JoJo1.jpg">
</p>
<p>Flag berada di 2 tempat, meskipun flagnya sama, pertama eksekusi perintah string dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# strings -a JoJo1.jpg | grep -i flag
flag.txtflag{0h?_Y0ur3_4ppr04ch1ng_M3?}
flag.txt
root@Python:/home/venom/Downloads# 
```
<p>Kedua, Ekstrak file dengan foremost, maka didapatkan file Zip, lalu unzip file Zip tersebut dan cat file</p>

```console
root@Python:/home/venom/Downloads# foremost JoJo1.jpg 
Processing: JoJo1.jpg
|foundat=flag.txtflag{0h?_Y0ur3_4ppr04ch1ng_M3?}
PK?

*|
root@Python:/home/venom/Downloads# cd output/zip/
root@Python:/home/venom/Downloads/output/zip# unzip 00000186.zip 
Archive:  00000186.zip
 extracting: flag.txt                
root@Python:/home/venom/Downloads/output/zip# cat flag.txt 
flag{0h?_Y0ur3_4ppr04ch1ng_M3?}
root@Python:/home/venom/Downloads/output/zip# 
```
<h3><b>Flag</b></h3>
<pre>
flag{0h?_Y0ur3_4ppr04ch1ng_M3?}
</pre>
