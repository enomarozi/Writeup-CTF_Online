<h1><b>ShahOfGimli</h1></b>
<pre>
That still only counts as one!

<a href='https://ctflearn.com/challenge/download/958'>ShahOfGimli.jpg</a>
</pre>
</b><h3>Solution</h3></b>
<p>Lihat comment file dengan exiftool, disana terdapat banyak encode base64 dan periksa satu persatu</p>

```console
root@Python:/home/venom/Downloads# exiftool ShahOfGimli.jpg -a | grep -i comment
Comment                         : CTFlearn{Gimli_Was_Part_Of_The_Fellowship_Of_The_Ring}.
Comment                         : Q1RGbGVhcm57R2ltbGkuSXMuQS5Ed2FyZn0KCldobyBpcyBHaW1saT8gIFlvdSBjYW4gbGVhcm4g.bW9yZSBhYm91dCBHaW1saSBoZXJlOgpodHRwczovL2xvdHIuZmFuZG9tLmNvbS93aWtpL0dpbWxp.Cmh0dHBzOi8vZW4ud2lraXBlZGlhLm9yZy93aWtpL0dpbWxpXyhNaWRkbGUtZWFydGgpCgpUaGlz.IGNoYWxsZW5nZSBpcyBiYXNlZCBvbiBoYXNoIGFsZ29yaXRobXMgYW5kIGVuY3J5cHRpb24uCgpJ.IGFtIHVzaW5nIE9QRU5TU0wgdjEuMS4xIHRvIGNyZWF0ZSB0aGlzIGNoYWxsZW5nZS4KCkhlcmUg.aXMgYSByZWZlcmVuY2UgZm9yIHVzaW5nIGhhc2ggY2FsY3VsYXRpb25zIHdpdGggT1BFTlNTTDoK.aHR0cHM6Ly93d3cub3BlbnNzbC5vcmcvZG9jcy9tYW4xLjEuMS9tYW4xL29wZW5zc2wtZGdzdC5o.dG1sCgpJZiB5b3UgYXJlIGEgUHl0aG9uIGNvZGVyLCBQeXRob24gcHJvdmlkZXMgYSBoYXNoaW5n.IGxpYnJhcnkgeW91IG1pZ2h0IGZpbmQgdXNlZnVsOgpodHRwczovL2RvY3MucHl0aG9uLm9yZy8z.L2xpYnJhcnkvaGFzaGxpYi5odG1sCgpJZiB0aGlzIGNoYWxsZW5nZSBoYXMgeW91IHdvbmRlcmlu.ZyB3aGF0IHRvIGRvIG5leHQsIHBsZWFzZSB0cnkgbXkgb3RoZXIgY2hhbGxlbmdlcwp0aGF0IGFy.ZSB3b3J0aCBmZXdlciBwb2ludHMuICBUaGUgbW9yZSBwb2ludHMsIHRoZSBtb3JlIGRpZmZpY3Vs.dCB0aGUgY2hhbGxlbmdlLgoKSWYgeW91IGFyZSBuZXcgdG8gQ1RGIGFuZC9vciBub3QgcXVpdGUg.c3VyZSBob3cgdG8gc29sdmUgdGhpcyBjaGFsbGVuZ2UsCnlvdSBzaG91bGQgcHJvYmFibHkgdHJ5.IHRoZXNlIG90aGVyIGNoYWxsZW5nZXMgZmlyc3QgaW4gdGhpcyBvcmRlcjoKUnViYmVyRHVjawpT.bm93Ym9hcmQKUGlrZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpBZnRlciBzb2x2aW5nIHRoaXMgU2hh.aE9mR2ltbGkgY2hhbGxlbmdlLCB0aGVuIHRyeToKSGFpbENhZXNhcgpNb3VudGFpbk1hbgpLZXlN.YWtlcgpWYXJnYXNJc2xhbmQKCk15IFR3aXR0ZXIgRE0ncyBhcmUgb3BlbiBAa2Nib3dodW50ZXIu.CgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgpUaGUgdGhpcmQgY29tbWVudCBibG9jayBp.cyBlbmNyeXB0ZWQgd2l0aCBBRVMgQ0JDIGVuY3J5cHRpb24gdXNpbmcgdGhlIGZvbGxvd2luZyBr.ZXk6CnNoYTI1NiBoYXNoIG9mIHRoZSBzdHJpbmcgIkNURmxlYXJuIgoKTm90ZSB0aGF0IHRoZSBj.b21tZW50IGJsb2NrIGlzIGFsc28gYmFzZTY0IGVuY29kZWQKVGhlcmUgaXMgbm8gaXYgYnV0IHlv.dSBuZWVkIHRvIGRldGVybWluZSBob3cgdG8gZXhwcmVzcyB0aGlzIG1hdGhlbWF0aWNhbGx5CgpJ.ZiB5b3UgYXJlIG5ldyB0byBlbmNyeXB0aW9uIGFuZCBoYXNoIGFsZ29yaXRobXMgaGVyZSBpcyBh.IGdvb2QgcGxhY2UgdG8gc3RhcnQ6Cm9wZW5zc2wgZW5jIC1oZWxwCm9wZW5zc2wgZGdzdCAtaGVs.cApzaGEyNTZzdW0KCk9mIGNvdXJzZSBHb29nbGUgaXMgeW91ciBmcmllbmQgKGlmIHlvdSBkb24n.dCBtaW5kIHRoZW0gcmVjb3JkaW5nIGFsbCB5b3VyIG9ubGluZSBhY3Rpdml0eSkKCmh0dHBzOi8v.d2lraS5vcGVuc3NsLm9yZy9pbmRleC5waHAvRW5jIGlzIGEgZ29vZCByZWZlcmVuY2UgZm9yIG9w.ZW5zc2wgZW5jcnlwdGlvbiBhbGdvcml0aG1zCmh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGli.cmFyeS9oYXNobGliLmh0bWwKCgoKCgoKCgo=.
Comment                         : TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8va.CK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4.A3aM2Mp0AGDPrK3X4eMu8Q==.
Comment                         : uq3wDbqt8A26rfANuq3wDQ==.
Comment                         : 5VVoFK+6zDi3cJLX57zPLkf4WnbqsA6nywxZp9B+GGJP.
Comment                         : H4sIAAAAAAAAA+1YWW/bOBDOq/UrWPnFQp1Ukp2jRtKizdED22ObFlggDQzKpm1tZMmQ6MbZIP99.Z4akDltO2wXa7i7MPMTiHJz5OAfJ1zMx9nZmN1s/cLgw9nd38b+3v+uW/+NPt7Prb3mdPWDp7u16.3S2Y2nPdLeb+SKPMmGeSp4xtpUl8L9/X6P/R0XzwaJ6lj4IwfjS7kZMk7lhWk/2JUWFZ4XSWpJIl.mfmV3WSWNe6/4emVSN/yqcjYERuGA9lyQOx4IgZXLBwxORFsFEaCiUWYyayNc3EicT7GOWkNxYgR.+6vRGTCeEl8LZWLQ6vSshhZJsp0Zl5MdscrRmKVhLFv2aZomaY99inkAS8qEJTNYBjl7zGYPWS4D.IuAAqpItHw1OBR8ycJ2nN8TVZqmQ8zRmPGOcBTdSMJ6m/IbM/QDMz4kXLa5YEnCAAdmJG7BojGAC.zcjZ2sxOA9vRvKMdXJoYdwZRkgn8qdcOuEXrPZ+H0VAhfQIIhwku3cLlKhtw4S6G/BJ02ufvzu1V.4kgQ8fjdmxriMCDiye8f64gHWu2rOuJjIp7WEgddpfZlndrBQBGfHdcRXb3mmVtH9QzVq6P6hurX.UTuG2qlzZ6iM+oDujJKULVgYs5THY9FyF8JtM0DSpairii5I7tn79xhpmUxbi23kd2q0jJQWsVbL.6/cvylpgPUuFwgshC+5WoNMjQOUVPahYR1FVf3BpNUSUiRKD/fTpUxtznZJATtJkPp5Q5mYDHrMh.l5xFSXIVxmOGriBFxEMQSEZVNtJBOnE6GY0yITENtcQqP7r0Pk0GIsvOYfIE5lpIaDOsxRLdw88s./EsALJA/RAVIF/BJLFbjeoL1ZcEOmWFF3wAV/CQ8jxDsEc42Ag/LFBEeepc4k2YSU9ZjT5Bt6DIO.hsLnIX3uIwvoQi5wHcVx3nVJG5mxgI3y6GuQxDKM54LUKhwW20gq2PLcdhtNJrBcWSXQ0rkwRXMc.foHSNaWdY2EGwEdRci3AtBsmrxPEYiwnVGoyglFt8kue/UaU50hoTXWATJXZQ95jTYUb7gXtA9QK.vUwREWccIqQs6Hq9e6jDg3upj9dQy4BPDd4rvDliHwEdBIviMTRlmeqsCSxsVlS+gU0sZMoH1GmY.vJlB2dXxiMtp9LSYcj8zCfYatCg0MxVuYJNmgX28gKhRmsyXUlalMfhyrcZgQqGrPuojWYWvlqrG.sJYmYbPmDp9BMxm21KdjNa0mtj9KIe0IihZxrhgvVUrA9INSNpTbJvNhJ6Qx5Na9A7Zbt+f6i7se.O13MBDQeKAAoy4K5hICcA5DA4xGPvQOlYcqlNqwNSznYZos+24EaBob5VcNUFmp4jXOB7yh7tTUY.RyovfWW/irgl+3er9les/mN48G1W+0tWd/FTRPW2lKK/ulkmJoxDikiajRqj7yHzrWrtoNVy7bzs.6RmZf+6es212btIYK6etrIbzA9CP1tRUjbhveMFILKNKaFuTS6vl6opo6JYwU2Sn6pWW0SVxCQa1.pnOvv49X/cVZsE93kHDKx0L5u6TepckA2tgVFoqxUNmvkx1aZBCOUUsIZU/5APzRUqbghmBIRv7K.fOdSJRuZFnk9woVFfu/WK1CJvDZMESoDsB4xgTl2eMgOHNAR4W4vRwfyOSXdH8FqTDSdf6U2AHF7.MLwrAlg1gHzxwG8zpc2x6kJNWYQhZ8pqS6eeiQ74oa1zLN2ewSQsiceTeXyVlY6x6yVhC80Gau7q.+Rt+2p8pZjWb7l6fJf69I3Xqt2pminf5GEXrGfsdOkvxALytnpE0HQ4CTnFRuO32/LsKxLedXhc2.87MEYPdyhPcWas43qPvVFCiU5yjQbw0E/uZBe+Hg8W3NKd5qKpsqxzTgh5zo9xGsfh8zw+73pzyM.+327Z+Ww4bZ4kBmnCz4NY8HwmyHk7BjSS8Qys7HogipECmsaT8dfHOy1Xuna9CmDjOqpq16+R3bl.kuShnnz7jpjRdQHl+3tuaN9/NWugWdTzv/liVZKou17l8OE9jnKYkoiN0mTKKqkMyo0up12YiLvZ.MPtmGC7c3l73Mt9OmxH096SXitTyYSNfC/X/k7yDqveNidf8nsxrfj31ml/NvaK6/ay8o33KN/tZ.FLGTJBYPbOdXv7T8O8epOjDTxeFHPQPS+9/+uvc/1/c7rnr/23fdPZz3fL/rb97/fsaoe/8rPfYV.L4DqXEBNAx+hGIxqI1mKJPYqns0ltaV3c2l+quOrqjJQY0paPsu3iYQeMYHjvD674UU1ECwWYy7h.YkzPEDClzzWpiNT06lMDFr712umVgkxSj5RwwEq+iPQ6DSV0T7yKh1K/XNrmBQabxvKzH6pf6oFh.NqphKtmx/q3SLrWaXKrSiXFibftDYvVpkdiL9oefSy+M5R1rhbF6AQVk9A99OVKboV3RDTaHQ0lV.oKb+areL2y6YWO61hDnQjWjVr3x5+9q4pQ4yGBBPmFsgOtrBHROt0mm9p+86in3bu1QK1MvXfXJK.4NIYU6B234GsvK362eEDv2YEJztDV5/RsUy70Sz4K+eyFWpOsUrul85xcBfeLdzRGbkaMq6RJ5yX.Tm9I0FCXKb6mmCtE2ZyLjoZTb8YStWvQ+66ossoolpq19avr4mZsxmZsxmZsxmZsxmZsxmZsxv9t./A3BMDa8ACgAAA==.
```
<p>Flag tersebut salah, dan jika kita decode base64 pertama</p>
<pre>
CTFlearn{Gimli.Is.A.Dwarf}

