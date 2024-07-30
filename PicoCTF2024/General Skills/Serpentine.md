<h1>Serpentine</h1>
<h3>Description</h3>
<p>Find the flag in the Python script!
Download Python <a href='https://artifacts.picoctf.net/c/37/serpentine.py'>script</a></p>
<h3>Solution</h3>
<p>Tambah fungsi print_flag() pada source code, dan running</p>

```python3
elif choice == 'b':  
      print_flag()
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```

```console
Welcome to the serpentine encourager!


a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b
picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}
```
<p>Script python</p>

```python3
flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5c) + chr(0x01) + chr(0x57) + chr(0x2a) + chr(0x17) + chr(0x5e) + chr(0x5f) + chr(0x0d) + chr(0x3b) + chr(0x19) + chr(0x56) + chr(0x5b) + chr(0x5e) + chr(0x36) + chr(0x53) + chr(0x07) + chr(0x51) + chr(0x18) + chr(0x58) + chr(0x05) + chr(0x57) + chr(0x11) + chr(0x3a) + chr(0x56) + chr(0x0e) + chr(0x5d) + chr(0x53) + chr(0x11) + chr(0x54) + chr(0x5c) + chr(0x53) + chr(0x14)
key = "enkidu"*7
for i,j in zip(flag_enc,key):
    print(chr(ord(i)^ord(j)),end='')
    

```
<h3>Flag</h3>
<pre>
picoCTF{7h3_r04d_l355_7r4v3l3d_8e47d128}
</pre>
