<h1>Brainsick</h1>
<pre>
<a href="https://ringzer0ctf.com/files/fbeaf2dcc012234eca5aa389cf0edf89.zip">File</a>
</pre>
<h3>Solution</h3>

```console
root@Python:/home/venom/Downloads# unzip fbeaf2dcc012234eca5aa389cf0edf89.zip 
Archive:  fbeaf2dcc012234eca5aa389cf0edf89.zip
  inflating: 5411333e505440020a1799da6071851b.gif  
root@Python:/home/venom/Downloads# file 5411333e505440020a1799da6071851b.gif 
5411333e505440020a1799da6071851b.gif: GIF image data, version 89a, 440 x 385
root@Python:/home/venom/Downloads# binwalk 5411333e505440020a1799da6071851b.gif 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 440 x 385
78301         0x131DD         RAR archive data, version 4.x, first volume type: MAIN_HEAD

root@Python:/home/venom/Downloads# foremost 5411333e505440020a1799da6071851b.gif 
Processing: 5411333e505440020a1799da6071851b.gif
|*|
root@Python:/home/venom/Downloads# cd output/rar/
root@Python:/home/venom/Downloads/output/rar# unrar x 00000152.rar 

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal


Extracting from 00000152.rar

Extracting  flag.gif                                                  OK 
All OK
root@Python:/home/venom/Downloads/output/rar# eog flag.gif 

```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/RingZer0CTF/Steganography/Images/flag.gif">
</p>
<h3>Flag</h3>
<pre>
Flag-Th2K4s83uQh9xA
</pre>
