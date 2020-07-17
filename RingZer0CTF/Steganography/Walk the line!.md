<h1><b>Walk the line!</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/81fa082ee694318d0d29b7039377c4a4.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi perintah strings pada file image maka didapatkan PGP Private key, dan juga dibawahnya raw bytes dari file zip. ekstrak file dengan foremost dan ekstrak file zip yang 
didapatkan maka akan ada sebuah file flag yang terencrypt dengan PGP private key</p>

```console
root@Python:/home/venom/Downloads# ls
root@Python:/home/venom/Downloads# unzip 81fa082ee694318d0d29b7039377c4a4.zip 
Archive:  81fa082ee694318d0d29b7039377c4a4.zip
  inflating: f0ddce75e8d0bad94273d9595a8210fd.jpg  
root@Python:/home/venom/Downloads# strings -a f0ddce75e8d0bad94273d9595a8210fd.jpg | tail -n 42 | head -n 34
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v2.0.14 (GNU/Linux)
lQH+BFMJmU0BBAC7J3IMTZRiWsK9KlFC/UXQ1p5XerK2z2u3UqoZuHJfEKY81HNK
[+]..........................................................[+]
Y4Nb6ts5capH8OEp6MOPxssIiNa3W6dIqucWSVVnCm2PAU+q2Q22PFe/+wZyRNtS
vkwFlWNWJ2oR7DdF
=vDAR
-----END PGP PRIVATE KEY BLOCK-----
root@Python:/home/venom/Downloads# 

root@Python:/home/venom/Downloads# foremost 
81fa082ee694318d0d29b7039377c4a4.zip  Private_key.pem
f0ddce75e8d0bad94273d9595a8210fd.jpg  
root@Python:/home/venom/Downloads# foremost f0ddce75e8d0bad94273d9595a8210fd.jpg 
Processing: f0ddce75e8d0bad94273d9595a8210fd.jpg
|foundat=flag.txt.gpgUT	
*|
root@Python:/home/venom/Downloads# cd output/zip/
root@Python:/home/venom/Downloads/output/zip# ls
00003542.zip
root@Python:/home/venom/Downloads/output/zip# unzip 00003542.zip 
Archive:  00003542.zip
 extracting: flag.txt.gpg            
root@Python:/home/venom/Downloads/output/zip# cat flag.txt.gpg 
���l���v>�X��'����	�)����1Ќb�N��p�+|	��f�_E�4���Ŀ
#�%ZqNP�b��D�sV"6����D;��]���)��u|�̞D�9��V8�YT����%�s���4� �V����c	��B�T�Ġ�?�#\�;ᩕ^�"�3���Uz����A
root@Python:/home/venom/Downloads/output/zip# �D
```
<p>PGP Private-key</p>
<pre>
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v2.0.14 (GNU/Linux)</br>

