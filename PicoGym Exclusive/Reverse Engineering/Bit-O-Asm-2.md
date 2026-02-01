<h1>Bit-O-Asm-2</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href='https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt'>here</a>. 
</pre>
<h3>Solution</h3>

<p>Sesuai soal</p>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# hexa=$(strings disassembler-dump0_b.txt| grep -oE '0x9[0-9a-fA-F]+'); printf 'picoCTF{%d}' hexa
picoCTF{654874} 
```
<h3>Flag</h3>
<pre>
picoCTF{654874}
</pre>
