<h1>Lets Warm Up</h1>
<h3>Description</h3>
<pre>
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "picoCTF{$(echo 70 | xxd -r -p)}"
picoCTF{p}
```
<h3>Flag</h3>
<pre>
picoCTF{p}
</pre>
