<h1>rotation</h1>
<p>You will find the flag after decrypting this file
Download the encrypted flag <a href='https://artifacts.picoctf.net/c/389/encrypted.txt'>here</a>.</h3>
<h3>Description</h3>

```python3
import string

letter_lower = string.ascii_lowercase
letter_upper = string.ascii_uppercase

flag_enc = "xqkwKBN{z0bib1wv_l3kzgxb3l_i4j7l759}"
for i in flag_enc:
    if i.islower():
        print(letter_lower[(letter_lower.index(i)+18)%26],end='')
    elif i.isupper():
        print(letter_upper[(letter_upper.index(i)+18)%26],end='')
    else:
        print(i,end='')
```

<h3>Flag</h3>
<pre>picoCTF{r0tat1on_d3crypt3d_a4b7d759}</pre>
