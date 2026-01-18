<h1>Twitter authentication</h1>
<h3>Description</h3>
<label>A twitter authentication session has been captured, you have to retrieve the password.</label><a href='https://static.root-me.org/reseau/ch3/ch3.pcap'>File</a>
<h3>Solution</h3>
<label>Follow HTTP Stream pada packet, cek Basic Authorization</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# tshark -F libpcap -r ch3.pcap -w convert.pcap 
Running as user "root" and group "root". This could be dangerous.
```
```python3
from scapy.all import rdpcap

file = rdpcap("convert.pcap")
for pkt in file:
    try:
        packet = pkt['Raw'].load.decode().split('\r\n')
        for i in packet:
            print(i)
    except:
        pass
```
```console
┌──(root㉿Kali)-[/home/venom]
└─# echo "dXNlcnRlc3Q6cGFzc3dvcmQ=" | base64 -d
usertest:password
```
<h3>Flag</h3>
<pre>
password
</pre>
