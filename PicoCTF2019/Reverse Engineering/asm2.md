<h1>asm2</h1>
<h3>Description</h3>
<pre>
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. <a href='https://jupiter.challenges.picoctf.org/static/ceac75672637589213b952abe32c84b3/test.S'>Source</a>
</pre>
<h3>Solution</h3>
<p>Persamaan programmnya di python</p>

```python3
param1,param2 = int(0x4),int(0x2d)
while param1 <= int(0x5fa1):
    param2 += int(0x1)
    param1 += int(0xd1)

print(hex(param2))
```
<h3>Flag</h3>
<pre>
0xa3
</pre>
