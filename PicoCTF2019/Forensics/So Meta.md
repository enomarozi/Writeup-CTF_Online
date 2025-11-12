<h1>So Meta</h1>
<pre>
Find the flag in this <a href='https://2019shell1.picoctf.com/static/707dcf0533b53e911b2f7496ebdf9a72/pico_img.png'>picture</a>. You can also find the 
file in /problems/so-meta_4_4e8d17dbd28e1fdfe82ba31ceb021615.
</pre>
<h3>Solution</h3>
<p>string dan grep</p>

```console
root@Python:/home/venom/Downloads# strings -a pico_img.png | grep -i pico
picoCTF{s0_m3ta_9a16fd1d}
root@Python:/home/venom/Downloads# 
```
<h3>Flag</h3>
<pre>
picoCTF{s0_m3ta_9a16fd1d}
</pre>
