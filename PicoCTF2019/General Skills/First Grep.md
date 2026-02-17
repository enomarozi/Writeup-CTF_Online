<h1>First Grep</h1>
<h3>Description</h3>
<pre>
Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.
The flag is in this <a href='https://challenge-files.picoctf.net/c_fickle_tempest/aed2b98bf6b93877d7152565a69d1e8de53138c8443678caa2a1dbc20f16b075/file'>file</a>.
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# grep -io 'picoCTF{[^}]*}' file 
picoCTF{grep_is_good_to_find_things_01aE5e9d}
```
<h3>Flag</h3>
<pre>
picoCTF{grep_is_good_to_find_things_01aE5e9d}
</pre>
