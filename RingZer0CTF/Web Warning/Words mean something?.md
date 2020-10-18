<h1><b>Words mean something?</h1></b>
<pre>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam commodo
risus lobortis diam molestie, varius vestibulum lacus condimentum. Phasellus
fringilla, leo at ornare tristique, est elit lobortis dolor, a placerat tortor eros nec
elit. Suspendisse feugiat, enim ac hendrerit malesuada, libero lectus rutrum
tellus, ut faucibus sem odio non nunc. Vestibulum dignissim magna et felis
laoreet viverra. Integer sodales tellus molestie suscipit feugiat. Praesent quis
elit tristique nisl laoreet elementum eu nec felis. Fusce nunc enim, rhoncus at
metus sed, accumsan accumsan augue. Nunc venenatis tempor mi sit amet
tempus. Maecenas luctus lacus mi, id pretium magna feugiat eu. Aenean
euismod ante at neque rhoncus, eget dapibus nisi lacinia. Aenean vulputate
risus id velit interdum vulputate. Mauris id rhoncus dolor.
</pre>
</b><h3>Solution</h3></b>
<p align='justify'>Jujur saja saya tak tau apa maksud kata2 diatas, tapi setelah saya periksa ada sesuai yg mencurigakan di cookie yaitu valuenya = 0, ganti value cookie = 1. 
dan kemungkinan script php-nya seperti dibawah ini</p>

```php
<?php
$cookie_name = "flag";
$cookie_value = 0;
setcookie($cookie_name,$cookie_value,time()+86400,'/');

if(isset($_COOKIE[$cookie_name]))
{
	if($_COOKIE[$cookie_name]==1)
	{
		echo "Flag:xxxxxxxxxxxxxxxxxxxxxx";
	}
	else
	{
		echo "Lorem ipsum dolor sit amet......";
	}
}
?>
```
</b><h3>Flag</h3></b>
<pre>
FLAG-AnlAb6QxDpQvg1yn2bAhyOJw
</pre>
