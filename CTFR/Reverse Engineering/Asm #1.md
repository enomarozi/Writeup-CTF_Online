<h1><b>Asm #1</b></h1>
<pre>
Pertama kali mendengar Assembly ? Coba kalkukasi dari instruksi dibawah ini.

Flag : CTFR{0x(Hexadecimal)}

main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 10
        add     DWORD PTR [rbp-4], 50
        sub     DWORD PTR [rbp-4], 100
        add     DWORD PTR [rbp-4], 1328
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret
</pre>
<h3><b>Solution</b></h3>
<p>Kalkulasi sederhana dengan assembly</p>
<pre>
mov --> menyimpan nilai 10
add --> menambah 50 + 10
sub --> mengurang 60 - 100
add --> menambah (-40) + 1328
</pre>

```python3
print('CTFR{'+hex(10+50-100+1328)+'}')
```
<h3><b>Flag</b></h3>
<pre>
CTFR{0x508}
</pre>
