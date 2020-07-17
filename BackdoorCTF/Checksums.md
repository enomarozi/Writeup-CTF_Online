<h1><b>Checksums</h1></b>
<pre>
You have to authenticate yourself as the administrator in order to proceed.
Unfortunately the username for administrator is not known.
The authentication is based on a crc16 checksum, calculated by the following <a href="http://static.beast.sdslabs.co/static/CHKSUM/code.txt">script</a>.

The checksum is checked against the decimal value of 43160. 
Can you authenticate yourselves? <a href="http://hack.bckdr.in:11006/">Here</a> is the link to the challenge.
</pre>
</b><h3>Solution</h3></b>
<p>Disini kita diberi chellenge tentang CRC checksum, dan kita diberi script generate crc tersebut</p>
<pre>
function crc16($data)
{
  $crc = 0xFFFF;
  for ($i = 0; $i < strlen($data); $i++)
  {
    $x = (($crc >> 8) ^ ord($data[$i])) & 0xFF;
    $x ^= $x >> 4;
    $crc = (($crc << 8) ^ ($x << 12) ^ ($x << 5) ^ $x) & 0xFFFF;
  }
  return $crc;
}
</pre>
<p>Pada soal juga terdapat URL, jika kita akses akan muncul pesan <b>You need to login as an admin user</b>, yang artinya selain admin tidak boleh masuk. Jika kita check 
cookie ketika kita request yaitu UserId=bob. Jadi kita diminta untuk request sebagai admin, bukan berarti kita ganti UserId=bob menjadi UserId=Admin</p>
<p>Pada soal kita juga diberi nilai desimal checksum yaitu 43160 untuk admin, cari nilai suatu string yang memuat nilai desimal tersebut sesuai algoritma program yang sudah diberikan soal</p>

```python
import itertools
import string

letter = string.ascii_lowercase
dictionary = itertools.product(letter,repeat=5)

def crc16_bruteforce(n):
    data = n
    crc = 0xffff
    for i in range(len(data)):
        x = ((crc >> 8) ^ ord(data[i])) & 0xff
        x ^= x >> 4
        crc = ((crc << 8) ^ (x << 12) ^ (x << 5) ^ x) & 0xffff
    if crc == 43160:
        print(crc, data)
for j in dictionary:
    crc16_bruteforce(''.join(j))
```
<p>Hasil Eksekusi program</p>
<pre>
43160 aaazq
43160 aapxa
43160 adntk
43160 akott
43160 apcjq
43160 aprha
43160 auldk
43160 azmdt
43160 bbavr
43160 bbptb
43160 bgnxh
[+]........
</pre>
<p>Kita mendapatkan beberapa value desimal 43160 dan string yang bisa request ke URL sebagai admin. Ambil salah satu string tersebut dan request ke URL dengan edit cookie pada URL sesuai string tersebut, atau dengan perintah curl pada terminal</p>

```console
root@Python:/home/venom/Downloads# curl --cookie "UserId=aaazq" http://hack.bckdr.in:11006/
Flag: 7062fa6a0d2fc311829256085b455778a15f50c4c9861efc33a15b73464b5b51
root@Python:/home/venom/Downloads# 

```

</b><h3>Flag</h3></b>
<pre>
7062fa6a0d2fc311829256085b455778a15f50c4c9861efc33a15b73464b5b51
</pre>
