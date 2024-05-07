<h1>packer</h1>
<h3>Description</h3>
<p>Reverse this linux executable?
<a href='https://artifacts.picoctf.net/c_titan/102/out'>binary</a></p>
<h3>Solution</h3>

<p>Check fungsi main() pada disassembly ghidra</p>

```python3
flag = "6437323338333633343330333133343339336635333533333936323534336536313332346635363365343133623633363433303565363535663538353933353562373634343533346636333639363037"
print(bytes.fromhex(flag)[::-1])
flag = "7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f39343130343638327d"
print(bytes.fromhex(flag))
```
<h3>Flag</h3>
<pre>picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_94104682}</pre>
