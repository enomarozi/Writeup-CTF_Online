<h1>GDB baby step 4</h1>
<h3>Description</h3>
<pre>
main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be picoCTF{4096}.
Debug <a href='https://artifacts.picoctf.net/c/532/debugger0_d'>this</a>.
</pre>
<h3>Solution</h3>
<p>dapatkan eax dari func1</p>

```assembly
 0x0000000000401106 <+0>:	endbr64
 0x000000000040110a <+4>:	push   rbp
 0x000000000040110b <+5>:	mov    rbp,rsp
 0x000000000040110e <+8>:	mov    DWORD PTR [rbp-0x4],edi
 0x0000000000401111 <+11>:	mov    eax,DWORD PTR [rbp-0x4]
 0x0000000000401114 <+14>:	imul   eax,eax,0x3269
 0x000000000040111a <+20>:	pop    rbp
 0x000000000040111b <+21>:	ret
```

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# printf "picoCTF{%d}" 0x3269       
picoCTF{12905}
```

<h3>Flag</h3>
<pre>
picoCTF{12905}
</pre>
