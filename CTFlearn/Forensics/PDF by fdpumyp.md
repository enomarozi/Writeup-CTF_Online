<h1><b>PDF by fdpumyp</h1></b>
<pre>
Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive

Bye

<a href='https://ctflearn.com/challenge/download/957'>File.pdf</a>
</pre>
</b><h3>Solution</h3></b>
<p>Jika kita buka file pdf-nya ternyata hasilnya null, dan eksekusi perintah strings pada file.pdf</p>

```console
root@Python:/home/venom/Downloads# strings -a dontopen.pdf | tail -n 15
== SECRET DATA DONT LOOK AT THIS ==
external:Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==
pin:1234
password:MTIzMVdST05HOWlzamRuUEFTU1dPUkQ=
endstream
endobj
xref
0000149877 00000 n 
13 1
0000150079 00000 n 
trailer
<</Size 14/Root 8 0 R/Info 1 0 R/Prev 149539>>
startxref
150295
%%EOF
root@Python:/home/venom/Downloads# 
```
<p>Dan didapatkan 1 pin dan 2 buah encode base64 yang jika didecode</p>
<pre>
external:Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ== --> CTFlearn{)_1l0w3y0Um00my123}
pin:1234
password:MTIzMVdST05HOWlzamRuUEFTU1dPUkQ= --> 1231WRONG9isjdnPASSWORD
</pre>
<p>flagnya tersebut benar, tetapi saya tidak tau apa gunannya PIN dan password</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{)_1l0w3y0Um00my123}
</pre>
