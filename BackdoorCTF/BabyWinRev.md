<h1><b>BabyWinRev</b></h1>
<pre>
SC4R used windows for a long time but after shifting to linux started reprimanding his ignorant past. 
I made this challenge to annoy him :p

<a href="http://static.beast.sdslabs.co/static/BabyWinRev/chall.exe">chall.exe</a>
</pre>
<h3><b>Solution</b></h3>
<p>Decompile program dengan ghidra tool, lihat pada fungsu main() program, disana terdapat statment mengembalikan nilai True jika string bernilai sama</p>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/BabyWinRev.jpg">
</p>
<p>Ambil seluruh string pada statment, maka menjadi <b>w1nd0w5_15_b4d</b></p>
<h3><b>Flag</b></h3>
<pre>
flag{w1nd0w5_15_b4d}
</pre>
