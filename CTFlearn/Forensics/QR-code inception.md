<h1><b>QR-code inception</h1></b>
<pre>
My boss read in a magazine that people in China are using QR-codes to pay goods. 
e thinks it is the future and he wants QR-codes everywhere from the company website to his coffee machine. 
To meet my new boss requirements, he asked me to write an application generating QR-code. 
I spent days on it as scope always changes.

Thanks god, the week-end is there and I can forget about these QR-codes. 
Yesterday, I watched "Inception" by Christopher Nolan, it was great but the night after did not turn well and I got strange dreams.

I am sharing with you a picture I took during my dream (yes I can because I am a hacker). Welcome to my QR-code inception...

<a href='https://ctflearn.com/challenge/download/920'>inception.png</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file PNG QR-Code dengan size 8700x8700, jika diperhatikan ditengah pixel hitam atau putih juga terdapat Encode QR-Code yang memuat 1 string</p>
<p>Tetapi disini saya menyelesaikannya dengan manual yang memakan waktu lama dengan bantuan QR-Code Reader android, maka didapatkan string</p>
<pre>
iVBORw0KGgoAAAANSUhEUgAAACUAAAAlAQAAAADt5R2uAAAAsUlEQVR4nGP4DwQ/GDDJD9IGDhUM369x3q9g+BJgdBFIRvQEAsnwKUD290uzgOIfREOBav5/jgSq/3T2sQtQb865mgqGn46fGn4wfLE/eqaC4VN/1jkgmVFdBdR7sripguGPMrfeD4ZvUhO1fjD8+P73JlAl58YDQPEfGxf/YPjuFcQINPOLSRHQDULCQUCRG6olQL0xh9lBLpkXAVQfM6sU6IYrr78B1Yga2mFzP5gEAB2SgeETXS+JAAAAAElFTkSuQmCC
</pre>
<p>Ternyata encode base64, jika didecode itu merupakan file PNG ukuran kecil, decode string tersebut dalam bentuk file dan hasilnya</p>
<p align='cente'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/decoded-20200605022319.png'>
</p>
<p>Ternyata masih merupaaan QR-Code tetapi ini akan memuat suatu text/flag karena dapat dilihat dari pola QR-Codenya, Decode QR pada websiet <a href='https://zxing.org/w/decode'>QR-Code</a></p>

</b><h3>Flag</h3></b>
<pre>
CTFlearn{Y0u_4re_in_QR-cOd3_l1mb0}
</pre>
