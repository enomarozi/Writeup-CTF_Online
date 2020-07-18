<h1><b>Encrypted ZIP</h1></b>
<pre>
wierd.zip and flag.zip apparently have the same password. We also found a unzipped version of wierd.txt
<a href="https://ringzer0ctf.com/files/0e7e17b0a3b18dbce02ad55c6cf868ae.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Tantangan kita disini ialah mencari password dari file zip atau crack password, sesuai intruksi challenge kita diberikan 2 file ZIP yaitu :</p>
<p>- File Flag.zip yaitu zip ter-encrypt</p>
<p>- File Weird.zip juga zip ter-encrypt, tetapi challenge memberikan hasil ekstraknya yaitu weird.txt</p>
<p>Berarti kita bisa melakukan serangan known-plaintext-attack, yaitu sejenis serangan bruteforce yang memanfaatkan 1 file zip terencrypt dengan 1 file zip tidak ter-encrypt, 
yang artinya kedua file tersebut memiliki file dan content yang sama untuk dijadikan referensi cracking oleh serangan</p>
<p>Pertama compress file weird.txt ke ZIP file (tanpa password)</p>

```console
root@Python:/home/venom/Downloads# zip non-encrypt.zip weird.txt 
  adding: weird.txt (deflated 100%)
```
<p>Eksekusi bruteforce dengan tool pkcrack</p>

```console
root@Python:/home/venom/Downloads# ../Tools/pkcrack-1.2.2/src/pkcrack -C weird.zip -c weird.txt -P non-encrypt.zip -p weird.txt -d decrypt.zip -a
Files read. Starting stage 1 on Sat Jul 18 20:10:03 2020
Generating 1st generation of possible key2_96 values...done.
Found 4194304 possible key2-values.
Now we're trying to reduce these...
Done. Left with 109196 possible Values. bestOffset is 24.
Stage 1 completed. Starting stage 2 on Sat Jul 18 20:10:07 2020
Strange... had a false hit.
Strange... had a false hit.
Strange... had a false hit.
Strange... had a false hit.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
Ta-daaaaa! key0=3330b3a9, key1=c403beea, key2=a0b3129d
Probabilistic test succeeded for 77 bytes.
Strange... had a false hit.
Stage 2 completed. Starting password search on Sat Jul 18 20:50:55 2020
Key: 74 65 73 74 74 65 73 74
Or as a string: 'testtest' (without the enclosing single quotes)
Key: 74 65 73 74 74 65 73 74
Or as a string: 'testtest' (without the enclosing single quotes)
Finished on Sat Jul 18 20:50:55 2020
root@Python:/home/venom/Downloads# 
```
<p>Passwordnya didapatkan yaitu testtest, dalam waktu 40 menit</p>
<p>Jika kita lakukan serangan known-plaintext-attack sesuai challenge, itu sangat memakan waktu. Disini ada tool yang mampu melakukan cracking 1 menit kurang yaitu john-the-ripper</p>

```console
root@Python:/home/venom/Downloads# zip2john flag.zip > flag_john.txt
ver 2.0 flag.zip/flag.txt PKZIP Encr: cmplen=41, decmplen=29, crc=58511BF4
root@Python:/home/venom/Downloads# john flag_john.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
No password hashes left to crack (see FAQ)
root@Python:/home/venom/Downloads# john flag_john.txt --show
flag.zip/flag.txt:testtest:flag.txt:flag.zip::flag.zip

1 password hash cracked, 0 left
root@Python:/home/venom/Downloads#
```
<p>Ektrak dan buka flag.zip</p>

```console
root@Python:/home/venom/Downloads# unzip flag.zip 
Archive:  flag.zip
[flag.zip] flag.txt password: 
 extracting: flag.txt                
root@Python:/home/venom/Downloads# cat flag.txt 
FLAG-Mk5N1z6PDbcw6alA1G8ixz85
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
FLAG-Mk5N1z6PDbcw6alA1G8ixz85
</pre>
