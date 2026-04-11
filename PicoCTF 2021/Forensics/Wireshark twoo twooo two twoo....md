<h1>Wireshark twoo twooo two twoo...</h1>
<h3>Description</h3>
<pre>
Can you find the flag?
<a href='https://challenge-files.picoctf.net/c_wily_courier/ccf87403213b438f1ae79d8513cc5f1104d9f3048857eadba67e07c7233502e5/shark2.pcapng'>shark2.pcapng</a>
</pre>
<h3>Solution</h3>
<label>Check query paket DNS</label>

```python3
from scapy.all import *
from base64 import b64decode

packets = rdpcap("shark2.pcapng")
result = ''
for pkt in packets:
    if pkt.haslayer(DNS):
        if "amazonaws" in pkt[DNS].summary() and pkt[IP].dst == "18.217.1.57":
            result += pkt[DNSQR].qname.decode().split('.')[0]

flag = b64decode(result.encode())
print(flag.decode())
```
<h3>Flag</h3>
<pre>
picoCTF{dns_3xf1l_ftw_deadbeef}
</pre>
