<b><h1>LHC</b></h1>
<pre>
The flag is in the middle of <a href="https://lhc-cdn.herokuapp.com/data.txt">this dataset</a> kindly provided to us bythe Large Hadron Collider.
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk mencari flag dari file dataset yang ukurannya 2TB tersebut, disini kita tidak akan mendownload filenya karna akan menguras waktu dan media penyimpanan.
oke sesuai clue pada soal, bahwa flag terdapat ditengah bytes dari file tersebut. pertama kita pastikan dahulu ukuran file dataset sesuai headers content-ranges</p>

```console
root@Python:/home/venom/Downloads# curl -I https://lhc-cdn.herokuapp.com/data.txt -r -1
HTTP/1.1 206 Partial Content
Server: Cowboy
Connection: keep-alive
X-Powered-By: Express
Accept-Ranges: bytes
Content-Type: text/plain; charset=utf-8
Content-Range: bytes 2199999999999-2199999999999/*
Content-Length: 0
Date: Fri, 10 Jul 2020 00:00:24 GMT
Via: 1.1 vegur

root@Python:/home/venom/Downloads#
```
<p>Dan didapatkan yaitu 2199999999999-2199999999999 persis sama 2TB, sekarang akan mencari flag dari setengah ukuran bytesnya<p>
<p><b>(((Content-Range + 1) / 2 ) - len(sha256)/2) to (((Content-Range + 1) / 2 ) + len(sha256)/2)</b></p>
<p><b>(((2199999999999 + 1) / 2 ) - 64/2) to (((2199999999999 + 1) / 2 ) + 64/2)</b></p>
<p><b>1099999999968 to 1100000000032</p></b>

```console
root@Python:/home/venom/Downloads# curl -r 1099999999968-1100000000032 https://lhc-cdn.herokuapp.com/data.txt
 flag is: bf16dc27625b189a2b0f2c52850890fac00189c0b88a2847e36fac
root@Python:/home/venom/Downloads# 
```
<p>Setelah didapatakan ternyata panjangan flag 54, dan itu masih kurang, 64-54 = 10, disini kita akan menambah end rangenya 10 lagi menjadi 1099999999968-1100000000042</p>

```console
root@Python:/home/venom/Downloads# curl -r 1099999999968-1100000000042 https://lhc-cdn.herokuapp.com/data.txt
 flag is: bf16dc27625b189a2b0f2c52850890fac00189c0b88a2847e36facf8071df1b4
root@Python:/home/venom/Downloads#
```
<h3><b>Flag</b></h3>
<pre>
bf16dc27625b189a2b0f2c52850890fac00189c0b88a2847e36facf8071df1b4
</pre>
