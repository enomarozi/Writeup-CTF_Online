<h1>shark on wire 1</h1>
<pre>
We found this packet <a href='https://2019shell1.picoctf.com/static/ae9ca8cff43ed638ed5d137f9ece7455/capture.pcap'>capture</a>. 
Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.
</pre>
<h3>Solution</h3>
<p>Terdapat ada beberapa flag, tetapi hanya ada 1 flag yang benar yaitu ip_src 10.0.0.2 ke ip_dst 10.0.0.12 dan protocol UDP stream</p>
<p align="center">
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/shark%20on%20wire%201_2.png">
</p>

```python3
from scapy.all import *

pcap = rdpcap("capture.pcap")
for i in pcap[UDP]:
    try:
        if i[IP].src=="10.0.0.2" and i[IP].dst=="10.0.0.12":
            print((i[Raw].load).decode("utf-8"),end="")
    except:
        pass
```
<h3>Flag</h3>
<pre>
picoCTF{StaT31355_636f6e6e}
</pre>
