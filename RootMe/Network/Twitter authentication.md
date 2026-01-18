<h1>Twitter authentication</h1>
<h3>Description</h3>
<label>A twitter authentication session has been captured, you have to retrieve the password.</label><a href='https://static.root-me.org/reseau/ch3/ch3.pcap'>File</a>
<h3>Solution</h3>
<label>Follow HTTP Stream pada packet, cek Basic Authorization</label>

```console
┌──(root㉿Kali)-[/home/venom]
└─# echo "dXNlcnRlc3Q6cGFzc3dvcmQ=" | base64 -d
usertest:password
```
<h3>Flag</h3>
<pre>
password
</pre>
