<h1>vault-door-5</h1>
<h3>Description</h3>
<pre>In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/d31ce4356bdfd15d33a9af7e35ab4d0a/VaultDoor5.java'>VaultDoor5.java</a></pre>
<h3>Solution</h3>
<p>Cek Source code</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "JTcwJTY5JTYzJTZmJTQzJTU0JTQ2JTdiJTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0JTdk" | base64 -d | sed 's/%//g' | xxd -r -p                   
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}                                                                                                                                      
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "JTcwJTY5JTYzJTZmJTQzJTU0JTQ2JTdiJTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0JTdk" | base64 -d | sed 's/%//g' | xxd -r -p | java VaultDoor5 
Enter vault password: Access granted.
```
<h3>Flag</h3>
<pre>
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}      
</pre>
