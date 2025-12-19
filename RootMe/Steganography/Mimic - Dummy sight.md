<h1>Mimic - Dummy sight</h1>
<h3>Description</h3>
<label>A childhood friend knows that you work in cybersecurity, and he thinks he has received a fraudulent email containing two attachments. He asks you to check that it is not malicious.</label>
<h3>Solution</h3>
<label>Merupakan text encipher </label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads/attachments]
└─# ls
ciphertext  plaintext
                                                                                                                                                                                                  
┌──(root㉿Venom)-[/home/venom/Downloads/attachments]
└─# cat ciphertext | plainsight -m decipher -f plaintext 
Adding models:
Model: plaintext added in 0.00s (context == 2)
input is "<stdin>", output is "<stdout>"

deciphering: 100%|####################################################################################################################################################| 53.92 kB/s | Time: 0:00:00

$ROO =  "MV93!fbjB0X200bDFjMTB1NV#F80b^h".Replace("!","NHN").Replace("@","q").Replace("#","80d").Replace("<","ZXI=").Replace("%","GVF").Replace("^","Gw").Replace("&","cTW").Replace("*","zb2Z").Replace("[","T").Replace("]","iZW1").Replace("{","Fdi");
$TME = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($ROO));
```
<label>Didapatkan syntax PowerShell</label>

```powershell
┌──(root㉿Venom)-[/home/venom/Downloads/attachments]
└─# pwsh          
PowerShell 7.5.4
PS /home/venom/Downloads/attachments> $ROO =  "MV93!fbjB0X200bDFjMTB1NV#F80b^h".Replace("!","NHN").Replace("@","q").Replace("#","80d").Replace("<","ZXI=").Replace("%","GVF").Replace("^","Gw").Replace("&","cTW").Replace("*","zb2Z").Replace("[","T").Replace("]","iZW1").Replace("{","Fdi");
PS /home/venom/Downloads/attachments> $ROO
MV93NHNfbjB0X200bDFjMTB1NV80dF80bGwh
PS /home/venom/Downloads/attachments> $TME = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($ROO))
PS /home/venom/Downloads/attachments> $TME
1_w4s_n0t_m4l1c10u5_4t_4ll!
```
<h3>Flag</h3>
<pre>
1_w4s_n0t_m4l1c10u5_4t_4ll!
</pre>
