<h1><b>Browser</h1></b>
<pre>
This one is pretty easy. <a href="http://hack.bckdr.in:11010/">Here</a> is the link of the page where the flag is there. 
This page opens only in a specific browser which is developed by the folks of SDSLabs. 
But unfortunately this browser is only availiable for internal use. 
See if you can find the flag...
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita melakukan request maka akan muncul pesan "Sorry you are not allowed to view this page. Only viewers using the browser developed by SDSLabs are allowed.",
yang artinya browser kita tidak diizinkan oleh server, dan ini terkait dengan user-agent. Kita hanya perlu melakukan requests dengan user-agent=SDSLabs ke URL</p>

```console
root@Python:/home/venom/Downloads# curl -H "User-agent:SDSLabs" http://hack.bckdr.in:11010/

<html>
	<head>
		<title>
		</title>
	<head>
	<body>
		<div>Welcome!! Thanks for using our browser! Here's a flag for you: e77aec24943bb31c63547812d1130c67d0e7e941bf5d85bfef0492cc68050aef</div>
	</body>
</html>
root@Python:/home/venom/Downloads# 
```

<h3><b>Flag</b></h3>
<pre>
e77aec24943bb31c63547812d1130c67d0e7e941bf5d85bfef0492cc68050aef
</pre>
