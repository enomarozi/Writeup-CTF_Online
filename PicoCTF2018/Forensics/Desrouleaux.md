<h1><b>Desrouleaux</h1></b>
<pre>
Our network administrator is having some trouble handling the tickets for all of of our incidents. 
Can you help him out by answering all the questions? 
Connect with nc 2018shell.picoctf.com 63299. <a href="https://2018shell.picoctf.com/static/eddbe63bba72a01be6c7c5aba03807bd/incidents.json">incidents.json</a>
</pre>
<b><h3>Solution</h3></b>

```json
{
    "tickets": [
        {
            "ticket_id": 0,
            "timestamp": "2015/07/03 19:00:05",
            "file_hash": "8ac844ab88c6dd7a",
            "src_ip": "186.120.220.162",
            "dst_ip": "27.125.245.207"
        },
        {
            "ticket_id": 1,
            "timestamp": "2015/08/28 17:24:05",
            "file_hash": "848345bee7363104",
            "src_ip": "186.120.220.162",
            "dst_ip": "99.188.121.177"
        },
        {
            "ticket_id": 2,
            "timestamp": "2017/09/01 01:24:25",
            "file_hash": "f92bd3ceb90c9aa9",
            "src_ip": "43.113.162.172",
            "dst_ip": "157.237.76.10"
        },
        {
            "ticket_id": 3,
            "timestamp": "2017/01/18 23:07:48",
            "file_hash": "67114cd4381339b2",
            "src_ip": "0.209.51.5",
            "dst_ip": "89.174.138.244"
        },
        {
            "ticket_id": 4,
            "timestamp": "2017/01/11 19:56:07",
            "file_hash": "ea55c71517cccde5",
            "src_ip": "34.104.29.49",
            "dst_ip": "124.92.82.238"
        },
        {
            "ticket_id": 5,
            "timestamp": "2016/04/28 08:30:35",
            "file_hash": "626d36347ebbdf18",
            "src_ip": "43.113.162.172",
            "dst_ip": "25.63.198.8"
        },
        {
            "ticket_id": 6,
            "timestamp": "2016/06/15 21:50:09",
            "file_hash": "4567c657527aecdc",
            "src_ip": "186.120.220.162",
            "dst_ip": "89.174.138.244"
        },
        {
            "ticket_id": 7,
            "timestamp": "2015/02/07 03:55:46",
            "file_hash": "72e8c7bec515d8f2",
            "src_ip": "34.104.29.49",
            "dst_ip": "99.188.121.177"
        },
        {
            "ticket_id": 8,
            "timestamp": "2016/07/02 05:57:54",
            "file_hash": "848345bee7363104",
            "src_ip": "186.120.220.162",
            "dst_ip": "27.125.245.207"
        },
        {
            "ticket_id": 9,
            "timestamp": "2015/05/16 18:48:45",
            "file_hash": "50ecac4733206868",
            "src_ip": "40.91.251.68",
            "dst_ip": "99.188.121.177"
        }
    ]
}
```
<p>Analisa seluruh data json file, dan jawab pertanyaan pada <b>nc 2018shell.picoctf.com 63299</b> sesuai analisa</p>
<p>Pertanyaan-1, Paket source yang sering muncul</p>
<p>Pertanyaan-2, Jumlah IP yang berbeda yang menuju source 186.120.220.162</p>
<p>Pertanyaan-3, Jumlah seluruh file_hash dibagi (Jumlah seluruh file_hash - jumlah file_hash yang sama)</p> 

```python
import json

Question1 = []
Question2 = []
Question3 = []
with open('incidents (1).json') as dat_analys:
    data = json.load(dat_analys)
    for i,j in data.items():
        for k in range(len(j)):
            Question1.append(j[k]["src_ip"])
            Question2.append(j[k]["src_ip"]+"  "+j[k]["dst_ip"])
            Question3.append(j[k]["file_hash"])

#Question-1
print("\nQuestion-1")            
for i in set(Question1):
    dat = Question1.count(i)
    print(i,"--> Total",dat)
print("\nQuestion-2")
#Question-2
for i in set(Question2):
    dat = Question2.count(i)
    print(i,"--> Total",dat)    
#Question-3
print("\nQuestion-3")
print(round(len(Question3)/len(set(Question3)),2)) 
```
<p>Hasilnya</p>
<pre>
<b>Question-1</b>
34.104.29.49 --> Total 2
0.209.51.5 --> Total 1
43.113.162.172 --> Total 2
186.120.220.162 --> Total 4
40.91.251.68 --> Total 1

<b>Question-2</b>
43.113.162.172  157.237.76.10 --> Total 1
186.120.220.162  27.125.245.207 --> Total 2
186.120.220.162  99.188.121.177 --> Total 1
34.104.29.49  99.188.121.177 --> Total 1
186.120.220.162  89.174.138.244 --> Total 1
43.113.162.172  25.63.198.8 --> Total 1
34.104.29.49  124.92.82.238 --> Total 1
40.91.251.68  99.188.121.177 --> Total 1
0.209.51.5  89.174.138.244 --> Total 1
<b>Question-3</b>
1.11
</pre>
<p>Jawab pertanyaan sesuai yang didapatkan soal dan hasil program</p>

```console
root@Python:/home/venom/Downloads# nc 2018shell.picoctf.com 63299
You'll need to consult the file `incidents.json` to answer the following questions.


What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.
186.120.220.162
Correct!


How many unique destination IP addresses were targeted by the source IP address 186.120.220.162?
3
Correct!


What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places.
1.11
Correct!


Great job. You've earned the flag: picoCTF{J4y_s0n_d3rUUUULo_23fa6fa6}
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
picoCTF{J4y_s0n_d3rUUUULo_23fa6fa6}
</pre>
