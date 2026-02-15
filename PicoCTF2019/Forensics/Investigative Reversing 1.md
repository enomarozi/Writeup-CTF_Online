<h1>Investigative Reversing 1</h1>
<h3>Description</h3>
<pre>
We have recovered a <a href='https://challenge-files.picoctf.net/c_fickle_tempest/3aeddcd34ea793b113c05097c002e6b3d187f224908bd1a85a8e7a1e11d15220/mystery'>binary</a> and a few images: <a href='https://challenge-files.picoctf.net/c_fickle_tempest/3aeddcd34ea793b113c05097c002e6b3d187f224908bd1a85a8e7a1e11d15220/mystery.png'>image</a>, <a href='https://challenge-files.picoctf.net/c_fickle_tempest/3aeddcd34ea793b113c05097c002e6b3d187f224908bd1a85a8e7a1e11d15220/mystery2.png'>image2</a>, <a href='https://challenge-files.picoctf.net/c_fickle_tempest/3aeddcd34ea793b113c05097c002e6b3d187f224908bd1a85a8e7a1e11d15220/mystery3.png'>image3</a>. See what you can make of it. There should be a flag somewhere.
</pre>
<h3>Solution</h3>
<label>Disassembly file elf dengan ghidra dan reverse</label>

```python3
stream_00 = open("mystery.png","rb").read().split(b"IEND")[1][4:]
stream_01 = open("mystery2.png","rb").read().split(b"IEND")[1][4:]
stream_02 = open("mystery3.png","rb").read().split(b"IEND")[1][4:]
flag = bytearray(26)

flag[0] = (stream_01[0] - 0x15) & 0xFF
flag[1] = stream_02[0]
flag[2] = stream_02[1]
flag[3] = (stream_01[-1] - 4) & 0xFF
flag[4] = stream_02[2]
flag[5] = stream_00[0]

flag[6:10] = stream_00[1:5]
flag[10:15] = stream_02[3:8]
flag[15:26] = stream_00[5:16]

print(flag.decode(errors="ignore"))
```
<h3>Flag</h3>
<pre>
picoTCF{An0tha_1_8a448cb2}
</pre>
