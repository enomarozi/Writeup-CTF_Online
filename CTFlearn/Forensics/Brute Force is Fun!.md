<h1><b>Brute Force is Fun!</h1></b>
<pre>
You'll need Brute Force to solve this. Knowing Python should help too. 
Oh! And Base64 encryption of course! Find the flag!

https://mega.nz/#!vf43RCyC!NNpuYjB3d-gevhsHXefwAAAmzk4tJHxUZr0GnrSDI_c 
Hash: e82a4b4a0386d5232d52337f36d2ab73
</pre>
</b><h3>Solution</h3></b>
<p>Ekstrak file JPG dengan binwalk tool, dan didapatkan 1 file ZIP, pada file ZIP terdapat 1 file flag.zip dan ratusan direktori</p>
<p>Ketika ektrak flag.zip ternyata ZIP berpassword, lanjut eksekusi perintah grep pada terminal maka didapatkan clue password</p>

```console
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# grep -iR flag
Binary file 1926.zip matches
folders/73/47/p:The password is: "ctflag*****" where * is a number.
folders/73/43/p:The password is: "ctflag*****" where * is a number.
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# 
```
<p>Ternyata password ctflag*****, dimana (*) itu number sebanyak 5 digit, lanjut ke script bruteforce dibawah</p>

```python
from zipfile import ZipFile
import string
import itertools

numbers = string.digits
code = itertools.product(numbers,repeat=5)
zip_file = '1926.zip'
with ZipFile(zip_file) as zf:
    for i in code:
        code = ''.join(i)
        password = "ctflag"+code
        try:
            zf.extractall(pwd=bytes(password,'utf-8'))
            print("[+] password is "+password)
        except:
            pass
```
<p>Hasil bruteforce</p>
<pre>
[+] password is ctflag48625
</pre>
<p>Lanjut ke eksekusi berikutnya</p>

```console
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# unzip 1926.zip 
Archive:  1926.zip
[1926.zip] flag.zip password: ctflag48625
replace flag.zip? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: flag.zip                
  inflating: folders/73/47/p         
  inflating: folders/73/43/p         
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# ls
1926.zip  cracking.py  flag.zip  folders
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# unzip flag.zip 
Archive:  flag.zip
  inflating: flag.txt                
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# cat flag.txt 
RkxBR3ttYXlfdGhlX2JydXRlX2ZvcmNlX2JlX3dpdGhfeW91fQ==
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# cat flag.txt | base64 -d
FLAG{may_the_brute_force_be_with_you}
root@Python:/home/venom/Downloads/_legotroopers.jpg.extracted# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG{may_the_brute_force_be_with_you}
</pre>
