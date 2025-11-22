<h1>Look inside the house</h1>
<pre>
<a href="https://ringzer0ctf.com/files/15fa3a948a1aed3802fe40c206b6df40.zip">File</a>
</pre>
<h3>Solution</h3>
<p>File jpg identik dengan steganography file flag.txt dengan steghide tanpa password</p>

```console
root@Python:/home/venom/Downloads# steghide extract -sf 3e634b3b5d0658c903fc8d42b033fa57.jpg 
Enter passphrase: 
wrote extracted data to "flag.txt".
root@Python:/home/venom/Downloads# ls
15fa3a948a1aed3802fe40c206b6df40.zip  3e634b3b5d0658c903fc8d42b033fa57.jpg  flag.txt
root@Python:/home/venom/Downloads# cat flag.txt 
FLAG-5jk682aqoepoi582r940oow
root@Python:/home/venom/Downloads# 
```
<h3>Flag</h3>
<pre>
FLAG-5jk682aqoepoi582r940oow
</pre>
