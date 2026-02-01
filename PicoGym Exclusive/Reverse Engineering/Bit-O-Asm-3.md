<h1>Bit-O-Asm-3</h1>
<h3>Deescription</h3>
<pre>
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href='https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt'>here.</a>
</pre>
<p>Sesuai soal dan perhatikan opcode dan operand</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# cat disassembler-dump0_c.txt 
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
                                                                                                                    
```

```python3
rbp_0xc = 0x9fe1a
rbp_0x8 = 0x4
eax = rbp_0xc
eax *= rbp_0x8
eax += 0x1f5
rbp_0x4 = eax
eax = rbp_0x4
print('picoCTF{'+str(eax)+'}')
```
<h3>Flag</h3>
<pre>
picoCTF{2619997}
</pre>
