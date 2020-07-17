<h1><b>LoadSomeBits</h1></b>
<pre>
Can you find the flag encoded inside this <a href="https://2018shell.picoctf.com/static/add26913a57edadb9ebeaa88cef670bc/pico2018-special-logo.bmp">image</a>? 
You can also find the file in /problems/loadsomebits_1_5ccf71e5726692c713405bb17da5cb37 on the shell server.
</pre>
</b><h3>Solution</h3></b>
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/LoadSomeBits1.jpg">
</p>
<p>Binary flag terdapat pada LSB (Least significant bits) image pada posisi 0x36 hingga 0x1ee</p>
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/LoadSomeBits.jpg">
</p>

```python
with open("pico2018-special-logo.bmp","rb") as f:
    data = f.read()
    data_flag = ""
    for i in range(54,494):
        data_flag += str(data[i])
    result = ''.join([chr(int(data_flag[:i][-8:],2)) for i in range(8,len(data_flag)+8,8)])
    print(result)
 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_882756901}
</pre>
