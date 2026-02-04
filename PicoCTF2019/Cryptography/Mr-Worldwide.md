<h1>Mr-Worldwide</h1>
<h3>Description</h3>
<pre>
A musician left us a <a href='https://challenge-files.picoctf.net/c_fickle_tempest/1a43c57b9e3f7bbad97efb8f7fe61fa41ba08e05a059500177635f5eaca370c6/message.txt'>message</a>. What's it mean?
</pre>
<h3>Solution</h3>
<label>Cek coordinate sesuai message.txt</label>

```python3
import requests
import time

list_ = [
    "35.028309, 135.753082","46.469391, 30.740883",
    "39.758949, -84.191605","41.015137, 28.979530",
    "24.466667, 54.366669","3.140853, 101.693207","_",
    "9.005401, 38.763611","-3.989038, -79.203560",
    "52.377956, 4.897070","41.085651, -73.858467",
    "57.790001, -152.407227","31.205753, 29.924526"
]

url = "https://geocode.xyz/"
print("picoCTF{",end='')
for i in list_:
    if i == "_":
        print("_", end="")
        continue

    data = {"locate": i, "ok": "Geocode"}

    while True:
        try:
            r = requests.post(url, data=data, timeout=5)
            text = r.text

            if 'Geocode: <a href="https://geocode.xyz/' in text:
                res = text.split('Geocode: <a href="https://geocode.xyz/')[1][:1]
                print(res, end="")
                break
            else:
                raise ValueError("Response tidak sesuai")

        except Exception:
            time.sleep(5)
print("}",end='')
```
<label>Hasil = picoCTF{KODIAK_ALANKA}, dan final flag = picoCTF{KODIAK_ALASKA}</label>
<h3>Flag</h3>
<pre>
picoCTF{KODIAK_ALASKA}
</pre>
