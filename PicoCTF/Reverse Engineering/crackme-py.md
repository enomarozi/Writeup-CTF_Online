<h1>crackme-py</h1>
<p><a href='https://mercury.picoctf.net/static/b7cabaae6561256c50728d3515db3058/crackme.py'>crackme.py</a></p>
<h3>Solution</h3>
<p>Rombak program untuk bruteforce flag</p>

```python3
enc = 'A:4@r%uL`M-^M0c0AbcM-MFE07b34c`_6N'
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
for j in range(len(enc)):
    for i in alphabet:
        index = alphabet.find(i)
        ori = (index+47)%len(alphabet)
        if alphabet[ori] == enc[j]:
            print(i,end='')
```
<h3>Flag</h3>
<p>picoCTF{1|\/|_4_p34|\|ut_f3bc410e}</p>
