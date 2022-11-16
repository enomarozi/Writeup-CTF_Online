<h1>ARMssembly 0</h1>
<p>What integer does this program print with arguments 266134863 and 1592237099? File: <a href='https://mercury.picoctf.net/static/104d6022bcea93f53083aeb61b134e8b/chall.S'>chall.S</a> Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})</p>
<h3>Solution</h3>
<p>Diberikan sebuah file ARMassembly, dan perhatikan fungsi 'func1' dengan nilai argument 266134863 and 1592237099</p>

```pre
func1:
	sub	sp, sp, #16              --> Stack Pointer
	str	w0, [sp, 12]             --> store w0[sp-12] = 266134863
	str	w1, [sp, 8]              --> store w1[sp-8]  = 1592237099
	ldr	w1, [sp, 12]             --> load w1[sp-12]  = 266134863
	ldr	w0, [sp, 8]              --> load w2[sp-8]   = 1592237099
	cmp	w1, w0                   --> compare w1 w0 (w1-w0)
	bls	.L2                      --> branch less (w1<w0) goto L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]              --> load w0[sp-8]   = 1592237099
.L3:
	add	sp, sp, 16
	ret
 ```
<p>Format flag nilai hexadesimal dari output tanpa symbol "0x"</p>

```pre
1592237099 = 0x5ee79c2b --> Flag = 5ee79c2b
```

<h3>Solution</h3>
<p>picoCTF{5ee79c2b}</p>
