<h1><b>DA-VINCI</b></h1>
<pre>
n00b hid secret data in this image. Help me recover it.

<a href="http://static.beast.sdslabs.co/static/DA-VINCI/stegano.jpg">Link</a>
</pre>
<h3><b>Solution</b></h3>
<p align="center">
    <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/davinci.jpg">
</p>
<p>Kita diberikan 1 file jpg, analisa seluruh raw bytes file dengan perintah string, disana terdapat <b>flag.txt</b> dan <b>password is monalisa</b>, ekstrak file image dengan foremost, 
dan ektrak file zip dengan password yang sudah didapatkan</p>

```console
root@Python:/home/venom/Downloads# foremost stegano.jpg 
Processing: stegano.jpg
|foundat=flag.txt�
*|
root@Python:/home/venom/Downloads# cd output/
jpg/ zip/ 
root@Python:/home/venom/Downloads# cd output/zip/
root@Python:/home/venom/Downloads/output/zip# 7z x 00000023.zip 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (306A9),ASM,AES-NI)

Scanning the drive for archives:
1 file, 193 bytes (1 KiB)

Extracting archive: 00000023.zip
--
Path = 00000023.zip
Type = zip
Physical Size = 193

    
Enter password (will not be echoed):
Everything is Ok

Size:       37
Compressed: 193
root@Python:/home/venom/Downloads/output/zip# cat flag.txt 
CTF{h3y_n00b_gr3at_st3g4n0_sk11ls!!}
root@Python:/home/venom/Downloads/output/zip#
```

<h3><b>Flag</b></h3>
<pre>
CTF{h3y_n00b_gr3at_st3g4n0_sk11ls!!}
</pre>
