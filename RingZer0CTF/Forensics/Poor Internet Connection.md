<h1><b>Poor Internet Connection</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/8d4ccebced1c7e68912ec01acc3ccf93.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file ekstensi pcap</p>
<p align='center'>
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/Poor%20internet%20connection.png">
</p>
<p>Seperti yang dapat dilihat, rata-rata paket yang tercapture yaitu protokol TCP. dan jika kita perhatikan pada protokol HTTP disana terdapat 2 file yaitu
secret.txt dan flag.zip.</p>
<p>Pada secret.txt lihat Follow TCP stream, <b>klik paket --> Follow --> TCP Stream</b>, dan hasil</p>
<pre>
the password for zip file is : ZipYourMouth
</pre>
<p>Dan untuk flag.zip, Ekstrak file pcap dengan tool foremost</p>

```console
root@Python:/home/venom/Downloads# ls
4545700e0e0dbc27cc964791f1cd30fa.pcap  8d4ccebced1c7e68912ec01acc3ccf93.zip
root@Python:/home/venom/Downloads# foremost 4545700e0e0dbc27cc964791f1cd30fa.pcap 
Processing: 4545700e0e0dbc27cc964791f1cd30fa.pcap
|foundat=flag.txtUT	
foundat=garbage.0UT	
*|
root@Python:/home/venom/Downloads# ls
4545700e0e0dbc27cc964791f1cd30fa.pcap  8d4ccebced1c7e68912ec01acc3ccf93.zip  output
root@Python:/home/venom/Downloads# cd output/
root@Python:/home/venom/Downloads/output# ls
audit.txt  zip
root@Python:/home/venom/Downloads/output# cd zip/
root@Python:/home/venom/Downloads/output/zip# ls
00002159.zip
root@Python:/home/venom/Downloads/output/zip# 
```
<p>Terakhir, Ekstrak file zip dengan password yang didapatkan</p>

```console
root@Python:/home/venom/Downloads/output/zip# 7z x 00002159.zip 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (306A9),ASM,AES-NI)

Scanning the drive for archives:
1 file, 291 bytes (1 KiB)

Extracting archive: 00002159.zip

ERRORS:
Unavailable start of archive

--
Path = 00002159.zip
Type = zip
ERRORS:
Unavailable start of archive
Offset = -1017724
Physical Size = 1018015

ERROR: Unavailable data : garbage.0
                
Enter password (will not be echoed):
               
Sub items Errors: 1

Archives with Errors: 1

Open Errors: 1

Sub items Errors: 1
root@Python:/home/venom/Downloads/output/zip# ls
00002159.zip  flag.txt
root@Python:/home/venom/Downloads/output/zip# cat flag.txt 
Flag-qscet5234diQ
```
<h3><b>Flag</b></h3>
<pre>
Flag-qscet5234diQ
</pre>
