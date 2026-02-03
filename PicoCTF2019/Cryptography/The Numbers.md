<h1><b>The Numbers</h1></b>
<pre>
The <a href='https://2019shell1.picoctf.com/static/eb3589c566dd3f809908053460acb817/the_numbers.png'>numbers</a>... what do they mean?
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan gambar kumpulan angka</p>
<pre>
16,9,3,15,3,20,6,{,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,}
</pre>

```python
from string import ascii_lowercase

letter = ascii_lowercase

values = '16,9,3,15,3,20,6,{,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,}'.split(",")
for i in values:
    if i == "{" or i == "}":
        print(i,end='')
    else:
        print(letter[int(i)-1],end='')
        
```
        
</b><h3>Flag</h3></b>
<pre>
PicoCTF{thenumbersmason}
</pre>
