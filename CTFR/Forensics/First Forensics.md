<h1><b>First Forensics</b></h1>
<pre>
Edit: Mimin baru cek tadi kalo filenya salah upload :(. Maafkan mimin yaah
Baru pertama kali dengan Forensics yaa ? Nah coba cari flag pada sebuah gambar ini.

Challenge --> <a href='https://mega.nz/#!k1wEUIrC!GxdSeRZ3ZapRQPoFqRwfiyhyZoSpFnUnmD-nulltG9M'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Dengan perintah sederhana</p>

```console
root@Python:/home/venom/Downloads# file 2.jpg 
2.jpg: JPEG image data, progressive, precision 8, 712x534, components 3
root@Python:/home/venom/Downloads# strings -a 2.jpg | grep -i CTFR
9acspAPPLCTFR{f1r5t_f0r3ns1c5}
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
CTFR{f1r5t_f0r3ns1c5}
</pre>
