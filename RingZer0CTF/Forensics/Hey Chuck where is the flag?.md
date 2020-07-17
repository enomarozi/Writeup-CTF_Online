<h1><b>Hey Chuck where is the flag?</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/a26a10853f9d170feba6ab9b627ad156.zip">File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan 1 file ekstensi pcap, lakukan analisa untuk mendapatkan flag</p>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/Hey%20Chuck%20where%20is%20the%20flag%3F.png">
</p>
<p>Dari jumlah paket yang tercapture, rata-rata itu adalah protocol HTTP. Bisa dilihat ditab info, bahwa protocol HTTP tersebut ada yang berupa file image atau data yang bisa dilihat <b>Klik kanan paket --> Follow --> TCP Stream</b>. Export semua paket data tersebut dalam bentuk file aslinya.</p>
<p><b>Tab File --> Export Objects --> HTTP --> Save All</b></p>
<p>Akan ada banyak file disana, dan untuk flagnya eksekusi <b>grep -iR flag</b> pada terminal, maka akan muncul flag dari file askldj3lkj234.php</p>
<h3><b>Flag</b></h3>
<pre>
FLAG-GehFMsqCeNvof5szVpB2Dmjx
</pre>
