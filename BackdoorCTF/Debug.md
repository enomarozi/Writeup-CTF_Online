<h1><b>Debug</b></h1>
<pre>
Take sha256 of string obtained.
http://static.beast.sdslabs.co/static/DEBUG/debug32
</pre>
<h3><b>Solution</b></h3>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/Debug.jpg">
</p>
<p>Decompile file dengan ghidra. Karena filenya type stripped jadi kita tidak bisa melihat nama fungsi asli programnya. 
Dan disana terdapat print flag yang terdapat pada fungsi FUN_0804849b. dan juga beberapa operasi yang berkemungkinan mencetak suatu string</p>


```python
local_24 = [0x1686f596, 0x5646f537, 0x76765726, 0x37f52756, 0xc6c696b6]
local_30 = 0
while local_30 < 5:
    local_2c = local_24[local_30]
    while local_2c != 0:
        text = (((local_2c & 0xf) << 4) | (local_2c & 0xff) >> 4)
        local_2c >>= 8
        print(chr(text),end="")
    local_30 += 1
```

<h3><b>Flag</b></h3>
<pre>
i_has_debugger_skill
</pre>
