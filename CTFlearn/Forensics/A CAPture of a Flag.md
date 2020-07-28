<h1><b>A CAPture of a Flag</h1></b>
<pre>
This isn't what I had in mind, when I asked someone to capture a flag... can you help? 
You should check out WireShark. 
https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4
</pre>
</b><h3>Solution</h3></b>
<p>Perhatikan seluruh protokol HTTP, khususnya pada stream ke-5 nomor 247. Disana terdapat encode base64, decode ke plaintext</p>
<p align='center'>
<img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/CaptuaFlag.jpg'>
</p>

```console
root@Python:/home/venom/Downloads/source# echo 'ZmxhZ3tBRmxhZ0luUENBUH0=' | base64 -d
flag{AFlagInPCAP}
root@Python:/home/venom/Downloads/source# 
```
</b><h3>Flag</h3></b>
<pre>
flag{AFlagInPCAP}
</pre>
