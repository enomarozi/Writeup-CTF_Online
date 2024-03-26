<h1>endianness</h1>
<h3>Description</h3>
<p>
  Know of little and big endian?
  nc titan.picoctf.net 53315. <a href='https://artifacts.picoctf.net/c_titan/78/flag.c'>Source</a>
</p>
<h3>Solution</h3>
<p>Kurang lebih dengan program C</p>

```python
import sys

def get_endian(args):
    big_endian = ''.join([hex(ord(i))[2:].rjust(2,'0') for i in args[1]])
    little_endian = ''.join([hex(ord(i))[2:].rjust(2,'0') for i in args[1][::-1]])
    print("Little Endian :",little_endian)
    print("Big Endian :",big_endian)
    
args = sys.argv
get_endian(args)
```

```console
root@xisco-VirtualBox:/home/xisco/Downloads# python3 ok.py akecq
Little Endian : 7163656b61
Big Endian : 616b656371
```
<p>Masukan Little dan Big Endiannya</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# nc titan.picoctf.net 53315
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: akecq
Enter the Little Endian representation: 7163656b61
Correct Little Endian representation!
Enter the Big Endian representation: 616b656371
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_cfe38ef0}
```

<h3>Flag</h3>
<pre>picoCTF{3ndi4n_sw4p_su33ess_cfe38ef0}</pre>
