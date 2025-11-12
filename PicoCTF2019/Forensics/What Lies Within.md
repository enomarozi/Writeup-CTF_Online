<h1>What Lies Within</h1>
<pre>
Theres something in the <a href='https://2019shell1.picoctf.com/static/aec3861fc4d5bce4d39dc0db196426de/buildings.png'>building</a>. Can you retrieve the flag?
</pre>
<h3>Solution</h3>
<p>tool zsteg didapatkan flag pada LSB bit 1 RGB</p>

```console
root@Python:/home/venom/Downloads# zsteg buildings.png 
b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"
root@Python:/home/venom/Downloads# 
```
<h3>Flag</h3>
<pre>
picoCTF{h1d1ng_1n_th3_b1t5}
</pre>
