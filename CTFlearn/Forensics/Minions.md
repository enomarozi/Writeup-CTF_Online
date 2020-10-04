<h1><b></h1></b>
<pre>
Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there: https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.
</pre>
</b><h3>Solution</h3></b>
<p>Ikuti langkah dibawah dengan tool binwalk dan command grep</p>

```console
root@Python:/home/venom/Downloads# binwalk -e Hey_You.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1144 x 1056, 8-bit/color RGBA, non-interlaced
91            0x5B            Zlib compressed data, compressed
868059        0xD3EDB         RAR archive data, version 5.x

root@Python:/home/venom/Downloads# grep -iR a
_Hey_You.png.extracted/..txt:https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZko
Binary file _Hey_You.png.extracted/5B.zlib matches
Binary file _Hey_You.png.extracted/D3EDB.rar matches
Binary file Only_Few_Steps.jpg matches
Binary file Hey_You.png matches
root@Python:/home/venom/Downloads# 
```
<p>Disana kita mendapatkan link download mega, dan download filenya maka didapatkan masih file.jpg juga. Lanjut analisa file tersebut</p>

```console
root@Python:/home/venom/Downloads# binwalk -e Only_Few_Steps.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
426           0x1AA           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
141318        0x22806         RAR archive data, version 5.x
root@Python:/home/venom/Downloads# cd _Only_Few_Steps.jpg.extracted/
root@Python:/home/venom/Downloads/_Only_Few_Steps.jpg.extracted# strings -a * | grep -i CTF
CTF{VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=)
root@Python:/home/venom/Downloads/_Only_Few_Steps.jpg.extracted#
```
<p>Dan decode base64 diatas 4 kali</p>

```console
root@Python:/home/venom/Downloads# echo "VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=" | base64 -d | base64 -d | base64 -d | base64 -d
M1NI0NS_ARE_C00L
root@Python:/home/venom/Downloads# 
```

</b><h3>Flag</h3></b>
<pre>
CTFlearn{M1NI0NS_ARE_C00L}
</pre>
