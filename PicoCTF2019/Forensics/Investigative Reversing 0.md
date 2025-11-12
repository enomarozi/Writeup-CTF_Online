```python3
local_54 = 6
part1 = "picoCT"
print(part1,end='')
text = '70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71'.split(' ')
for i in range(local_54, 0xf):
    print(chr(int(text[i-0x5],16)-0x5),end='')

local_50 = 0x10
for i in range(local_50, 0x1a):
    print(chr(int(text[i-0x9],16)),end='')
```
