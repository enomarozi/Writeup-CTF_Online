<h1>GDB baby step 3</h1>
<h3>Description</h3>
<pre>
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
Debug <a href='https://artifacts.picoctf.net/c/531/debugger0_c'>this</a>.
</pre>
<h3>Solution</h3>
<p>Perhatikan Soal dan Hint pada soal</p>

```assembly
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   rbp
   0x000000000040110b <+5>:	mov    rbp,rsp
   0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:	mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:	mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:	mov    eax,DWORD PTR [rbp-0x4] ; <-- memory rbp-0x4
   0x000000000040111f <+25>:	pop    rbp
   0x0000000000401120 <+26>:	ret
```
<p>Set Breakpint main dan 0x000000000040111f lalu run dan continue</p>

```console
gef➤  x/4xb $rbp-0x4
0x7fffffffe27c:	0x6b	0xc9	0x62	0x22
```
<h3>Flag</h3>
<pre>
picoCTF{0x6bc96222}
</pre>
