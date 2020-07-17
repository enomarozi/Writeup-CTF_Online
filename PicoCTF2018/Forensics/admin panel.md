<h1><b>admin panel</h1></b>
<pre>
We captured some <a href="https://2018shell.picoctf.com/static/1a6db339e11fa100ef52d944edaa9612/data.pcap">traffic</a> logging into the admin panel, can you find the password?
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file ekstensi pcap</p>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/admin%20panel.png">
</p>
<h3><b>Solution</b></h3>
<p>Sebenarnya cara mendapatkan admin password/flag itu mudah, hanya dengan perintah <b>strings -a data.pcap | grep -i picoctf{</b> pada terminal, dan flag didapatkan.</p>
<a align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/admin%20panel1.png">
</a>
<p>Tetapi disini saya ingin menambah sedikit analisa untuk mendapatkannya yaitu, seperti yang kita ketahui pada file pcap hanya terdapat TCP protokol, lihat stream protocol dari TCP dan HTTP</p>
<p><b>Select Protocol --> Follow --> TCP Stream</b>, disana terdapat 2 kali proses authetifikasi, tetapi authetifikasi pertama status admin=false, dan lihat pada stream ke-5, disana terdapat password admin yang berupa flag</p>
<h3><b>Flag</b></h3>
<pre>
picoCTF{n0ts3cur3_b186631d}
</pre>
