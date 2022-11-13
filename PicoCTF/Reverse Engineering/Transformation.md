<h1>Transformation</h1>
<p>I wonder what this really is... <a href='https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc'>enc</a> ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])</p>
<h3>Solution</h3>
<p>Diberikan sebuah Encrypted flag :</p>
<pre>
Character Flag : 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽
Order Flag : 28777,25455,17236,18043,12598,24418,26996,29535,26990,29556,13108,25695,28518,24376,24420,13618,25398,25145,13181
</pre>
<p>Bruteforce masing-masing character flag</p>

```python3
import string

flag_enc = [28777,25455,17236,18043,12598,24418,26996,29535,26990,29556,13108,25695,28518,24376,24420,13618,25398,25145,13181]
def bruteforce(str1,str2,a):
    flag = str1+str2
    for i in range(0,len(flag),2):
        split_flag = (ord(flag[i]) << 8)+(ord(flag[i + 1]))
        if split_flag == flag_enc[a]:
            print(str1+str2,end='')
for a in range(len(flag_enc)):
    for i in string.printable:
        for j in string.printable:
            bruteforce(i,j,a)
```
<p>Atau decode utf16-be</p>

```python3
file = open('enc','r').readline()
print(file.encode('utf-16-be').decode('ascii'))
```
<h3>Flag</h3>
<p>
  picoCTF{16_bits_inst34d_of_8_d52c6b93}
</p>
