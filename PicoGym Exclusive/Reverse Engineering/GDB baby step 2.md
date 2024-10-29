<h1>GDB baby step 2</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Debug <a href='https://artifacts.picoctf.net/c/520/debugger0_b'>this</a>.
</pre>
<h3>Solution</h3>
<p>Ada operasi aritmatika dalam program</p>

```assembly
 0x0000000000401115 <+15>:	mov    DWORD PTR [rbp-0x4],0x1e0da ;simpan 0x1e0da ke rbp-0x4
 0x000000000040111c <+22>:	mov    DWORD PTR [rbp-0xc],0x25f ;simpan 0x25f ke rbp-0xc
 0x0000000000401123 <+29>:	mov    DWORD PTR [rbp-0x8],0x0 ;simpan 0x0 ke rbp-0x8
 0x000000000040112a <+36>:	jmp    0x401136 <main+48> ; while true
 0x000000000040112c <+38>:	mov    eax,DWORD PTR [rbp-0x8] ;rbp-0x8 ke register eax
 0x000000000040112f <+41>:	add    DWORD PTR [rbp-0x4],eax ;eax + rbp-0x4
 0x0000000000401132 <+44>:	add    DWORD PTR [rbp-0x8],0x1 ;0x1 + rbp-0x8
 0x0000000000401136 <+48>:	mov    eax,DWORD PTR [rbp-0x8] ;rbp-0x8 ke register eax
 0x0000000000401139 <+51>:	cmp    eax,DWORD PTR [rbp-0xc] ;jika eax < rbp-0xc
 0x000000000040113c <+54>:	jl     0x40112c <main+38> ;goto <main+38>
 0x000000000040113e <+56>:	mov    eax,DWORD PTR [rbp-0x4] ;rbp-0x4 ke register eax
```
<p>Persamaan dengan script python</p>

```python3
result = 0x1e0da
batas = 0x25f
inc_ = 0
while True:
    inc_ += 1
    if inc_ >= batas:
        break
    result += inc_

print("picoCTF{"+str(result)+"}")
```

<h3>Flag</h3>
<pre>
picoCTF{307019}
</pre>
