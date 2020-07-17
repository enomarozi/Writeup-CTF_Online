<h1><b>Ups and Downs</b></h1>
<pre>
Ups and downs are a part of life.They teach you the most important lessons.
Just don't be like mav3rick who faces downs from every girl XD. 
The flag must be wrapped in usual format CTF{flag received}

<a href="http://static.beast.sdslabs.co/static/UpsAndDowns/audio.wav">audio.wav</a>
</pre>
<h3><b>Solution</b></h3>
<p>Buka file audio.wav dengan audacity, maka ditampilkan amplitudo ups dan downs</p>
<p align="center">
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/Ups%20and%20Downs.jpg">
</p>
</p>Kita anggap seluruh ampitudo itu binary, ups = 1, dan downs = 0</p>
<pre>
010000100011000101101110001100100100000100110101011000110011000100110001
</pre>
<p>Panjang seluruh binary yaitu 64, satu ascii character = 8 bit, jadi 72/8=9. Terdapat 9 character string pada seluruh binary</p>

```python
list_amp = "010000100011000101101110001100100100000100110101011000110011000100110001"
result = ''.join([chr(int(list_amp[:i][-8:],2)) for i in range(8,len(list_amp)+8,8)])
print(result)

```
<h3><b>Solution</b></h3>
<pre>
CTF{B1n2A5c11}
</pre>
