<h1><b>Up For A Little Challenge?</h1></b>
<pre>
https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0

You Know What To Do ...
</pre>
</b><h3>Solution</h3></b>
<p>Pada file pertama terdapat password, key-unlick, link Meganz dan fake flag</p>

```console
root@Python:/home/venom/Downloads# strings -a Begin\ Hack.jpg | grep -i http
`- https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg -N17hGnFBfJliykJxXu8 -
root@Python:/home/venom/Downloads# strings -a Begin\ Hack.jpg | grep -i key
Mp real_unlock_key: Nothing Is As It SeemsU
root@Python:/home/venom/Downloads# strings -a Begin\ Hack.jpg | grep -i flag
flag{Not_So_Simple...}
root@Python:/home/venom/Downloads# 
```

<p>Download file pada link yg didapatkan, Ekstrak kemudian disana terdapat file ZIP berpassword, ektrak file ZIP dengan password <b>Nothing Is As It Seems</b></p>

```console
root@Python:/home/venom/Downloads# unzip Up\ For\ A\ Little\ Challenge.zip 
Archive:  Up For A Little Challenge.zip
  inflating: Did I Forget Again?/.Processing.cerb4  
  inflating: __MACOSX/Did I Forget Again?/._.Processing.cerb4  
  inflating: Did I Forget Again?/Loo Nothing Becomes Useless ack.jpg  
  inflating: __MACOSX/Did I Forget Again?/._Loo Nothing Becomes Useless ack.jpg  
  inflating: __MACOSX/._Did I Forget Again?  
root@Python:/home/venom/Downloads# cd Did\ I\ Forget\ Again\?/output/zip
root@Python:/home/venom/Downloads/Did I Forget Again?/output/zip# unzip 00000000.zip 
Archive:  00000000.zip
[00000000.zip] skycoder.jpg password: Nothing Is As It Seems
  inflating: skycoder.jpg            
root@Python:/home/venom/Downloads/Did I Forget Again?/output/zip# eog skycoder.jpg 
```

<p>Dan Hasilnya</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/skycoder.jpg'>
</p>
<p>Flag terdapat pada sudut kiri bawah gambar</p>
</b><h3>Flag</h3></b>
<pre>
flag{hack_complete}
</pre>
