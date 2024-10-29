<h1>Big Zip</h1>
<h3>Description</h3>
<pre>
Unzip this archive and find the flag.
<a href='https://artifacts.picoctf.net/c/505/big-zip-files.zip'>Download zip file</a>
</pre>
<h3>Solution</h3>
<p>Unzip dan Grep Directory</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/big-zip-files]
└─# grep -iR 'pico'                                
folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```
<h3>Flag</h3>
<pre>
picoCTF{gr3p_15_m4g1c_ef8790dc}
</pre>
