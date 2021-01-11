<h1><b>Keyboard</b></h1>
<pre>
Keyboard merupakan Hardware yang membantu kita dalam menulis pada komputer. Tapi ketahuilah, dengan Keyboard kita sendiri dapat membuat enkripsi yang unik. Contohnya seperti "Ayam" akan menjadi "Sus,". Nah sampe sini sudah paham kan ? Coba Decode Flag dibawah ini dengan Trik yang sama seperti contoh diatas

Flag : VYGT}l4un-5tf+dj2gy+2d+e42tfQ
</pre>
<h3><b>Solution</b></h3>
<p>Bukan jenis kriptografi, perhatikan keyboard. Berikut script pythonnya</p>

```python
keyboard_list = [['` 1 2 3 4 5 6 7 8 9 0 - _ +'.split(' ')],
                 ['q w e r t y u i o p { }'.split(' ')],
                 ['a s d f g h j k l : " '.split(' ')],
                 ['z x c v b n m , . /'.split(' ')]]

encode_flag = "VYGT}l4un-5tf+dj2gy+2d+e42tfQ"
for part in encode_flag:
    for i in keyboard_list:
        for j in i:
            for k in j:
                part = part.lower()
                if part == k:
                    print(j[j.index(k)-1],end='')
         
```
<h3><b>Flag</b></h3>
<pre>
CTFR{k3yb04rd_sh1ft_1s_w31rd}
</pre>
