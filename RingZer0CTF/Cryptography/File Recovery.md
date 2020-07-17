<h1><b>File Recovery</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/e2c9757d48bd69a357a78223dd4a2bd1.zip">File</a>
</pre>
<h3><b>Solution</b></h3>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/RSA/Image/File-Recovery.png">
</p>
<p>Diberikan 2 file (flag.enc dan private.pem)</p>
<p>Sebenarnya men-decrypt file flag.enc untuk memperoleh flag itu simpel, karena kita sudah memiliki file private.pem atau privatekey(d) 
<b>openssl rsautl -decrypt -inkey private.pem -in flag.enc</b>, dan Hasil :</p>
<pre>
FLAG-vOAM5ZcReMNzJqOfxLauakHx
</pre>
<p>Tetapi seperti ini prosesnya, pertama generate modulus(n), eksponen(e), prima-pertama(p), prima-kedua(q), dan privatekey(d) dari file private.pem
<b>openssl rsa -in private.pem -text -noout</b>,dan Hasil :</p>
<pre>
RSA Private-Key: (1024 bit, 2 primes)
modulus:
    00:c5:0f:1a:cb:cf:f9:41:69:ba:3f:26:b4:6f:28:
    de:3b:21:1c:d4:82:6f:cb:cc:6f:73:6e:7d:e0:f0:
    73:27:3c:8a:72:e1:93:85:7e:18:db:96:f6:fc:88:
    d7:85:31:b5:08:0c:04:f6:42:6b:2a:0d:12:61:1c:
    7e:f1:51:57:c2:e8:38:98:07:76:2e:28:90:bf:44:
    12:07:ce:a9:41:b3:15:97:23:90:c5:8a:4c:92:df:
    24:fa:4e:14:1a:a7:72:59:10:a1:3b:7d:55:c7:1c:
    99:9e:6b:85:6b:b1:15:61:58:6e:b3:b6:83:d8:7f:
    e3:9f:88:cc:b3:8f:42:15:dd
publicExponent: 65537 (0x10001)
privateExponent:
    5f:54:27:4a:61:99:db:23:22:8e:5a:52:ff:53:6d:
    ee:7c:de:4d:8f:ac:35:92:f8:77:87:04:2e:45:23:
    ef:df:41:ba:c1:95:74:06:c4:4f:b6:80:55:3a:7d:
    c8:59:7b:92:20:fe:65:83:4c:04:53:be:88:6c:18:
    9c:f5:14:d6:c3:d2:94:57:12:d5:83:6e:d9:2f:b8:
    76:cd:b2:9b:55:5f:66:ed:9d:ad:33:79:a9:42:06:
    22:6d:b6:da:68:32:38:6d:42:4b:1e:36:d4:db:38:
    5f:9a:88:7b:19:10:d6:03:a7:a9:a0:6e:0f:b3:22:
    dc:3d:7d:73:99:8a:eb:a1
prime1:
    00:e5:b7:df:49:73:0e:c9:87:51:9d:4c:cc:bc:71:
    0e:c4:04:8f:36:60:f7:9d:44:fe:52:9c:0b:f4:fe:
    c0:88:81:cb:01:99:b0:01:3b:a5:b0:09:e4:b5:05:
    58:e8:89:c7:fe:a4:f9:88:cb:76:24:ca:2c:8e:f0:
    92:1a:f4:62:4b
prime2:
    00:db:9a:b0:44:40:a5:9e:6f:b6:a8:80:51:2d:a9:
    7e:a4:6f:2d:ef:16:65:13:26:be:1e:b9:57:de:88:
    13:85:ff:fd:1b:26:df:22:6c:ca:65:06:a0:6e:89:
    b7:b0:39:91:4d:eb:ba:3e:10:e1:bb:85:d9:4b:b0:
    f8:81:f2:0f:77
