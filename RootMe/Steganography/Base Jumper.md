<h1>Base Jumper</h1>
<h3>Description</h3>
<label>It seems steganography is all the rage with attackers exfiltrating data these days.
Look at this example I found, I think it has a flag inside.</label>
<h3>Solution</h3>
<label>Merupakan steganography Paddinganograph</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# ls
 ch15.jpg

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# paddinganograph -e base64 -f Comment -s . < ch15.jpg | paddinganograph -e base32
/usr/local/lib/python3.13/dist-packages/codext/__common__.py:9: DeprecationWarning: module 'sre_parse' is deprecated
  import sre_parse
3v3ry0ne_h4s_s3cr3ts!
```
<h3>Flag</h3>
<pre>
3v3ry0ne_h4s_s3cr3ts!
</pre>
