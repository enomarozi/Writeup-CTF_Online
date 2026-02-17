<h1>2warm</h1>
<h3>Description</h3>
<pre>
Can you convert the number 42 (base 10) to binary (base 2)?
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "picoCTF{$(echo 'obase=2; 42' | bc)}"
picoCTF{101010}

```
<h3>Flag</h3>
<pre>
picoCTF{101010}
</pre>
