<h1><b>Troll Face</b></h1>
<pre>
Didalam gambar ini terdapat teks yang tersembunyi, akan tetapi kalian harus menggunakan tools agar dapat membacanya. Toolsnya bernama z....

Challenge --> <a href='https://mega.nz/file/dth2zZqJ#eq_VqZTUyHYKTEruOxT1bvkElDsj0xcRXcjkPOe04Hs'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Periksa pada RGB index 1 LSB dengan tool stegsolve atau zsteg</p>

```console
root@Python:/home/venom/Downloads# zsteg troll.png | grep -i CTFR
b1,rgb,lsb,xy       .. text: "24:CTFR{st3g4n0_1s_aw3s0me}"
root@Python:/home/venom/Downloads# 
```
<p>Atau Jalankan Script Python dibawah</p>

```python
import cv2

brk = 0
image = cv2.imread('troll.png')
list_bin = ''
for i in image:
    for j in i:
        for k in j[::-1]:
            brk += 1
            if brk < 217:
                list_bin += bin(k)[-1:]
            else:
                break
result = ''.join([chr(int(list_bin[:i][-8:],2)) for i in range(8,len(list_bin)+8,8)])
print(result) #CTFR{st3g4n0_1s_aw3s0me}

```
<h3><b>Flag</b></h3>
<pre>
CTFR{st3g4n0_1s_aw3s0me}
</pre>
