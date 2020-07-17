<h1><b>Hash me please</h1></b>

<pre>
----- BEGIN MESSAGE -----
dGBgAKV8kwTCgJVmxOMPTM54Q26sCu0G1sNr3yqeU9H0Jsc67PMQrHL7zHq22hyUAcctAsxks4b1neYkTA1b7D8wbpp3xONXQQhg8FrqzshNw5YgvPhtjgPkv5eTJSGqyOwwjOMJ6UmtQazcQHv0Nba96fTGXpWl4jIdXlMU5YdMZDOGbawObwO8BxFpNsAHB8KpjmafbeR1IwxJwToyf2xHq2W3knBMlc2vo2Bq6jhEGEe2nsrtkO1BGNuR0WtcYmydeZtb8BGF5Kxj2PDdtuE07ZIYL10AdoDieXkdoQIkq6ujLXm5hRWfHu3jmUJq9cyeZIhepQoFMJPow2kEJ6JgrDqDoZTo2isSQzW6gbBSKh779hBIebPvF5YTVH7NQpwxPitWkVFV2CS1KkzOlf9QbYAXwyBcOXzu6SggEL2wdKnOVNs6TsNUgeHCC9FgW5ASOGZiiSEmtR0evibeAPYHTwamwFsiBT1fqRnzzRLSzBXUJYYaDNInaIzweSFFCwKTeYiEFTn4kaPUZDVthtGh26E7O9Dhwe0A285xRis2j7N8ByrISYQKUkIzkbGGfx77v2vdbN6kLJjc7ALPprq9CYzMZ6i4tf2P8nS90OjBotElUf19xh9Z6yCVvLQORItPVcOMRYd5hIg2O81bf01bpuXK5DpMbJrXL6zsVDn3buVPsNRyDJAT3nuYRKASjSGUO5dAzquALfg4SXsmwS6p5reN1Ewam2V1YYsnfMOQRUKAI3N4LJkH0okSTGS5zDXnsfAxSeezZO0xHDsjdCR4R1MAyuwXYkahqBE8GIyvnoTVSb5VEMPmEsM3N9QBjRJAjeyPNWb0bVMTWIFrklDPDgIggoIq6hQfleVY1XP2IsMv0hNashPVnn2uCAKzIrFTvqInenfNGR8wZMwhTc37qVrTm1iUjOEE4cR9qXMWFLjunGC6Iv3ZhlJudSfmwJRrMyq3m2PREZcRvEO30IT8TstWby8x7POJe4CrXi9r7c9sGNmxm6w5pPSqdRNb
----- END MESSAGE -----
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk hash pesan diatas menggunakan sha512, dan requests ke link https://ringzer0ctf.com/challenges/13/[your_hash] dalam waktu 2 detik</p>

```python3
import requests
import re
import hashlib


with requests.Session() as session:
    payload = {"username":"your-username",#username
               "password":"your-password"}#password
    URL = "https://ringzer0ctf.com/login"
    post = session.post(URL, data=payload)
    r = session.get("https://ringzer0ctf.com/challenges/13")
    challenge = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', r.text)[0]
    hacha = hashlib.sha512(challenge.encode('utf8')).hexdigest()
    resp = session.get("https://ringzer0ctf.com/challenges/13/"+hacha)
    flag = re.findall('<div class="alert alert-info">(.*?)</div>',resp.text)[0]
    print(flag)
```

<h3><b>Flag</b></h3>
<pre>
FLAG-mukgu5g2w932t2kx1nqnhhlhy4
</pre>
