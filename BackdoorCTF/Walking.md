<h1><b>Walking</b></h1>
<pre>
Sometimes an image contains more than it looks.

http://static.beast.sdslabs.co/static/noob/bing.jpg
</pre>
<h3><b>Solution</b></h3>
<p align='center'>
    <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/bing.jpg">
</p>
<p>Periksa file dengan binwalk, maka didalam file terdapat file Zip. Lanjut, ekstrak file dengan foremost dan read file flag.txt pada file Zip</p>

```console
root@Python:/home/venom/Downloads# binwalk bing.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
24907         0x614B          Zip archive data, at least v2.0 to extract, name: Found/
24975         0x618F          Zip archive data, at least v2.0 to extract, uncompressed size: 33, name: Found/flag.txt
25278         0x62BE          End of Zip archive, footer length: 22

root@Python:/home/venom/Downloads# foremost bing.jpg 
Processing: bing.jpg
|foundat=Found/UT
foundat=Found/flag.txtUT
*|
root@Python:/home/venom/Downloads# cd output/
root@Python:/home/venom/Downloads/output# cd zip/
root@Python:/home/venom/Downloads/output/zip# unzip 00000048.zip 
Archive:  00000048.zip
   creating: Found/
  inflating: Found/flag.txt          
root@Python:/home/venom/Downloads/output/zip# cat Found/flag.txt 
flag{n00b_kn0ws_abou7_foresincs}
```
<h3><b>Flag</b></h3>
<pre>
flag{n00b_kn0ws_abou7_foresincs}
</pre>
