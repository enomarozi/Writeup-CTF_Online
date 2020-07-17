<h1><b>Detroit Become Human</b></h1>
<pre>
2 server on my PC became self-aware and are doing some weird sh*t. Try to find something out.

<a href="http://static.beast.sdslabs.co/static/Detroit%20Become%20Human/capture.pcapng">capture.pcapng</a>
</pre>
<h3><b>Solution</b></h3>
<p>Diberikan file ekstensi pcap</p>
<p align="center">
       <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/Detroit%20Become%20Human1.png">
</p>
<p>Lakukan analisa terhadap requests protokol TCP dengan melihat keseluruhan semua TCP Stream, dimana terdapat beberapa potongan huruf yang jika disatukan itu berupa flag</p>
<p align="center">
    <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/Detroit%20Become%20Human2.png">
</p>

```python
from scapy.all import *

pcap = rdpcap("capture.pcapng")
for i in pcap[TCP]:
    try:
        text = str((i[Raw].load)).split('output":')[1].split('", "category":')
        if len(text[0][1:]) < 3:
            print(text[0][2:],end="")
    except:
        pass
````

<h3><b>Flag</b></h3>
<pre>
flag{why_4r3_tw0_pr0gr4mm3s_thr0w1ng_ch4r4ct3r5_4t_34ch_0th3r??}
</pre>
