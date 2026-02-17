<h1>mus1c</h1>
<h3>Description</h3>
<pre>
I wrote you a <a href='https://challenge-files.picoctf.net/c_fickle_tempest/375750638d0c9c3a142d094f5b5dbba4e9739029e4215e633f7e55151562f977/lyrics.txt'>song</a>. Put it in the picoCTF{} flag format.
</pre>
<h3>Solution</h3>

<label>Eksekusi lyric ke interpreter esolang program <a href='https://codewithrockstar.com/online.html'>rockstar</a>, dan didapatkan integer</label>

<pre>
114 114 114 111 99 107 110 114 110 48 49 49 51 114
</pre>

```python3
int_str = "114 114 114 111 99 107 110 114 110 48 49 49 51 114".split(' ')
print('picoCTF{',end='')
for i in int_str:
    print(chr(int(i)),end='')
print('}',end='')
```
<h3>Flag</h3>
<pre>
picoCTF{rrrocknrn0113r}
</pre>
