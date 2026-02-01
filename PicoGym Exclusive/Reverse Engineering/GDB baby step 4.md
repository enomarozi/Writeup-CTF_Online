<h1>GDB baby step 4</h1>
<h3>Description</h3>
<pre>
main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be picoCTF{4096}.
Debug <a href='https://artifacts.picoctf.net/c/532/debugger0_d'>this</a>.
</pre>
<h3>Solution</h3>
<p>dapatkan eax dari func1</p>

```assembly
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# gdb -q debugger0_d 
GEF for linux ready, type `gef' to start, `gef config' to configure
93 commands loaded and 5 functions added for GDB 17.1 in 0.00ms using Python engine 3.13
Reading symbols from debugger0_d...
(No debugging symbols found in debugger0_d)
gef➤  disas main
Dump of assembler code for function main:
   0x000000000040111c <+0>:	endbr64
   0x0000000000401120 <+4>:	push   rbp
   0x0000000000401121 <+5>:	mov    rbp,rsp
   0x0000000000401124 <+8>:	sub    rsp,0x20
   0x0000000000401128 <+12>:	mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:	mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:	mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:	mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:	mov    edi,eax
   0x0000000000401142 <+38>:	call   0x401106 <func1>
   0x0000000000401147 <+43>:	mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:	leave
   0x000000000040114e <+50>:	ret
End of assembler dump.
gef➤  disas func1
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   rbp
   0x000000000040110b <+5>:	mov    rbp,rsp
   0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:	mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:	imul   eax,eax,0x3269
   0x000000000040111a <+20>:	pop    rbp
   0x000000000040111b <+21>:	ret
End of assembler dump.
gef➤  print/d 0x3269
$1 = 12905
gef➤  

```

<h3>Flag</h3>
<pre>
picoCTF{12905}
</pre>
