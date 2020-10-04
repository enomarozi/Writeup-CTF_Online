<h1><b>Simple Steganography</h1></b>
<pre>
Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"

<a href='https://ctflearn.com/challenge/download/894'>File.jpeg</a>
</pre>
</b><h3>Solution</h3></b>
<p>Ikuti langkah dibawah ini, dengan tool steghide dan string,base64 command</p>

```console
root@Python:/home/venom/Downloads# strings -a Minions1.jpeg | head -5
JFIF
0Photoshop 3.0
8BIM
myadmin
!1#%)+...
root@Python:/home/venom/Downloads# steghide --extract -sf Minions1.jpeg 
Enter passphrase: myadmin
wrote extracted data to "raw.txt".
root@Python:/home/venom/Downloads# 
root@Python:/home/venom/Downloads# cat raw.txt | base64 -d
CTFlearn{this_is_fun}
root@Python:/home/venom/Downloads# 
```
<p>password untuk steghide terdapat didekat header file.jpeg</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{this_is_fun}
</pre>
