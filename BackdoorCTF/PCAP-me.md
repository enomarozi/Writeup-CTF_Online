<h1><b>PCAP-me</b></h1>
<p>Diberikan 1 file pcap</p>
<p align="center">
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/pcapNG.jpg">
</p>
<h3><b>Solution</b></h3>
<p>Pada file pcap itu sepertinya penyadapan(sniffing) protocol HTTP sederhana, dan disana ada beberapa kejadian requests login yang didapatkan username dan passwordnya sebagai berikut</p>
<pre>
uname=admin&psw=admin
uname=admin&psw=admin1
uname=admin&psw=people
uname=admina&psw=admind
uname=admin&psw=proceedfurther
uname=admin&psw=givememyflag
uname=heypeople&psw=fakeflagflagy
uname=flag&psw=flagflag
uname=please+see+the+pcap+file+carefully&psw=see+the+pcapcarefully
uname=pcappcap&psw=pcappcap
uname=flag&psw=CTF{fake_flag_heheh}
</pre>
<p>Selanjutnya kita mencari URL login dari proses authentifikasi tersebut, filter dengan pencarian dns, dan lihat pada DNS queris, disana terdapat URLnya</p>
<p align="center">
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/pcapNG1.jpg">
</p>
<p>Terakhir, coba semua username dan password yang didapatkan untuk login pada URL <a href="http://n00bctf.herokuapp.com/">http://n00bctf.herokuapp.com</a></p>
<p align='center'>
  <img src="https://github.com/enomarozi/CTF-Writeup/blob/master/Wireshark/Images/pcapNG2.jpg">
</p>

```python3
import requests
import re

username = ["admin","admin","admin","admina","admin","admin","heypeople",
            "flag","please+see+the+pcap+file+carefully","pcappcap","flag"]
password = ["admin","admin1","people","admind","proceedfurther","givememyflag",
            "fakeflagflagy","flagflag","see+the+pcapcarefully","pcappcap",
            "CTF{fake_flag_heheh}"]

url = "http://n00bctf.herokuapp.com"
for user,passwd in zip(username,password):
    data = {'uname':user,
            'psw':passwd
            }
    resp = requests.post(url,data=data).text
    if "CTF{" in resp:
        flag = re.findall('Here is your flag (.*?)<html>',resp)[0]
        print(flag)

```
<h3><b>Flag</b></h3>
<pre>
CTF{1_l0v3_wir3shark_4nd_pc4p_f1les}
</pre>