Who is Gimli?  You can learn more about Gimli here:
https://lotr.fandom.com/wiki/Gimli
https://en.wikipedia.org/wiki/Gimli_(Middle-earth)

This challenge is based on hash algorithms and encryption.

I am using OPENSSL v1.1.1 to create this challenge.

Here is a reference for using hash calculations with OPENSSL:
https://www.openssl.org/docs/man1.1.1/man1/openssl-dgst.html

If you are a Python coder, Python provides a hashing library you might find useful:
https://docs.python.org/3/library/hashlib.html

If this challenge has you wondering what to do next, please try my other challenges
that are worth fewer points.  The more points, the more difficult the challenge.

If you are new to CTF and/or not quite sure how to solve this challenge,
you should probably try these other challenges first in this order:
RubberDuck
Snowboard
PikesPeak
GandalfTheWise

After solving this ShahOfGimli challenge, then try:
HailCaesar
MountainMan
KeyMaker
VargasIsland

My Twitter DM's are open @kcbowhunter.

----------------------------

The third comment block is encrypted with AES CBC encryption using the following key:
sha256 hash of the string "CTFlearn"

Note that the comment block is also base64 encoded
There is no iv but you need to determine how to express this mathematically

If you are new to encryption and hash algorithms here is a good place to start:
openssl enc -help
openssl dgst -help
sha256sum

