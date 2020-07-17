<h1><b>Ascii art</b></h1>
<pre>
----- BEGIN MESSAGE -----
 xxx     xxx    x   x  xxxxx    xxx     xxx     x   x  xxxxx   xxx    xxx
x   x   x   x  x    x  x       x   x   x   x   x    x  x      x   x  x   x
  xx      xx    xxxxx   xxxx     xx      xx     xxxxx   xxxx    xx   x   x
x   x    x          x      x   x   x   x   x        x      x  x   x  x   x
 xxx    xxxxx      x   xxxxx    xxx     xxx        x   xxxxx   xxx    xxx 
 

----- END MESSAGE -----
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta membaca seluruh ascii art berupa number yang akan di requests ke link https://ringzer0ctf.com/challenges/119/[number], dalam waktu 2 detik</p>

```python3
import requests
import re

number = {"&nbsp;xxx&nbsp;x&nbsp;&nbsp;&nbsp;xx&nbsp;&nbsp;&nbsp;xx&nbsp;&nbsp;&nbsp;x&nbsp;xxx&nbsp;":0,
          "&nbsp;xx&nbsp;&nbsp;x&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;xxxxx":1,
          "&nbsp;xxx&nbsp;x&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;xx&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;xxxxx":2,
          "xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xxxx&nbsp;&nbsp;&nbsp;&nbsp;xxxxxx":5,
          "&nbsp;xxx&nbsp;x&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;xx&nbsp;x&nbsp;&nbsp;&nbsp;x&nbsp;xxx&nbsp;":8,
          "&nbsp;x&nbsp;&nbsp;&nbsp;xx&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;xxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;x":9}

with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    while 1:
        r = session.get("https://ringzer0ctf.com/challenges/119")
        challenge = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', r.text)[0]
        structs = challenge[6:].replace(" ","").split("<br/>")
        structs = [i for i in structs if len(i) > 3]
        data = ""
        structs_data = []
        for i in range(1,len(structs)+1):
            data += structs[i-1]
            if i%5==0:
                structs_data.append(data)
                data = ""
        submit = ""
        for i in structs_data:
            submit +=str(number[i])
        resp = session.get("https://ringzer0ctf.com/challenges/119/"+str(submit))
        if "FLAG-" in resp.text:
            flag = re.findall('<div class="flag">(.*?)</div>',resp.text)[0]
            print(flag)
```

<h3><b>Flag</b></h3>
<pre>
FLAG-ioXVYPyk4sjtsPydks1pph84Gs
</pre>
