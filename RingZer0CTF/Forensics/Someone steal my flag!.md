<h1><b>Someone steal my flag!</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/bdc8c86f1c082715762b4d9cb755c4c7.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<h1><b>Someone steal my flag!</b></h1>
<p>Diberikan 1 file ekstensi pcap, yang terdapat 783 packet yang masing-masing berbeda protocol</p>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/Someone%20steal%20my%20flag!.png">
</p>
<p>Dari banyaknya paket data tersebut, terdapat nilai hexa yang mencurigakan itu dari ICMP packet, yaitu nilai hexa yang memungkinkan mencetak nilai ascii 0-9,a-z dan A-Z.
lakukan filter pada paket ICMP, IP source dan IP destination pada kolom filter.</p>
<p><b>icmp && ip.src==192.168.191.129 && ip.dst==192.168.191.128</b></p> 
<p>Untuk detail packet dapat dilihat pada jendela detail packet --> layer ICMP yang tepatnya pada DNS query name</p>
<p align="center">
  <img src="https://github.com/enomarozi/RSA-CTF-Writeup/blob/master/Wireshark/Images/Someonesteal.png">
</p>
<p>Disini kita bisa menyelesaikannya dengan manual, tetapi itu akan memakan waktu. Dan saya melakukannya dengan script python dibawah ini.</p>

```python
from scapy.all import *
import base64

pcap = rdpcap("6338c3e33776b9844814d2daadf208bc.pcap")
result = []
for i in pcap[ICMP]:
    try:
        if(i[IP].src=="192.168.191.129" and i[IP].dst == "192.168.191.128"):
            a = str(i[IP][DNS])
            split1 = a.split("\\x10")[1]
            split2 = split1.split("\\x03192")
            result.append(split2[0])
    except:
        pass
flag = ""
for i in range(0,len(result),2):
    flag += result[i]
print(base64.b64decode(bytes.fromhex(flag+"57564a330a")))
```

<h3><b>Flag</b></h3>
<pre>
FLAG-FT47cMX26pWyFSI6RPWaSr5YRw
</pre>
