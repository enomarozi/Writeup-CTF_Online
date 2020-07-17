<h1><b>Someone steal my flag again</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/2a3a751a5785ac4f1daa4c27c1ff00aa.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p align='center'>
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/Steal_again1.jpg">
</p>

<p>Sesuai Challenge sebelumnya <a href="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Ringzer0CTF-Someone%20steal%20my%20flag!.md">Someone steal my flag!</a>
string Flag terdapat disetiap ICMP packet</p>
<p>Maka, disini saya ekstrak string yang terdapat pada ICMP paket juga, dan hasilnya</p>
<pre>
['eb', '11', 'd6', '0a', '9f', '10', 'cc', '59']
['eb', '11', 'd6', '0a', '9f', '10', 'cc', '59']
['c6', 'd1', 'c5', 'c1', 'c7', '84', 'd6', 'cb']
['c6', 'd1', 'c5', 'c1', 'c7', '84', 'd6', 'cb']
['0a', '3d', '0d', '3f', '01', '35', '10', '32']
['0a', '3d', '0d', '3f', '01', '35', '10', '32']
['47', 'e0', '07', 'ac', '60', 'c0', '67', 'cb']
['47', 'e0', '07', 'ac', '60', 'c0', '67', 'cb']
['5e', 'f6', '40', 'f1', '4b', '88', '42', 'f2']
['5e', 'f6', '40', 'f1', '4b', '88', '42', 'f2']
['d8', 'f2', 'ab', '8b', 'ad', '80', 'e0', 'ad']
['d8', 'f2', 'ab', '8b', 'ad', '80', 'e0', 'ad']
['f7', 'd3', '95', 'ae', '93', 'd0', 'a9', 'e6']
['f7', 'd3', '95', 'ae', '93', 'd0', 'a9', 'e6']
['98', '6b', '98', '6b', '98', '17', 'ed', '03']
['98', '6b', '98', '6b', '98', '17', 'ed', '03']
</pre>
<p>Semua random string saya convert ke hexa dan ternyata panjangnya sama, yang kemungkinan ini merupakan string hasil encrypt, selanjutnya saya coba mencari key 
untuk mendecrypt string tersebut yang ternyata terdapat pada ICMP sequence number (BE)</p>
<p align="center">
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/Steal_again2.jpg">
</p>
<p>Berikut hasil ekstrak key</p>
<pre>
['bf', '79']
['bf', '79']
['b5', 'a4']
['b5', 'a4']
['64', '5b']
['64', '5b']
['26', '8c']
['26', '8c']
['73', 'c2']
['73', 'c2']
['9a', 'c2']
['9a', 'c2']
['c1', '9f']
['c1', '9f']
['a8', '5b']
['a8', '5b']
</pre>
<p>Terakhir, saya mencoba decrypt message dengan key</p>

```python
from scapy.all import *

pcap = rdpcap("stealed_8670c3ef00baa6aba581cab446d456ab.pcap")
for i in pcap[ICMP]:
    try:
        message_enc = i[Raw].load
        if len(message_enc) == 8:
            message_enc = [hex(i)[2:].rjust(2,"0") for i in message_enc]
        key_dat = i.seq
        if key_dat > 1000:
            key_dat = hex(key_dat)[2:]
            key_dat = [key_dat[:i][-2:] for i in range(2,len(key_dat)+2,2)]
            key_dec = key_dat*4
            for i,j in zip(message_enc,key_dec):
                print(chr(int(i,16)^int(j,16)),end="")
    except:
        pass
```
<p>dan hasilnya</p>
<pre>
This is This is super cosuper confidentinfidential! FLAGal! FLAG-4338J10-4338J10B01I7BzoB01I7Bzo6LT1ROhy6LT1ROhy00000LEX00000LEX
</pre>
<p>Disana terdapat banyak perulangan string, dan padding yaitu 00000, filter semuanya dan dapatkan flag</p>
<h3><b>Flag</b></h3>
<pre>
FLAG-4338J10B01I7Bzo6LT1ROhyLEX
</pre>
