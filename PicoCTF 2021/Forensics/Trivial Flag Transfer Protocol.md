<h1>Trivial Flag Transfer Protocol</h1>
<h3>Description</h3>
<pre>
Figure out how they moved the flag.
<a href='https://challenge-files.picoctf.net/c_wily_courier/9f32bef3f1ad1e5a7c5992f3c1e86619ff557537080e163e5a6d9f01070192a9/tftp.pcapng'>tftp.pcapng</a>
</pre>
<h3>Solution</h3>
<label>Export Object TFTP dari file pcapng</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# ls -al          
total 38144
drwxr-xr-x  2 root  root      4096 Apr 11 20:55 .
drwxr-xr-x 21 venom venom    24576 Apr 11 20:53 ..
-rw-r--r--  1 root  root       138 Apr 11 08:04 instructions.txt
-rw-r--r--  1 root  root    824518 Apr 11 08:02 picture1.bmp
-rw-r--r--  1 root  root  36578358 Apr 11 08:02 picture2.bmp
-rw-r--r--  1 root  root   1466574 Apr 11 08:02 picture3.bmp
-rw-r--r--  1 root  root        70 Apr 11 08:05 plan
-rw-r--r--  1 root  root    138310 Apr 11 08:02 program.deb
```
<label>file instructions.txt dan plan decode dengan rot13 lalu sesuaikan textnya, dan hasilnya</label>

<pre>
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# cat instructions.txt 
TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAGT RANSFER.FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# cat plan            
I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE. CHECK OUT THE PHOTOS
</pre>
<h3>File program.deb merupakan file dari steghide</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# dpkg-deb -c program.deb 
drwxr-xr-x root/root         0 2014-10-15 07:02 ./
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/doc/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/doc/steghide/
-rw-r--r-- root/root      6066 2014-10-15 07:02 ./usr/share/doc/steghide/ABOUT-NLS.gz
-rw-r--r-- root/root      2771 2014-10-15 07:02 ./usr/share/doc/steghide/LEAME.gz
-rw-r--r-- root/root      2488 2003-09-28 22:30 ./usr/share/doc/steghide/README.gz
-rw-r--r-- root/root      1763 2014-10-15 07:01 ./usr/share/doc/steghide/changelog.Debian.gz
-rw-r--r-- root/root       215 2014-10-15 07:01 ./usr/share/doc/steghide/changelog.Debian.amd64.gz
-rw-r--r-- root/root       860 2003-10-11 16:03 ./usr/share/doc/steghide/changelog.gz
-rw-r--r-- root/root      1088 2014-10-15 07:01 ./usr/share/doc/steghide/copyright
-rw-r--r-- root/root       787 2003-05-03 19:41 ./usr/share/doc/steghide/TODO
-rw-r--r-- root/root      1957 2003-10-11 16:03 ./usr/share/doc/steghide/HISTORY
-rw-r--r-- root/root       895 2003-10-11 16:04 ./usr/share/doc/steghide/CREDITS
-rw-r--r-- root/root       598 2003-09-27 14:40 ./usr/share/doc/steghide/BUGS
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/man/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/man/man1/
-rw-r--r-- root/root      3760 2014-10-15 07:02 ./usr/share/man/man1/steghide.1.gz
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/ro/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/ro/LC_MESSAGES/
-rw-r--r-- root/root     30028 2014-10-15 07:02 ./usr/share/locale/ro/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/fr/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/fr/LC_MESSAGES/
-rw-r--r-- root/root     30386 2014-10-15 07:02 ./usr/share/locale/fr/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/de/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/de/LC_MESSAGES/
-rw-r--r-- root/root     30268 2014-10-15 07:02 ./usr/share/locale/de/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/es/
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/share/locale/es/LC_MESSAGES/
-rw-r--r-- root/root     29198 2014-10-15 07:02 ./usr/share/locale/es/LC_MESSAGES/steghide.mo
drwxr-xr-x root/root         0 2014-10-15 07:02 ./usr/bin/
-rwxr-xr-x root/root    290888 2014-10-15 07:02 ./usr/bin/steghide
```

<label>Coba extract secret dari semua file bmp, dengan password dari file plan "DUEDILIGENCE"</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# steghide extract -sf picture1.bmp                             
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# steghide extract -sf picture2.bmp
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# steghide extract -sf picture3.bmp
Enter passphrase: 
wrote extracted data to "flag.txt".
                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/Export_wr]
└─# cat flag.txt 
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
<h3>Flag</h3>
<pre>
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
</pre>
