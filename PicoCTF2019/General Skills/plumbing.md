<h1>plumbing</h1>
<h3>Description</h3>
<pre>
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?
Connect to fickle-tempest.picoctf.net 50924.
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# nc fickle-tempest.picoctf.net 50924 | grep -io "picoCTF{[^}]*}"
picoCTF{digital_plumb3r_A01Bc3eC}
```
<h3>Flag</h3>
<pre>
picoCTF{digital_plumb3r_A01Bc3eC}
</pre>

