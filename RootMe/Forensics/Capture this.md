<h1>Capture this</h1>
<h3>Description</h3>
<label>An employee has lost his Keepass password. He couldn’t remember it, and couldn’t find his password file. After hours of searching, it turns out that he has sent a screen of his passwords to one of his colleagues, but it’s still nowhere to be found.

He’s asking for your help to find him.
It’s up to you

sha256sum: 028c8561f087da873b08968d55141dcfc8f10a47e787f79c35b2da611a5e07ce</label><a href='https://static.root-me.org/forensic/ch42/ch42.zip'>File</a>
<h3>Solution</h3>
<label>Tool acropalypse rekonstruksi screenshoot bagian yang hilang</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls                                                                         
Capture.png  ch42.zip  Database.kdbx
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# acropalypse       
                                                                                                                                
/home/venom/Downloads/Capture.png
True
Found 419252 trailing bytes!
Extracted 419148 bytes of idat!
building bitstream...
reconstructing bit-shifted bytestreams...
Scanning for viable parses...
Found viable parse at bit offset 278910!
Generating output PNG...
Done!

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls                                                                         
Capture.png  ch42.zip  Database.kdbx  restore.png

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# eog restore.png 
```
<label>Password : -=b9w9h^+j%\x-rMPUqv9Vv`@X%*=a</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# keepassxc Database.kdbx
```
<label>Check di Database --> Internet --> Root-me-Real-Flag dan Show Password</label> 

<h3>Flag</h3>
<pre>
@cropalypse_vuln_is_impressive  
</pre>
