<h1>Hangovers and more: Bacon<b></h1></b>
<pre>
VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!

We hijack the Bacon Bacon Truck in San Francisco!

The cure for your worst
Hangovers and more: Bacon
True: Science says so
</pre>
</b><h3>Solution</h3></b>
<p>Ambil setiap uppercase dan lowercase pada pesan, convert ke B jika upper dan A jika lower, itu merupakan encode baconian cipher</p>

```python
message = "VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!"
bacon = ""
for i in message:
    if i.isupper():
        bacon += "B"
    elif i.islower():
        bacon += "A"
print(bacon)

```
<p>Hasil</p>
<pre>
BAABBAABBBAABAAAABABABABBAAAAAAABBAABAAABAABAAAAABAAAAAAAABAABBBAABBABAAAAAABBABAAABBABAABAAAAAAAABAABABAAAABBAAAAAABBABABAAAAABAAABABBBAABAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
</pre>
<p>Decode pada website <a href="http://rumkin.com/tools/cipher/baconian.php">rumkin-cipher</a>, dan hasilnya</p>
<pre>
THEFLAGISBACONANDJACKDANIELSACAAAAAAAAAAAAA
</pre>
</b><h3>Flag</h3></b>
<pre>
baconandjackdaniels
</pre>
