<h1><b>The Keymaker</h1></b>
<pre>
Jpeg comments can be very interesting.

<a href="https://ctflearn.com/challenge/download/912">The-Keymaker.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file JPG, pertama lakukan sesuai perintah soal yaitu lihat comment</p>

```console
Comment                         : CTFlearn{TheKeymakerIsK00l}.
Comment                         : b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg.LW91dCBmbGFnIC1iYXNlNjQKCml2IGRvZXMgbm90IGluY2x1ZGUgdGhlIG1hcmtlciBvciBsZW5n.dGggb2YgU09GMAoKa2V5IGRvZXMgbm90IGluY2x1ZGUgdGhlIFMwUyBtYXJrZXIKCg==.
Comment                         : mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY.
```
<p>Disana terdapat Flag, tetapi salah. Dan terdapat 2 encode base64</p>
<p>Base64 Pertama</p>

```console
root@Python:/home/venom/Downloads# echo 'b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMgLW91dCBmbGFnIC1iYXNlNjQKCml2IGRvZXMgbm90IGluY2x1ZGUgdGhlIG1hcmtlciBvciBsZW5ndGggb2YgU09GMAoKa2V5IGRvZXMgbm90IGluY2x1ZGUgdGhlIFMwUyBtYXJrZXIKCg==' | base64 -d
openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc -out flag -base64

iv does not include the marker or length of SOF0

key does not include the S0S marker

root@Python:/home/venom/Downloads# 
```
<p>Base64 Kedua</p>

```console
root@Python:/home/venom/Downloads# echo "mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY" | base64 -d
�kZHx@��i,ǩ�P�ߵ]�mfN�চ������蛜�J�RX�'
root@Python:/home/venom/Downloads# 
```
<p>Base64 pertama itu merupakan intruksi soal, yaitu diencrypt dengan AES_CBC 256 bit dengan IV-nya adalah nilai SOF0 dari image JPG tanpa maker dan length dari SOF0, dan untuk 
Key-nya itu terdapat pada S0S file JPG tidak termasuk makernya</p> 
<p>Sedangkan base64 kedua itu merupakan flag ter-encrypt</p>
<p>SOF0 itu merupakan bagian SOF/SOI dari file image dengan maker 0xc0, atau diakhirnya terdapat 0xff menjadi 0xffc0</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/S0f0.jpg'>
</p>
<p>Seperti ketentuan IV yaitu tidak termasuk maker dan length dari SOF0, jadi IV-nya yaitu</p>
<pre>
IV = 0800be00c803011100021101031101ff
</pre>
<p>Dan untuk Key-nya terdapat pada SOI file JPG</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/SOI.jpg'>
</p>
<p>Sesuai ketentuan key tidak termasuk maker dari SOI, jadi Key yaitu </p>
<pre>
Key = 000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952
</pre>
<p>Selanjutnya proses decrypt dengan openssl sesuai Key dan IV yang telah didapatkan</p> 

```console
root@Python:/home/venom/Downloads# echo "mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY" | base64 -d > flag.enc
root@Python:/home/venom/Downloads# openssl enc -d -aes-256-cbc -iv 0800be00c803011100021101031101ff -K 000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952 -in flag.enc -out flag
root@Python:/home/venom/Downloads# cat flag
CTFlearn{Ne0.TheMatrix}        
root@Python:/home/venom/Downloads# 
```
<p>Atau dengan script python dibawah</p>

```python
import base64
from Crypto.Cipher import AES
import hashlib

msg = "mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY"
Key = "000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952"
IV = "0800be00c803011100021101031101ff"

key_dec = bytes.fromhex(Key)
IV = bytes.fromhex(IV)
encryption = base64.b64decode(msg)
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(decrypt)

```
<p>Hasil Program</p>
<pre>
b'CTFlearn{Ne0.TheMatrix}        \n\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
</pre>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{Ne0.TheMatrix}    
</pre>
