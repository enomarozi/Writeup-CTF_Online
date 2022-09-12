<h1>Mod 26</h1>
<p>Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}</p>
<p>Hint :</p>
<ul><li>This can be solved online if you don't want to do it by hand!</li></ul>
<h3>Solution</h3>
<p>Lakukan decrypt ROT13 pada pesan</p>

```python3
import string

flag_enc = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
for i in flag_enc:
    if i.islower():
        data = (ord(i)+13-97)%26
        print(string.ascii_lowercase[data],end='')
    elif i.isupper():
        data = (ord(i)+13-65)%26
        print(string.ascii_uppercase[data],end='')
    else:
        print(i,end='')
```

<h3>Flag</h3>
<p>picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}</p>
