<h1><b>My Head Hurts</b></h1>
<pre>
My head has been aching since I received this file from SC4R. 
What has he done this time?

<a href="http://static.beast.sdslabs.co/static/My%20Head%20Hurts/dont2">dont2</a>
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita periksa seluruh raw bytes file dengan tool bless, disana terdapat beberapa chunk dari file image PNG yaitu Header PNG, Footer IEND, chuck IHDR, dan chuck IDAT</p>
<p>Hapus header PDF pada file yaitu 25 50 44 46 2D 31 2E 33 2E 25 FF D8 FF menjadi null</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/My%20Head%20Hurts2.jpg">
</p>
<p>Hasil</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/My%20Head%20Hurts1.jpg">
</p>
<p>Simpan raw bytes data dengan format PNG, dan hasilnya</p>
<p align='center'>
<img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/My%20Head%20Hurts.png">
</p>
<h3><b>Flag</b></h3>
<pre>
flag{d0nt_tru5t_4ny0n3_n0t_3v3n_y0urs3lv3s}
</pre>
