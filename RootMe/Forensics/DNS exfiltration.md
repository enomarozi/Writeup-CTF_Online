<h1>DNS exfiltration</h1>
<h3>Description</h3>
<label>Find the exfiltrated data.</label><a href='https://static.root-me.org/forensic/ch21/ch21.pcap'>File</a>
<h3>Solution</h3>
<label>Cek setiap query DNS paket ada raw bytes header image PNG</label>

```python3
from scapy.all import *

pkts = rdpcap('ch21.pcap')
result = b''
for pkt in pkts:
    if pkt['IP'].src == "192.168.56.101":
        byte_dns = pkt['DNS'].qd.qname.split(b'jz')[0].replace(b'.',b'')[18:]
        result += byte_dns

header = b'89504e470d0a1a0a'
cleaned = header+result.split(header)[1]
with open('image.png','wb') as f:
    f.write(bytes.fromhex(cleaned.decode()))
f.close()
```
<label>Jika berhasil tampilkan gambar PNG</label>
<h3>Flag</h3>
<pre>
FLAG{ExF1ltr4tion_15-s0_Bl4ck}
</pre>
