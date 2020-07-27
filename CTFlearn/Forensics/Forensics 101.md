<h1><b>Forensics 101</h1></b>
<pre>
Think the flag is somewhere in there. Would you help me find it? 
https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah strings dan grep pada file image</p>

```console
root@Python:/home/venom/Downloads# file 95f6edfb66ef42d774a5a34581f19052.jpg 
95f6edfb66ef42d774a5a34581f19052.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 236x218, components 3
root@Python:/home/venom/Downloads# strings 95f6edfb66ef42d774a5a34581f19052.jpg | grep -i flag
flag{wow!_data_is_cool}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
flag{wow!_data_is_cool}
</pre>
