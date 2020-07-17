<h1><b>Find the right word</b></h1>
<pre>
----- BEGIN WORDS -----
gougers,determinative,utesseatn,parleys,cretinous,phenocopy,chaufers
----- END WORDS -----
</pre>
<p>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk unscramble seluruh word english ke word yang benar, lalu requests word ke link https://ringzer0ctf.com/challenges/126/[string] dengan comma sebagai pemisah dalam waktu 2 detik</p>


```python3
import requests
import re

with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    while 1:
        r = session.get("https://ringzer0ctf.com/challenges/126")
        challenge = re.findall('----- BEGIN WORDS -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END WORDS -----', r.text)[0].split(",")
        right_word = ""
        for i in range(len(challenge)):
            get_word = requests.get("http://www.allscrabblewords.com/unscramble/"+challenge[i])
            word = re.findall("Words made by unscrambling the letters in (.*?) | Word Decoder for ",get_word.text)
            right_word += word[1]+","
            
        resp = session.get("https://ringzer0ctf.com/challenges/126/"+right_word[:-1])
        if "FLAG-" in resp:
            print(resp.text)
        else:
            print("Lose --> "+right_word[:-1])
```

<h3><b>Flag</b></h3>
<pre>
Redacted
</pre>