exponent1:
    36:50:eb:b2:ea:49:ac:cd:1a:37:1f:59:a9:94:f1:
    f0:d7:43:25:90:77:fb:ef:bc:52:bc:22:f7:a2:e4:
    d3:62:1d:26:1b:b8:ca:11:d8:73:6f:63:6c:89:ff:
    23:bc:b0:55:3d:9c:e3:03:78:c3:ea:29:ef:02:63:
    09:8c:8f:51
exponent2:
    69:51:28:53:b3:45:3a:54:8d:1f:06:5a:e8:31:2f:
    41:20:e8:c0:8e:d6:ee:76:58:1b:57:fb:e2:07:14:
    85:e1:1c:bb:96:ca:d0:31:a8:67:06:e4:8d:de:92:
    2f:7b:8c:49:f8:51:1b:4e:f1:53:03:80:10:a2:d0:
    ab:51:31:45
coefficient:
    00:9a:2e:72:2e:c2:54:86:dd:f1:7a:99:10:16:81:
    02:a2:04:54:a0:9f:7f:ea:87:b0:7c:e8:66:8d:6b:
    ca:88:3c:bc:88:1e:bc:8f:5e:ff:4d:42:ab:2b:8a:
    21:1b:3d:5a:63:3e:0d:4f:d0:9d:9b:4b:24:75:2a:
    82:4a:52:09:a8
</pre>
<p>Selanjutnya, conversi modulus(n), eksponen(e), prima1(p), prima2(q), dan privatekey(d) dari bilangan hexa ke desimal, dan Hasil :</p>
<pre>
e = 65537
n = 138379537572187417525716958096344297737306941144440456301092881426923212359225017408288486394734469524503142706623004324938825138645138494101986501393785250273860698734376241414268739623082355863756016350214564747738782067433575251990907004547254119017930289613838337896185925267946859766711246354643570267613
q = 11501607941238992181742812061114672253608335214188481893279882779140606954597060408821323601607624893702027758802695445840832180665615874601418269771566967
p = 12031321036081212904391045175033473831054562898264724728651997476360140537721183216703878216582942480438791132082440974521045395707418796095365296063537739
d = 66942106889064648751626263629499360902445630133258162970075662797491089379081586766443050073373233773362339386465290280572203674193287315821740086366305549973213593782365416589257462291062751455696766485355445306223640482021080814372397455195808484910759298432870196107475279944585591518571396060262882274209
</pre>
<p>Dan juga, conversi pesan flag.enc ke desimal, Hasil</p>
<pre>
c = 104156723444975389550665011116917104373786239275693203375523427101278757224015423940709531632140351017602350094963564897604016008122353027729555931175458064409870780132116927959159055170043399560533757159771565093746792035157155025417337106668043958886088210250918386082867139783000900058648375395393716199340
</pre>
<p>Terakhir, lakukan decrypt dari ciphertext(c) ke plaintext

```python
e = 65537
n = 138379537572187417525716958096344297737306941144440456301092881426923212359225017408288486394734469524503142706623004324938825138645138494101986501393785250273860698734376241414268739623082355863756016350214564747738782067433575251990907004547254119017930289613838337896185925267946859766711246354643570267613
q = 11501607941238992181742812061114672253608335214188481893279882779140606954597060408821323601607624893702027758802695445840832180665615874601418269771566967
p = 12031321036081212904391045175033473831054562898264724728651997476360140537721183216703878216582942480438791132082440974521045395707418796095365296063537739
c = 104156723444975389550665011116917104373786239275693203375523427101278757224015423940709531632140351017602350094963564897604016008122353027729555931175458064409870780132116927959159055170043399560533757159771565093746792035157155025417337106668043958886088210250918386082867139783000900058648375395393716199340
d = 66942106889064648751626263629499360902445630133258162970075662797491089379081586766443050073373233773362339386465290280572203674193287315821740086366305549973213593782365416589257462291062751455696766485355445306223640482021080814372397455195808484910759298432870196107475279944585591518571396060262882274209
print(bytes.fromhex(hex(pow(c,d,n)).split("00")[1]))
```
<h3><b>Flag</b></h3>
<pre>
FLAG-vOAM5ZcReMNzJqOfxLauakHx
</pre>