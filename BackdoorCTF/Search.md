<h1><b>Search</h1></b>
<pre>
A particular file came across our team of hackers. 
Some say the it gives the location of a flag. Download the file <a href="http://static.beast.sdslabs.co/static/SEARCH/search.zip">here</a>.
</pre>
<p>Analisa file yang diberikan, dan disana terdapat header JFIF yang merupakan header dari file image jpg. beri format pada file menjadi search.jpg lalu tampilkan, maka didapatkan image QR-code</p>

```console
root@Python:/home/venom/Downloads# mv search search.jpg
root@Python:/home/venom/Downloads# eog search.jpg 
```
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/search.jpg">
</p>
<p>Decode image QR-code tersebut</p>

```python
from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open('search.jpg'))
print(data)
```
<p>Hasil decode didapatkan URL <b>https://dhavalkapil.com/assets/files/flag.txt</b>, akses URL tersebut maka didapatkanlah flagnya</p>
<h3><b>Flag</b></h3>
<pre>
05b51fa36f665e94780fdf7225aaffaec503ed2dbc88d742078cdaab245b536e
</pre>
