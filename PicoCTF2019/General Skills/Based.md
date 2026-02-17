<h1>Based</h1>
<h3>Description</h3>
<pre>
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337?
Connect with nc fickle-tempest.picoctf.net 62828.
</pre>
<h3>Solution</h3>

```python3
from pwn import *

def binary_to_text(data):
    text = ''.join([chr(int(b, 2)) for b in data])
    return text

def ocatl_to_text(data):
    text = ''.join([chr(int(b, 8)) for b in data])
    return text

def hex_to_text(data):
    text = bytes.fromhex(data[0])
    return text

host = "fickle-tempest.picoctf.net"
port = 62828
r = remote(host,port)

line = r.recvuntil(b"Input:").decode()
data = line.split('the ')[1].split(' as')[0].split(' ')
soal_1 = binary_to_text(data)
r.sendline(soal_1)

line = r.recvuntil(b"Input:").decode()
data = line.replace('o','').split('the  ')[1].split(' as')[0].split(' ')
soal_2 = ocatl_to_text(data)
r.sendline(soal_2)

line = r.recvuntil(b"Input:").decode()
data = line.split('the ')[1].split(' as')[0].split(' ')
soal_3 = hex_to_text(data)
r.sendline(soal_3)

output = r.recvall(timeout=5).decode()
print(output)
```
<label>Output</label>

```console
[+] Opening connection to fickle-tempest.picoctf.net on port 62828: Done
/home/venom/Downloads/ok.py:22: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendline(soal_1)
/home/venom/Downloads/ok.py:27: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendline(soal_2)
[+] Receiving all data: Done (86B)
[*] Closed connection to fickle-tempest.picoctf.net port 62828

You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_aa2bA794}
```
<h3>Flag</h3>
<pre>
picoCTF{learning_about_converting_values_aa2bA794}
</pre>
