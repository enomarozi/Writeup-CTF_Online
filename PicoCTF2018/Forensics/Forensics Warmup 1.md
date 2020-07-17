<h1><b>Forensics Warmup 1</h1></b>
<pre>
Can you unzip this <a href="https://2018shell.picoctf.com/static/1c1504eeb8236a26646a02bb29620923/flag.zip">file</a> for me and retreive the flag?

</pre>
</b><h3>Solution</h3></b>
<p>Unzip dan buka file</p>

```console
root@Python:/home/venom/Downloads# unzip flag.zip 
Archive:  flag.zip
  inflating: flag.jpg                
root@Python:/home/venom/Downloads# eog flag.jpg 
```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/PicoCTF2018/Forensics/Images/Forensics%20Warmup%201.jpg">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{welcome_to_forensics}
</pre>
