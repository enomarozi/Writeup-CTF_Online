<h1><b>So Meta</h1></b>
<pre>
Find the flag in this <a href='https://2019shell1.picoctf.com/static/707dcf0533b53e911b2f7496ebdf9a72/pico_img.png'>picture</a>. You can also find the 
file in /problems/so-meta_4_4e8d17dbd28e1fdfe82ba31ceb021615.
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah string dan grep</p>

```console
root@Python:/home/venom/Downloads# strings -a pico_img.png | grep -i pico
picoCTF{s0_m3ta_9a16fd1d}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{s0_m3ta_9a16fd1d}
</pre>
