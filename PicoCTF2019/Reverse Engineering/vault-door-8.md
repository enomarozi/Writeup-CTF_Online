<h1>vault-door-8</h1>
<h3>Description</h3>
<pre>
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: <a href='https://jupiter.challenges.picoctf.org/static/87f4f8ce117f80ab7b809f161661ce6a/VaultDoor8.java'>VaultDoor8.java</a>
</pre>
<h3>Solution</h3>
<p>Hasil Convert ke Python dan reverse</p>

```python3
def switchBits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = ((bit1 << shift) | (bit2 >> shift) | rest)
    return result
    
flag = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC2, 0xD2, 0x95, 0xA4, 0xF0, 0xD2, 0xD2, 0xC1, 0x95]
for i in range(len(flag)):
    c = flag[i]
    c = switchBits(c,6,7)
    c = switchBits(c,2,5)
    c = switchBits(c,3,4)
    c = switchBits(c,0,1)
    c = switchBits(c,4,7)
    c = switchBits(c,5,6)
    c = switchBits(c,0,3)
    c = switchBits(c,1,2)
    print(chr(c),end='')
```
<h3>Flag</h3>
<pre>
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_89eb3994e}
</pre>
