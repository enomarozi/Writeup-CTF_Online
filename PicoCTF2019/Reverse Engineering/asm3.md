<h1>asm3</h1>
<h3>Description</h3>
<pre>
What does asm3(0xdb5bc7fb,0xd5781141,0xc7d66f97) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. <a href='https://challenge-files.picoctf.net/c_fickle_tempest/64f65c2cd120e568d93fc10d4cce2d3f1c163fa67f980d36736f6abd8b9481a5/test.S'>Source</a>
</pre>
<h3>Solution</h3>
<label>Diberikan file assembly dan fungsi param asm3(0xdb5bc7fb,0xd5781141,0xc7d66f97)</label>

```assembly
asm3:
	<+0>:	endbr32 
	<+4>:	push   ebp
	<+5>:	mov    ebp,esp
	<+7>:	xor    eax,eax
	<+9>:	mov    ah,BYTE PTR [ebp+0xb]
	<+12>:	shl    ax,0x10
	<+16>:	sub    al,BYTE PTR [ebp+0xd]
	<+19>:	add    ah,BYTE PTR [ebp+0xf]
	<+22>:	xor    ax,WORD PTR [ebp+0x12]
	<+26>:	nop
	<+27>:	pop    ebp
	<+28>:	ret 
```
<label>Persamaan script python</label>

```python3
#ebp_08 = 0xdb5bc7fb
#ebp_12 = 0xd5781141
#ebp_16 = 0xc7d66f97

ax = 0x0000
al = (0x00 - 0x11) & 0xff
ah = (0x00 + 0xd5) & 0xff
ax = (ah << 8) | al
ax ^= 0xc7d6
print(hex(ax))
```
<h3>Flag</h3>
<pre>
0x1239
</pre>
