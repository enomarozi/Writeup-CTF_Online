<h1><b>Exif</h1></b>
<pre>
If only the password were in the image?

https://mega.nz/#!SDpF0aYC!fkkhBJuBBtBKGsLTDiF2NuLihP2WRd97Iynd3PhWqRw 
You could really ‘own’ it with exif.
</pre>
</b><h3>Solution</h3></b>
<p>Sesuai judul, eksekusi exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool Computer-Password-Security-Hacker\ -\ Copy.jpg | grep -i flag
Owner Name                      : flag{3l1t3_3x1f_4uth0r1ty_dud3br0}
APP14 Flags 0                   : [14], Encoded with Blend=1 downsampling
APP14 Flags 1                   : (none)
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
flag{3l1t3_3x1f_4uth0r1ty_dud3br0}
</pre>