lQH+BFMJmU0BBAC7J3IMTZRiWsK9KlFC/UXQ1p5XerK2z2u3UqoZuHJfEKY81HNK
6kd6Ar134Mc80ItJl0JGdCgt56zNO68PHvLpLMTm3N6vjUUhEW4sJYbRQqk8AD5c
HKT5Hfb+WGGzPC4ZYqqmS39YNmx829Y58mDCKQX1uWAHh60Y1vUclZUp9wARAQAB
/gIDAhOLmBU0A0WY0PNdHjFHSA8M2efZJa2m/J0wIuBOQh2F1GFn3clu88fgh/uv
MwHNErzdP81oPZydnfntDUSX06l69jlc2JeLPbF5r8ndvyAmMzK9dWecB/wymjTy
DwyvQbevHAfwak30Ih3xmk6WzsTyLh9oUrAR9D6c9uDM+ce4H6Rpaz749cMiHHqC
jJh0qhDSPfSrps+gWUVbewVH0nl6JO1eUZCyEYv+GzbrwMvvzB6DKmPddWC/RUhM
rPArGLDNA7nuiErNfKPH5WxplFNgL/w8wN2JEX5WcseO3ky5RuyKNVcneDd1Ix+D
zCfXQM278P/1094/AllOEYRlyrzP/Mze6uu+5PcNEWmZbkOosFlIdL9fOiKn1kWC
9F8QGMBP5zw0VUXQXbhyJMf7QJDOHUyQWgODhvk+AI1T22sIzRowLAlxjqP45kkk
qANODqTHM4TPUpzUNsXZUn62n7jeOSXNlkBAgLM6hKAStB1zdGVldmUgKHN0ZWV2
ZSkgPHN0ZWV2ZUB0ZXN0Poi4BBMBAgAiBQJTCZlNAhsDBgsJCAcDAgYVCAIJCgsE
FgIDAQIeAQIXgAAKCRCqYfmAxT1btofZA/9gulteMQ5X2dre41sxrsMqm4Js6HPx
CwxpX99VjilkHAKCXJSnqU7JqWoFzPpyrTBtS29VoXXuFOpzL8BxYnzDoP+Q3Ybl
kq86zt4E+ryTtiaxgbSKT+BVAIp8AaIuAIWIS7pIzyacMDnEWui8GwgxBhPN/3Tu
Oi7oRetOVpDRcp0B/gRTCZlNAQQA7wnoBWSrppeWx5q0cC3G47eaXM32weHX1Kqy
Lw/Q+plHSThniy6kNEoiNBTd3pT8mIMCzz613EUwHbd2dDXf5zC8gds4Iveop+44
MgKInG8io2KYtXQOaRN5ivcD6ccjsp0t/5i7FjSH6XU14KzENJW0CQBPAgdoLmW/
+OTKVBcAEQEAAf4CAwITi5gVNANFmNBcvRhALhfr9KSDntvXJ0y3X8nAoCyInWW2
cmGgD2FTttpqskxKFpH7a0y0JtqMCMye3/EYtlEUFbASL1zHMNh2KAIRZeXmcsdt
a8me78xc3wNjyC0J4xHFqs3UBt9XhqxmaubjisEz2J6apqfMVS+TrP5dTF9N46Sl
LTBSXhwOKMlR+1HILiSBuNHuDPR757+jT/aUzSSqYSdUSipsHx6k8FCKhfBhnpJq
k6dNNjweYJWaV9n9ZHLSpsZBwJj9STy0lXvTURK9EjPJrwIJbN+BDl2ipftWsEbm
D8OjjOHWY7YjDwe/X9U46W5Z2sfgMS0NBR+uS+v8MA+ww3Ez+ND3vwT+MAGMU55a
F7G9URgZQiBOgrr1OX8657t0N9KynkSKPUXVgrU0V93UAWdE/hplxy3Im1zeU0fL
ntwC/Pa6lVJk11Rizs/laJIerhjpGwn1I6J6bt+B2m4aRDVUAkSUJTKnq4ifBBgB
AgAJBQJTCZlNAhsMAAoJEKph+YDFPVu2M9oEALT4GOGNKlVV5j+JzGhG+OP1ojru
CVe7InSEtVUdQKeN4w/1myoz0SbAm+jGIFz4TFoZ+rP2d8DcBtqGFiwXzL9MaDnT
Y4Nb6ts5capH8OEp6MOPxssIiNa3W6dIqucWSVVnCm2PAU+q2Q22PFe/+wZyRNtS
vkwFlWNWJ2oR7DdF
=vDAR
-----END PGP PRIVATE KEY BLOCK-----
</pre>
<p>Jika kita decrypt file flag.txt.gpg dengan private-key, maka kita diminta untuk input passpharse-nya, tetapi disini kita tidak mengetahui passpharse.</p>

```console
root@Python:/home/venom/Downloads# gpg --import key.gpg 
gpg: key AA61F980C53D5BB6: "steeve (steeve) <steeve@test>" not changed
gpg: key AA61F980C53D5BB6: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
root@Python:/home/venom/Downloads# gpg -d output/zip/flag.txt.gpg 
gpg: encrypted with 1024-bit RSA key, ID EC6C8BA88B76173E, created 2014-02-23
      "steeve (steeve) <steeve@test>"
gpg: public key decryption failed: Bad passphrase
gpg: decryption failed: No secret key
root@Python:/home/venom/Downloads# 
```
<p>Maka solusinya crack passpharse dengan tool john</p>

```console
root@Python:/home/venom/Downloads# gpg2john key.gpg > crack_pgp.john 

File key.gpg
root@Python:/home/venom/Downloads# john crack_pgp.john --show
steeve:1234:::steeve (steeve) <steeve@test>::key.gpg

1 password hash cracked, 0 left
root@Python:/home/venom/Downloads# 
```
<p>Didapatkan password yaitu 1234, decrypt flag.txt.gpg dengan privatekey dan passpharse tersebut</p>

```console
root@Python:/home/venom/Downloads# gpg --import key.gpg 
gpg: key AA61F980C53D5BB6: "steeve (steeve) <steeve@test>" not changed
gpg: key AA61F980C53D5BB6: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
root@Python:/home/venom/Downloads# gpg -d output/zip/flag.txt.gpg 
gpg: encrypted with 1024-bit RSA key, ID EC6C8BA88B76173E, created 2014-02-23
      "steeve (steeve) <steeve@test>"
FLAG-f9f$9{!-_4F"+
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG-f9f$9{!-_4F"+
</pre>
