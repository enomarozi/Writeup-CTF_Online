<h1><b>LOST</h1></b>
<pre>
Recently, n00b got hands on a flag in hackland, but competition is fierce. 
n00b lost his flag to pro people somewhere in the hackland. 
Help him recover it <a href="http://hack.bckdr.in:17016/">here</a>
</pre>
<h3><b>Solution</b></h3>
<p>Lihat source code (CTRL + U) pada halaman, disana dikatakan terdapat direktori flag.php</p>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/LOST.jpg">
</p>
<p>akses direktori tersebut http://hack.bckdr.in:17016/flag.php maka ditampilkan pesan <b>You really taught that it would be so simple! Awesome! Try more!</b></p>
<p>Tetapi jika diperhatikan lagi dari statment windows console pada source code itu merupakan request POST, dan bukan GET, karena default request ke URL itu adalah 
GET, jadi disini kita mengganti requests ke POST</p>

```python
import requests

URL = 'http://hack.bckdr.in:17016/'
res = requests.post("http://hack.bckdr.in:17016/flag.php").text
print(res)
```
<h3><b>Flag</b></h3>
<pre>
5bea47fd93d6c46bc6108f255de66a556332a6b657972ffaf4da01e6f768cc5e
</pre>
