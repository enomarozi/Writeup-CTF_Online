<h1>GDB baby step 1</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Disassemble <a href='https://artifacts.picoctf.net/c/512/debugger0_a'>this</a>.
</pre>
<h3>Solution</h3>
<p>Dissasembly program dan perhatikan nilai register eax</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# objdump -d debugger0_a| awk '/<main>:/,/^$/'  
0000000000001129 <main>:
    1129:	f3 0f 1e fa          	endbr64
    112d:	55                   	push   %rbp
    112e:	48 89 e5             	mov    %rsp,%rbp
    1131:	89 7d fc             	mov    %edi,-0x4(%rbp)
    1134:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)
    1138:	b8 42 63 08 00       	mov    $0x86342,%eax
    113d:	5d                   	pop    %rbp
    113e:	c3                   	ret
    113f:	90                   	nop

                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# printf "picoCTF{%d}\n" 0x86342
picoCTF{549698}
```
<h3>Flag</h3>
<pre>
picoCTF{549698}
</pre>
