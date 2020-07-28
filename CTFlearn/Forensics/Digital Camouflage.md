<h1><b>Digital Camouflage</h1></b>
<pre>
We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: 
https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY 
Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

Credit: picoCTF 2017
</pre>
</b><h3>Solution</h3></b>
<p>Buka file dengan wireshark dan perhatikan seluruh stream protokol HTTP</p>

```python
from scapy.all import *

pcap = rdpcap("data.pcap")
for i in pcap[TCP]:
    try:
        data = i[Raw]
        if len(str(data)) < 100:
            print(i[Raw].load)
    except:
        pass
```
<p>Hasil</p>
<pre>
b'HTTP/1.0 200 OK\r\n'
b'HTTP/1.0 200 OK\r\n'
b'HTTP/1.0 200 OK\r\n'
b'userid=hardawayn&pswrd=UEFwZHNqUlRhZQ%3D%3D'
b'HTTP/1.0 200 OK\r\n'
b'HTTP/1.0 200 OK\r\n'
</pre>
<p>Didapatkan userid dan pswrd, decode password dengan base64decode</p>

```console
root@Python:/home/venom/Downloads# echo 'UEFwZHNqUlRhZQ==' | base64 -d
PApdsjRTae
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
PApdsjRTae
</pre>
