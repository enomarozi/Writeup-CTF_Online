<h1>strings it</h1>
<h3>Description</h3>
<pre>
Can you find the flag in <a href='https://challenge-files.picoctf.net/c_fickle_tempest/6577d3f1500aebcd300787bd5d96216b30aed379c811f5e83e888f897da4a3d5/strings'>file</a> without running it?
</pre>
<h3>Solution</h3>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls
strings
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file strings 
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ac2be8917250478c4e3cdd8b41a945cfdd4a755f, for GNU/Linux 3.2.0, not stripped
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# chmod +x strings   
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ./strings  
Maybe try the 'strings' function? Take a look at the man page
                                                                                                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# strings strings| grep -io 'picoCTF{[^}]*}'
picoCTF{5tRIng5_1T_d6306c19}
```
<h3>Flag</h3>
<pre>
picoCTF{5tRIng5_1T_d6306c19}
</pre>


