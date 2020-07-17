<h1><b>Love Letter</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/93af48d6653be40a1919484a7481ddc4.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Analisa raw bytes file, disana terdapat beberapa codec yang tidak dapat didecode menjadi ascii yaitu 0xa0 dan juga ambil semua value 0x20 untuk disatukan menjadi binary data</p>

```python
with open("LoveLetter.txt","rb") as f:
    flag_data = ""
    for i in f.read():
        if i == 160:
            flag_data += "1"
        elif i == 32:
            flag_data += "0"
    print(flag_data)
    flag = ''.join([chr(int(flag_data[:i][-8:],2)) for i in range(8,len(flag_data)+8,8)])
    print(flag)
```
</b><h3>Flag</h3></b>
<pre>
FLAG-3b6f70fcf070009561f5276fe98fc9c6
</pre>
