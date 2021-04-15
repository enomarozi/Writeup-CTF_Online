<h1><b>First .NET</b></h1>
<pre>
Apa itu .NET Framework ? .NET Framework merupakan sebuah perangkat lunak kerangka kerja yang berjalan terutama pada sistem operasi Microsoft Windows, saat ini .NET Framework umumnya telah terintegrasi dalam distribusi standar Windows. Ada rumor bahwa .NET mudah untuk di Decompile, coba Decompile file dibawah ini.

Challenge --> <a href='https://mega.nz/#!59YwxJSB!kKDYJ1RBNyh5mcPdf3zbSfQX0plwEqKaEvH3KWJdc28'>File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Dengan perintah strings dan grep pada terminal</p>

```console
root@Python:/home/venom/Downloads# strings -a First.NET.exe | grep -i CTFR{
CTFR{d0t_n3t_1s_th3_b35t_fr4m3w0rk}
root@Python:/home/venom/Downloads# 

```
<h3><b>Flag</b></h3>
<pre>
CTFR{d0t_n3t_1s_th3_b35t_fr4m3w0rk}
</pre>
