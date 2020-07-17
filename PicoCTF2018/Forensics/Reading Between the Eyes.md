<h1><b>Reading Between the Eyes</h1></b>
<pre>
Stego-Saurus hid a message for you in this <a href="https://2018shell.picoctf.com/static/3e423171eed198e8425524a1b052869b/husky.png">image</a>, can you retreive it?
</pre>
</b><h3>Solution</h3></b>
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/husky.png" width=900>
</p>
<p>Gunakan tool zsteg pada file dan grep</p>

```console
root@Python:/home/venom/Downloads# zsteg husky.png | grep -i pico
b1,rgb,lsb,xy       .. text: "picoCTF{r34d1ng_b37w33n_7h3_by73s}"
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{r34d1ng_b37w33n_7h3_by73s}
</pre>
