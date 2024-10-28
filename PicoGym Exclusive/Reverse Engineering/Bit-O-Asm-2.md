<h1>Bit-O-Asm-2</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href='https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt'>here</a>. 
</pre>
<h3>Solution</h3>

<p>Sesuai soal</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# cat disassembler-dump0_b.txt                   
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
                                                                                                                    
┌──(root㉿Python)-[/home/venom/Downloads]
└─# printf "picoCTF{%d}\n" 0x9fe1a
picoCTF{654874}

```
<h3>Flag</h3>
<pre>
picoCTF{654874}
</pre>
