<h1>Bit-O-Asm-1</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href='https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt'>here.</a>
</pre>
<h3>Solution</h3>

<p>Intruksi soal</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# cat disassembler-dump0_a.txt                            
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
                                                                                
┌──(root㉿Python)-[/home/venom/Downloads]
└─# hexa=$(cat disassembler-dump0_a.txt | grep -oE 0x.* | tail -n 1);printf "picoCTF{%d}\n" hexa
picoCTF{48}
```
<h3>Flag</h3>
<pre>
picoCTF{48}
</pre>
