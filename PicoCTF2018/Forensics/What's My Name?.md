<h1><b>What's My Name?</h1></b>
<pre>
Say my name, say <a href="https://2018shell.picoctf.com/static/6ae91abb9e70e527e32729413103af90/myname.pcap">my name</a>.
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file ekstensi pcap</p>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/What's%20My%20Name%3F.png">
</p>
<h3><b>Solution</b></h3>
<p>Sebenarnya cara mendapatkan flagnya itu mudah, hanya dengan perintah <b>strings -a myname.pcap | grep -i picoctf{</b> pada terminal, dan flag didapatkan.</p>
<p>Tetapi disini saya ingin menambah sedikit penjelasan, seperti yang kita lihat pada file tersebut terdapat banyak protokol TCP, tetapi itu sangat menipu kita bahwa flag tidak terdapat pada protokol tersebut. Filter paket data yang protokol DNS pada kolom filter,
 disana terdapat hanya 2 protokol DNS katergori UDP, lihat stream protokol tersebut.</p>
 <b>Klik Protokol --> Follow --> UDP Stream</b>
 <h3><b>Flag</b></h3>
 <pre>
 picoCTF{w4lt3r_wh1t3_033ad0f914a0b9d213bcc3ce5566038b}
 </pre>
