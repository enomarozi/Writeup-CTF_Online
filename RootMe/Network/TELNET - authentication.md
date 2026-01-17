<h1>TELNET - authentication</h1>
<h3>Decription</h3>
<label>Find the user password in this TELNET session capture.</label>
<h3>Solution</h3>
<label>Convert pcapng ke pcap</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# tshark -F libpcap -r ch2.pcap -w convert.pcap
```

```python
from scapy.all import rdpcap

file = rdpcap("convert.pcap")
for pkt in file:
    try:
        print(pkt['Raw'].load)
    except:
        pass
```
<pre>
Username : ffaakkee
Password : user
</pre>
<h3>Flag</h3>
<pre>
user
</pre>
