<h1><b>Wheres the f4cking password</b></h1>
<pre>
fs0ciety made a zip but forgot the password,but somehow dr3dd cracked the zip. 
Can you crack it too..!!

<a href="http://static.beast.sdslabs.co/static/Where's%20the%20f4cking%20password/file.zip">Link</a>

Hint: CRC32 Hash Collision Probability
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan 1 file zip berpassword, disini kita tidak akan me-bruteforce password zip, karena size dari masing-masing isi file zip hanya 5 bytes atau 5 string ascii</p>

```python
import zlib
import zipfile

file = "file.zip"
fh = zipfile.ZipFile(file)
for info in fh.infolist():
    print(info.filename ,hex(info.CRC),"dan size", int(info.file_size),"bytes")

```
<p>Hasil</p>
<pre>
part1.txt 0xf1792cdc dan size 5 bytes
part2.txt 0x9badb643 dan size 5 bytes
part3.txt 0x33743a30 dan size 5 bytes
part4.txt 0xa707d325 dan size 5 bytes
part5.txt 0x1655e253 dan size 5 bytes
</pre>
<p>Selanjutnya kita bisa mencari collision CRC32 dari masing-masing file, CRC32 file = content file flag</p>

```python
import zlib
import zipfile
import itertools
import string

list_crc = ["0xf1792cdc","0x9badb643","0x33743a30",
            "0xa707d325","0x1655e253"]
letter = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{_}"
brute_crc = itertools.product(letter, repeat=5)
for i in brute_crc:
    password = ''.join(i)
    crc32 = zlib.crc32(password.encode('utf8'))
    if hex(crc32) in list_crc:
        print(str(password)+" and crc "+str(hex(crc32)))
```
<p>Hasil</p>
<pre>
g00d} and crc 0x1655e253
rc_15 and crc 0x9badb643
th4t_ and crc 0xa707d325
CTF{c and crc 0xf1792cdc
_n0t_ and crc 0x33743a30
</pre>

<h3><b>Flag</b></h3>
<pre>
CTF{crc_15_n0t_th4t_g00d}
</pre>
