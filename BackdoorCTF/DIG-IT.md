<h1><b>DIG-IT</b></h1>
<pre>
n00b claims for being pr0 in reversing. To be honest I don't think so. 
Prove me wrong, I will reward you the precious flag.
<a href="http://static.beast.sdslabs.co/static/DIG-IT/rev">file</a>

Flag = CTF{some_string}
</pre>
<h3><b>Solution</b></h3>
<p>Decompile program dengan tool hidra, maka didapatkan string yang memungkinkan mencetak ascii yang terdapat pada fungsi main() program</p>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/DIG-IT.jpg">
</p>
<p>Cetak semua string ke ascii</p>

```python
flag_dat = [0x73, 0x74, 0x72, 0x31, 0x6e, 0x67, 0x73, 0x5f, 0x34, 0x72, 0x33, 0x5f,
            0x6e, 0x30, 0x74, 0x5f, 0x34, 0x6c, 0x77, 0x34, 0x79, 0x73, 0x5f, 0x68,
            0x65, 0x6c, 0x70, 0x66, 0x75, 0x6c]
for i in flag_dat:
    print(chr(i),end='')
```
<h3><b>Flag</b></h3>
<pre>
CTF{str1ngs_4r3_n0t_4lw4ys_helpful}
</pre>
