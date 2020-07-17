<h1><b>CLUTTER</b></h1>
<pre>
n00b after failing in all attempts, fixed his eyes on pro Divij. 
n00b tapped all the lines of pro's home to get this <a href="http://static.beast.sdslabs.co/static/CLUTTER/clutter.pcap.gz">file</a> in result. 
Help him find the flag. Submit SHA-256 of the flag obtained.
</pre>
<h3><b>Solution</b></h3>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/CLUTTER.jpg">
</p>
<p>Sesuai yang ditampilkan wireshark disana ada banyak packet capture, dan sebagian capture meupakan protokol HTTP, Eksport seluruh protokol HTTP</p>
<b><p>Tab File --> Export Objects --> HTTP --> Save as --> Select Directori --> OK</b></p>
<p>Dikarenakan banyaknya file yang dicapture oleh protokol HTTP, maka untuk mencari flag eksekusi perintah grep</p>

```console
root@Python:/home/venom/Downloads/source# grep -iR flag
game_cf(18).asp:<P>If the flag is successfully captured, it must be carried across the line 
game_cf(18).asp:flag is set up again at the point where it was rescued and the game as 
game_cf(18).asp:before.  If niether side captures the enemy's flag within the time agreed up
game_cf(18).asp:<DT><H4>Hidden Flag</H4>
game_cf(18).asp:<DD>Allow each team to hide their flag out of sight.  Before starting the game
game_cf(18).asp:allow a scout from each team to be shown where the flag is.  He must describe
game_cf(18).asp:accurately, to his team, where the flag is.  This requires that the scout be
akfq4mjb:		<title>flag: pcap_is_the_real_fun_always - Pastebin.com</title>
Capture_the_flag:<title>Capture the flag - Wikipedia, the free encyclopedia</title>
```
<p>Dan disana terdapat flag pada file akfq4mjb</p>
<h3><b>Solution</b></h3>
<pre>
pcap_is_the_real_fun_always
</pre>
