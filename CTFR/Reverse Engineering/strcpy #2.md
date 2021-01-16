<h1><b>strcpy #2</b></h1>
<pre>
Udah selesai pada challenge pertama ? Nah coba lanjut ke challenge ke-2. Kalo yang pertama easy, berarti ke-2 juga easy :D

Download : <a href='https://mega.nz/#!Bxwi3ZrA!CAWqiGKKXVtVyDtrtQrdj9vRgue7nU9HkeRUYQb1HTs'>strcpy2</a>
</pre>
<h3><b>Solution</b></h3>
<p>Buka program dengan Ghidra Tool, dan perhatikan string yang direverse pada program</p>

<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFR/Image/strcpy2.jpg'>
</p>

```python
flag = '}thg1r_ys43_s1_3sr3v3r_ht1w_yp0c_rt5{RFTC'
print(flag[::-1])

```
<h3><b>Flag</b></h3>
<pre>
CTFR{5tr_c0py_w1th_r3v3rs3_1s_34sy_r1ght}
</pre>
