<h1><b>MATRIX</b></h1>

<pre>
n00b was captured by the enemy. Forced to reveal the flag, he disclosed this string:
<a href="http://static.beast.sdslabs.co/static/MATRIX/matrix.txt">Here</a> is the string
Can you find the flag?
</pre>

<h3><b>Solution</h3></b>
<p>Pada soal kita dipaksa menemukan flag pada string hexa yang akan diolah terlebih dahulu dalam bentuk matrix, yang awalnya saya mengira ini merupakan hill cipher karena 
challengenya kategori crypto ,dan itu ternyata salah besar
<pre>
83ad8cgf228bfgc7adf1g4a588eg265a87gcc165dg64ad49gd362bagd04eedgf459beg9a8ee7g9da116g658f0eg69db80gd3e915gb82986g3e233bgba40c0g0f42a8g906be0geec4b7g8fc789g4b7944g366a5eg6cd8cfg5c6f74g033e6ag3e9574g45a461g3390a7g5dedebg7c944bg
</pre>

```python
matrix = "83ad8cgf228bfgc7adf1g4a588eg265a87gcc165dg64ad49gd362bagd04eedgf459beg9a8ee7g9da116g658f0eg69db80gd3e915gb82986g3e233bgba40c0g0f42a8g906be0geec4b7g8fc789g4b7944g366a5eg6cd8cfg5c6f74g033e6ag3e9574g45a461g3390a7g5dedebg7c944bg"
result = [matrix[:i][-7:] for i in range(7,len(matrix)+7,7)]
md5_1 = ''.join([i[0] for i in result]);print(md5_1)
md5_2 = ''.join([i[1] for i in result]);print(md5_2)
md5_3 = ''.join([i[2] for i in result]);print(md5_3)
md5_4 = ''.join([i[3] for i in result]);print(md5_4)
md5_5 = ''.join([i[4] for i in result]);print(md5_5)
md5_6 = ''.join([i[5] for i in result]);print(md5_6)
```

<p>Hasil program dan hasil decrypt pada <a href="https://md5.gromweb.com/">link</a></p>
<pre>
8fc42c6ddf9966db3b09e84365034357 = the
327a6c4304ad5938eaf0efb6cc3e53dc = flag
a2a551a6458a8de22446cc76d639a9e9 = is
d8d8a6d2e9e1fb99302b479a8fe540d4 = sha256
8bf8854bebe108183caeb845c7676ae4 = of
cf1e7d9ade76e056b080794ef4a417bb = redblood
</pre>

<h3><b>Solution</h3></b>
<pre>
redblood
</pre>
