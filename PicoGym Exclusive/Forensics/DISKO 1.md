<h1>DISKO 1</h1>
<h3>Description</h3>
<label>Can you find the flag in this disk image?
Download the disk image <a href='https://artifacts.picoctf.net/c/538/disko-1.dd.gz'>here</a>.
</label>
<h3>Solution</h3>
<label>Strings dan grep</label>

```console
┌──(xxxx㉿Kali)-[/home/xxxxx/Downloads/PicoCTF]
└─# strings -a disko-1.dd | grep -i 'picoCTF'                
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
```
<h3>Flag</h3>
<pre>
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
</pre>
