<h1>endianness-v2</h1>
<h3>Description</h3>
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.
Download it here and see what you can get out of it
<a href='https://artifacts.picoctf.net/c_titan/115/challengefile'>File</a>

<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# xxd challengefile | head -n 10
00000000: e0ff d8ff 464a 1000 0100 4649 0100 0001  ....FJ....FI....
00000010: 0000 0100 4300 dbff 0606 0800 0805 0607  ....C...........
00000020: 0907 0707 0c0a 0809 0b0c 0d14 1219 0c0b  ................
00000030: 1d14 0f13 1d1e 1f1a 201c 1c1a 2027 2e24  ........ ... '.$
00000040: 1c23 2c22 2937 281c 3431 302c 271f 3434  .#,")7(.410,'.44
00000050: 3238 3d39 3433 2e3c 00db ff32 0909 0143  28=943.<...2...C
00000060: 0c0b 0c09 180d 0d18 211c 2132 3232 3232  ........!.!22222
00000070: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000080: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000090: 3232 3232 3232 3232 3232 3232 c0ff 3232  222222222222..22
root@xisco-VirtualBox:/home/xisco/Downloads# 

```
<p>Binary JPG -> ff d8 ff e0 00 10 4a 46 49 46 00 01</p>
<p>Sedangkan pada challenge "e0 ff d8 ff 46 4a 10 00 01 00 46 49", yang sepertinya binary file teracak dengan pola</p>
<p align='center'>
  <img  src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2024/Forensics/Images/pola.jpg">
</p>

```python3
file = open("challengefile",'rb').read()
list_data_rev = []
result = ""
for i in file:
    if len(list_data_rev) == 4:
        result += ''.join(list_data_rev)[::-1]
        list_data_rev = []
    list_data_rev.append(str(hex(i))[2:].rjust(2,'0')[::-1])

file = open("image.jpg","wb")
file.write(bytes.fromhex(result))
file.close()

```
<p align='center'>
  <img  src="https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2024/Forensics/Images/file.jpg">
</p>

<h3>Flag</h3>
<pre>
  picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_004850bf}
</pre>
