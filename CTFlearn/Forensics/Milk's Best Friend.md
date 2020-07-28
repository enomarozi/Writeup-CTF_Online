<h1><b>Milk's Best Friend</h1></b>
  
 
<pre>
There's nothing I love more than oreos, lions, and winning. 
https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y 
Have Fun :)
</pre>
</b><h3>Solution</h3></b>
<p>Hasil ientifikasi file terdapat file RAR didalamnya, ekstrak file dengan binwalk, lalu eksekusi perintah string dan grep</p>

```console
root@Python:/home/venom/Downloads# binwalk -e oreo.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
9515          0x252B          RAR archive data, version 4.x, first volume type: MAIN_HEAD

root@Python:/home/venom/Downloads# cd _oreo.jpg.extracted/
root@Python:/home/venom/Downloads/_oreo.jpg.extracted# ls
252B.rar  a  b.jpg
root@Python:/home/venom/Downloads/_oreo.jpg.extracted# strings * | grep -i flag
This is not the flag you are looking for.Q"t
This is not the flag you are looking for.
Finally, flag{eat_more_oreos}
root@Python:/home/venom/Downloads/_oreo.jpg.extracted#
```
</b><h3>Flag</h3></b>
<pre>
flag{eat_more_oreos}
</pre>
