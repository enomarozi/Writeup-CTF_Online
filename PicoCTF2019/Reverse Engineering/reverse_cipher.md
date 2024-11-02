<h1>reverse_cipher</h1>
<h3>Description</h3>
<pre>
We have recovered a <a href='https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev'>binary</a> and a <a href='https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this'>text file</a>. Can you reverse the flag.
</pre>
<h3>Solution</h3>
<p>Buka dengan ghidra, rev proses encrypt nya</p>

```python3
local_10 = 0
local_14 = 0
local_9 = ''
local_58 = open('rev_this','r').read()


for local_10 in range(0x8):
    local_9 = local_58[local_10]
    print(local_9,end='')

for local_14 in range(0x8,0x17):
    if (local_14 & 1) == 0:
        local_9 = chr(ord(local_58[local_14])-5)
    else:
        local_9 = chr(ord(local_58[local_14])+2)
    print(local_9,end='')
print("}",end='')
```
<h3>Flag</h3>
<pre>
picoCTF{r3v3rs36ad73964}
</pre>
