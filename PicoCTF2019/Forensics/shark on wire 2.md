<h1><b>shark on wire 2</h1></b>
<pre>
We found this <a href='https://2019shell1.picoctf.com/static/dcd259894e0efe9d6e91da2af47e6369/capture.pcap'>packet capture</a>. Recover the flag that was pilfered from the network. 
You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.
</pre>
<h3><b>Solution</b></h3>
<p>Pada soal sebenarnya merupakan bagian dari stego, yaitu flag terdapat dari nilai desimal dari angka ratusan source port ip 10.0.0.66 ke ip 10.0.0.1</p>
<p align='center'>
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/shark%20on%20wire%202_2.png">
</p>
<p>Contohnya pada gambar diatas ada source port 5112 menjadi desimal 112, 5105 menjadi desimal 105, 5099 menjadi desimal 99 dan begitu seterusnya untuk keseluruh paketnya</p>

```python3
from scapy.all import *

pcap = rdpcap("capture1.pcap")
for i in pcap[UDP]:
    try:
        if i[IP].src=="10.0.0.66" and i[IP].dst=="10.0.0.1":
            print(chr(int(str(i[UDP].sport)[1:])),end="")
    except:
        pass
```

<h3><b>Flag</b></h3>
<pre>
picoCTF{p1LLf3r3d_data_v1a_st3g0}
</pre>
