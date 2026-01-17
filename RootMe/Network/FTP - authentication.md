<h1>FTP - authentication</h1>
<h3>Description</h3>
<label>An authenticated file exchange achieved through FTP. Recover the password used by the user.</label>
<h3>Solution</h3>
<label>Check Password di Follow TCP Stream</label>

```python3
from scapy.all import rdpcap

file = rdpcap("convert.pcap")
for pkt in file:
    try:
        if b"PASS" in pkt['Raw'].load:
            print(pkt['Raw'].load.decode().split(' ')[1][:-2])
    except:
        pass
```
<h3>Flag</h3>
<pre>
cdts3500
</pre>
