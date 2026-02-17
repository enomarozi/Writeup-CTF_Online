<h1>Bases</h1>
<h3>Description</h3>
<pre>
What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "picoCTF{$(echo bDNhcm5fdGgzX3IwcDM1 | base64 -d)}"
picoCTF{l3arn_th3_r0p35}
```
<h3>Flag</h3>
<pre>
picoCTF{l3arn_th3_r0p35}
</pre>
