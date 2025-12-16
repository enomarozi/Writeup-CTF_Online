<h1>APNG - Just A PNG</h1>
<h3>Description</h3>
<label>Your joking colleague challenges you to find the message hidden in this animation.</label>
<h3>Solution</h3>
<label>Analisa file APNG</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls
ch21.apng

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# zsteg ch21.apng              
meta Software       .. text: "APNG Assembler 2.91"
```
<label>Jika ada assembler maka ada disassembler</label>

```console                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# apngdis ch21.apng 

APNG Disassembler 2.9

Reading 'ch21.apng'...
extracting frame 1 of 13
extracting frame 2 of 13
extracting frame 3 of 13
extracting frame 4 of 13
extracting frame 5 of 13
extracting frame 6 of 13
extracting frame 7 of 13
extracting frame 8 of 13
extracting frame 9 of 13
extracting frame 10 of 13
extracting frame 11 of 13
extracting frame 12 of 13
extracting frame 13 of 13
all done
                                                                                                                 
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls
apngframe01.png  apngframe03.txt  apngframe06.png  apngframe08.txt  apngframe11.png  apngframe13.txt
apngframe01.txt  apngframe04.png  apngframe06.txt  apngframe09.png  apngframe11.txt  ch21.apng
apngframe02.png  apngframe04.txt  apngframe07.png  apngframe09.txt  apngframe12.png
apngframe02.txt  apngframe05.png  apngframe07.txt  apngframe10.png  apngframe12.txt
apngframe03.png  apngframe05.txt  apngframe08.png  apngframe10.txt  apngframe13.png
```
<label>Cetak flag dari file .txt</label>

```python3
import os
sort_files = []
for i in range(1,14):
    number = str(i).rjust(2,'0')
    file = open('apngframe'+number+'.txt').read().strip('\n')
    print(chr(int(file.split('=')[1].split('/')[0])),end='')
```
<h3>Flag</h3>
<pre>
FLAG:P3PoFRoG
</pre>
