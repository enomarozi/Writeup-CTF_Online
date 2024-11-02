<h1>vault-door-6</h1>
<h3>Description</h3>
<pre>
This vault uses an XOR encryption scheme. The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java'>VaultDoor6.java</a>
</pre>
<h3>Solution</h3>
<p>Cek Source code, xor dengan 0x55</p>

```python3
hex_flag = "0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d, 0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa , 0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27, 0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36".replace(' ','').split(',')
result = 'picoCTF{'
for i in hex_flag:
    result += chr(int(i[2:],16)^0x55)
print(result+"}")
```

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py                         
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
                                                                                                                                                              
┌──(root㉿Python)-[/home/venom/Downloads]
└─# python3 solved.py | java VaultDoor6
Enter vault password: Access granted.
```

<h3>Flag</h3>
<pre>
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}
</pre>
