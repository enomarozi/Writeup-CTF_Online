```python3
from scapy.all import *

pcap = rdpcap("myNetworkTraffic.pcap")
data = {}
flag = ''
for i in pcap[TCP]:
    try:
        if i[IP].src=="192.168.0.2" and i[IP].dst=="192.168.1.2":
            if i.time >= 1741231902.550000:
                part_flag = base64.b64decode(i[Raw].load).decode("utf-8")
                data.update({part_flag:i.time})
    except:
        pass
sorted_flag = dict(sorted(data.items(), key=operator.itemgetter(1)))
for part in sorted_flag.items():
    print(part[0],end='')

```