Of course Google is your friend (if you don't mind them recording all your online activity)

https://wiki.openssl.org/index.php/Enc is a good reference for openssl encryption algorithms
https://docs.python.org/3/library/hashlib.html
</pre>
<p>Disana terdapat clue berupa key adalah sha256(CTFlearn) dan terkait dengan AES_CBC, lalu untuk comment ke-3 jika didecode itu merupakan sebuat encrypt.
Sekarang kita akan coba decrypt pesan tersebut</p>
<pre>
sha256(CTFlearn) = b18ef1351fc0df641abbe56dcd4928a8bb98452b1b43d8c1c13f1874c8b35056
IV = 00000000000000000000000000000000
</pre>

```python
import base64
from Crypto.Cipher import AES
import hashlib

msg = "TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8va.CK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4.A3aM2Mp0AGDPrK3X4eMu8Q=="
Key = "b18ef1351fc0df641abbe56dcd4928a8bb98452b1b43d8c1c13f1874c8b35056"
IV = "00000000000000000000000000000000"

key_dec = bytes.fromhex(Key)
IV = bytes.fromhex(IV)
encryption = base64.b64decode(msg)
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(decrypt)
```
<p>Hasilnya</p>
<pre>
CTFlearn{The_Shah_Of_Gimli_Is_The_Key}
CTFlearn{Gimli_Has_256_Gemstones}
CTFlearn{Breakfast_Hash_Is_The_Best}
</pre>
<p>Jika kita periksa dengan tool binwalk pada file JPG terdapat gzip compress</p>

```console
root@Python:/home/venom/Downloads# binwalk -e ShahOfGimli.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
132375        0x20517         gzip compressed data, from Unix, last modified: 1970-01-01 00:00:00 (null date)

root@Python:/home/venom/Downloads# cd _ShahOfGimli.jpg.extracted/
root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted# binwalk -e 20517 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             POSIX tar archive (GNU), owner user name: "ase.jpg"

root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted# cd _20517.extracted/
root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted/_20517.extracted# ls
0.tar  flag.enc  Gimli04Base.jpg
```
<p>Dari 3 Flag yg didapatkan diatas itu merupakan clue, yaitu Key merupakan sha256(File Gimli) dan juga pada file JPG masih terdapat file flag.enc yang masih encrypted AES_CBC</p>
<p>Decrypt file flag.enc sama dengan metode decrypt sebelumnya, dan decode file encrypt ke base64 terlebih dahulu</p>

```console
root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted/_20517.extracted# cat flag.enc | base64
fD3kitB7aiTuyjuKflZw4O4KX8+t6pHkzr8EGirMByk=
root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted/_20517.extracted# sha256sum Gimli04Base.jpg 
e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87  Gimli04Base.jpg
root@Python:/home/venom/Downloads/_ShahOfGimli.jpg.extracted/_20517.extracted# 
```

```python
import base64
from Crypto.Cipher import AES
import hashlib

msg = "fD3kitB7aiTuyjuKflZw4O4KX8+t6pHkzr8EGirMByk="
Key = "e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87"
IV = "00000000000000000000000000000000"
key_dec = bytes.fromhex(Key)
IV = bytes.fromhex(IV)
encryption = base64.b64decode(msg)
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(decrypt)
```
<p>Output program</p>
<pre>
CTFlearn{Gimli.Is.A.Warrior}\x04\x04\x04\x04
</pre>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{Gimli.Is.A.Warrior}
</pre>
