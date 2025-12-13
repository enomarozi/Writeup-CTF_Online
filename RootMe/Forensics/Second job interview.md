<h1>Second job interview</h1>
<h3>Description</h3>
<label>After passing the first interview with flying colors you’re now called in again.
You’ve got to analyze a new file.</label><a href='https://static.root-me.org/forensic/ch17/ch17.zip'>File</a>
<h3>Solution</h3>
<label>Image disk forensic</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file forensic.E01  
forensic.E01: EWF/Expert Witness/EnCase image file format
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ewfexport forensic.E01                       

ewfexport 20140816

Information for export required, please provide the necessary input
Export to format (raw, files, ewf, smart, ftk, encase1, encase2, encase3, encase4, encase5, encase6, encase7, encase7-v2, linen5, linen6, linen7, ewfx) [raw]: 
Target path and filename without extension or - for stdout: image
Evidence segment file size in bytes (0 is unlimited) (0 B <= value <= 7.9 EiB) [0 B]: 
Start export at offset (0 <= value <= 615516160) [0]: 
Number of bytes to export (0 <= value <= 615516160) [615516160]: 

Export started at: Dec 13, 2025 13:54:13
This could take a while.

Export completed at: Dec 13, 2025 13:54:16

Written: 587 MiB (615516160 bytes) in 3 second(s) with 195 MiB/s (205172053 bytes/second).
MD5 hash calculated over data:		9f6a0da4d8658c0980d97627be8f6eb9
ewfexport: SUCCESS

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls
ch17.zip  forensic.E01  image.raw  image.raw.info
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file image.raw                                                
image.raw: POSIX tar archive (GNU)
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# tar xvf image.raw
image.dd
memory.dmp
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x64 filescan | grep -i flag
Volatility Foundation Volatility Framework 2.6.1
0x000000001db096b0      2      0 RW-rw- \Device\HarddiskVolume2\Users\info\AppData\Roaming\Microsoft\Windows\Recent\flag.txt.lnk
0x000000001db67f20     16      0 RW---- \Device\HarddiskVolume3\flag.jpg
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x64 dumpfiles -Q 0x000000001db67f20 --name -D .
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x1db67f20   None   \Device\HarddiskVolume3\flag.jpg
                                                                                                                                                                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# eog file.None.0xfffffa8002b23f10.flag.jpg.dat
```
<h3>Flag</h3>
<pre>
B1tL0ck3R_1ts_n0t_sUr3
</pre>
