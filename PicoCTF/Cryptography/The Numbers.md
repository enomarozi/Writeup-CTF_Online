<h1>The Numbers</h1>
<p>The <a href='https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png'>numbers</a>... what do they mean?</p>
<p>Hint :</p>
<ul><li>The flag is in the format PICOCTF{}</li></ul>
<h3>Solution</h3>
<p>(Angka-1) = index dari string</p>

```python3
from string import ascii_lowercase as letter

idx_ = "16,9,3,15,3,20,6,{,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,}".split(',')
for i in idx_:
    if i in ['{','}']:
        print(i,end='')
    elif letter[int(i)-1] in letter:
        print(letter[int(i)-1],end='')
   
```

<h3>Solution</h3>
<p>picoctf{thenumbersmason}</p> 
