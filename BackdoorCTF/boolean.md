<h1><b>boolean</b></h1>
<pre>
I like NAND logic, what's your favourite?

http://static.beast.sdslabs.co/static/noob/boolean
</pre>
<h3><b>Solution</b></h3>
<p>Decompile program dengan ghidra, periksa pada fungsu check, disana terdapat operasi xor terhadap list hexadesimal</p>
<p align="center">
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/boolean.jpg">
</p>
<p>Eksekusi sesuai operasi tersebut pada python</p>

```python
list_bool = [0x2f, 0x25, 0x28, 0x2e, 0x32, 0x31, 0x79, 0x3b, 0x16, 0x78, 0x3a,
             0x16, 0x24, 0x30, 0x16, 0x2f, 0x7d, 0x3f, 0x79, 0x3c, 0x3b, 0x20,
             0x3d, 0x7a, 0x34]
local_44 = 0
for i in list_bool:
    print(chr(i^0x49),end="")
```
<h3><b>Flag</b></h3>
<pre>
flag{x0r_1s_my_f4v0urit3}
</pre>
