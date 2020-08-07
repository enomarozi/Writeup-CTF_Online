<h1><b>WebNet0</h1></b>
<pre>
We found this packet <a href='https://2019shell1.picoctf.com/static/470e17b168561f9eabdfa95e412dbe10/capture.pcap'>capture</a> and <a href='https://2019shell1.picoctf.com/static/470e17b168561f9eabdfa95e412dbe10/picopico.key'>key</a>. Recover the flag. 
You can also find the file in /problems/webnet0_0_363c0e92cf19b68e5b5c14efb37ed786.
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita buka file pcap dengan wireshark terdapat penyadapan trafik HTTPS yang pastinya ter-encrypt seperti pada setiap protokol TLSv1.2, dan sekarang gunakan key yang diberikan untuk decrypt semua protokol HTTPS</p>
<p>Seperti yang anda ketahui pada info protokol TLSv2.1 disana terdapat key-exchange yang berkemungkinan besar stream HTTPS ter-encrypt dengan kriptografi RSA</p>
<p>Decrypt protokol, <b>Pilih Tab menu Edit --> Preference --> Protocols --> TLS --> Edit</b>, dan insert key seperti pada gambar dibawah lalu OK</p>
<p align="center">
  <img width='500' src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/WebNet0_3.jpg">
</p>
<p>Terakhir, periksa TLS stream <b>Klik 1 protokol TLS --> Follow --> TLS Stream</b>, dan flag terdapat pada stream index 0 seperti pada gambar dibawah<p>
<p align="center">
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/WebNet0_2.jpg">
</p>
<p>Cara sederhana menggunakan tool tshark melalui terminal</p> 
<p>eksekusi <b>tshark -r capture.pcap -o "ssl.keys_list:172.31.22.220,443,http,picopico.key" -qz follow,ssl,ascii,0</b> dan periksa setiap streamnya</p>
<h3><b>Flag</b></h3>
<pre>
picoCTF{nongshim.shrimp.crackers}
</pre>
