<h1>Bit-O-Asm-4</h1>
<h3>Description</h3>
<pre>
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href='https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt'>here.</a>
</pre>
<h3>Solution</h3>
<p>Ikuti intruksi assembly</p>

```assembly
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a ;simpan 654874 ke rbp-0x4
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710 ;bandingkan 10000 dengan 654874
<+29>:    jle    0x55555555514e <main+37> ;jika 10000 < 654874
<+31>:    sub    DWORD PTR [rbp-0x4],0x65 ;maka kurangi, 654874 - 65
<+45>:    ret #return
```

```python3
rbp_0x4 = 0x9fe1a
temp = 0x2710
if temp <= rbp_0x4:
    rbp_0x4 -= 0x65
else:
    rbp_0x4 += 0x65
print('picoCTF{'+str(rbp_0x4)+'}')
```

<h3>Flag</h3>
<pre>
picoCTF{654773}
</pre>
