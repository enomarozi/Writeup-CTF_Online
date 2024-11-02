<h1>asm1</h1>
<h3>Description</h3>
<pre>
What does asm1(0x6fa) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. <a href='https://jupiter.challenges.picoctf.org/static/b41e08fc19ceb9d0466ebd68d36c5630/test.S'>Source</a>
</pre>
<h3>Solution</h3>
<p>Berikut script persamaan dengan assembly</p>

```assembly
asm1:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x3a2
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x358
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0x12
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0x12
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x6fa
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0x12
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0x12
        <+60>:  pop    ebp
        <+61>:  ret    

```

```python
def solved(param):
    if param > 0x3a2:
        if param == 0x6fa:
            result = param - 0x12
            return hex(result)
        elif param != 0x6fa:
            result = param + 0x12
            return hex(result)
    if param == 0x358:
        result = param - 0x12
        return hex(result)
    if param != 0x358:
        result = param - 0x12
        return hex(result)
        

param = 0x6fa
print(solved(param))
```
<p>Flag tidak menggunakan format picoCTF{}</p>
<h3>Flag</h3>
<pre>
0x6e8
</pre>
