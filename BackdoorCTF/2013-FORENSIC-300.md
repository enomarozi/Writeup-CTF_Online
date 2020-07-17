<h1><b>2013-FORENSIC-300</b></h1>
<pre>
H4x0r has now learnt that simple text authentications are not the in thing today. 
Also since voice authentication is all the rage nowadays thanx to siri, he decided to get one for his castle. 
But he messed it big time and now has a audio file which he himself can't seem to decipher. 
So now he needs your help to get into his own castle.

You can find the file <a href='http://static.beast.sdslabs.co/static/2013-FORENSIC-300/siri_audio.zip'>here</a>.

Find the hidden passphrase, the flag is the SHA-256 of the MD5 of the passphrase.
</pre>
<h3><b>Solution</b></h3>
<p align='center'>
  <img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/2013-FORENSIC-300.jpg">
</p>
<p>Perhatikan amplitudo gelombang, disana terdapat 2 perbedaan amplitudo yaitu</p>

<p>1.<img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/2013-FORENSIC-300_1.jpg"></p>
<p>2.<img src="https://github.com/enomarozi/BackdoorCTF_Writeup/blob/master/Images/2013-FORENSIC-300_2.jpg"></p>
<p> Pada gambar pertama itu melambangkan binary 0, dan gambar kedua binary 1, lalu salin semua binary disetiap amplitudo maka didapatkan 
<b>011000100110000101101011011001000110111101110010</b>, Terakhir decode seluruh binary ke text</p>

```python
amp_analys = ["01100010","01100001","01101011",
               "01100100","01101111","01110010"]
for i in amp_analys:
    print(chr(int(i,2)),end="")
```
<h3><b>Flag</b></h3>
<pre>
bakdor
</pre>
