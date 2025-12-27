<h1>ELF C++ - 0 protection</h1>
<h3>Description</h3>
<label>Find the validation password.</label><a href='https://static.root-me.org/cracking/ch25/ch25.bin'>File</a>
<h3>Solution</h3>
<label>Cek fungsi main() di alamat &DAT_08048dc4 dan &DAT_08048dcc</label>
<pre>
&DAT_08048dc4 = 18 d6 15 ca fa 77
&DAT_08048dcc = 50 b3 67 af a5 0e 77 a3 4a a2 9b 01 7d 89 61 a5 a5 02 76 b2 70 b8 89 03 79 b8 71 95 9b 28 74 bf 61 be 96 12 47 95 3e e1 a5 04 6c a3 73 ac 89
</pre>

```python3
param1 = '18 d6 15 ca fa 77'.split(' ')*8
param2 = '50 b3 67 af a5 0e 77 a3 4a a2 9b 01 7d 89 61 a5 a5 02 76 b2 70 b8 89 03 79 b8 71 95 9b 28 74 bf 61 be 96 12 47 95 3e e1 a5 04 6c a3 73 ac 89'.split(' ')
for i,j in zip(param1, param2):
    print(chr(int(i,16)^int(j,16)),end='')
```
<h3>Flag</h3>
<pre>
Here_you_have_to_understand_a_little_C++_stuffs
</pre>
