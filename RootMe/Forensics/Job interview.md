<h1>Job interview</h1>
<h3>Description</h3>
<label>You are invited to an interview for a forensics investigator position at the NSA. For your first technical evaluation they ask you to analyze this file. Prove to them that you’re a fitting candidate for this job.

SHA256 hash : b35f4cd4bad19301e6970b30c1c713883b657858ef86d2b7247272c9d0f23591

</label><a href='https://static.root-me.org/forensic/ch16/ch16.zip'>File</a>
<h3>Solution</h3>
<label>Analisa FIle EWF</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file image_forensic.e01 
image_forensic.e01: EWF/Expert Witness/EnCase image file format

┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ewfexport image_forensic.e01                                              

ewfexport 20140816

Information for export required, please provide the necessary input
Export to format (raw, files, ewf, smart, ftk, encase1, encase2, encase3, encase4, encase5, encase6, encase7, encase7-v2, linen5, linen6, linen7, ewfx) [raw]: 
Target path and filename without extension or - for stdout: image
Evidence segment file size in bytes (0 is unlimited) (0 B <= value <= 7.9 EiB) [0 B]: 
Start export at offset (0 <= value <= 9431040) [0]: 
Number of bytes to export (0 <= value <= 9431040) [9431040]: 

Export started at: Dec 06, 2025 09:50:25
This could take a while.

Export completed at: Dec 06, 2025 09:50:25

Written: 8.9 MiB (9431040 bytes) in 0 second(s).
MD5 hash calculated over data:		ba74f9213ff89221eb9b68cd03ff0242
ewfexport: SUCCESS
                                                                                                                                                                                           
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# file image.raw
image.raw: POSIX tar archive (GNU)
                                                                                                                                                                                           
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# tar xvf image.raw
bcache24.bmc
```
<label>Extract BMC (RDP Bitmap Cache)

```console
┌──(root㉿Kali)-[/home/venom/Downloads/output]
└─# bmctool -s bcache24.bmc -d output -b
┌──(root㉿Kali)-[/home/venom/Downloads/output]
└─# eog bcache24.bmc_collage.bmp 
```
<h3>Flag</h3>
<pre>
RdP_l3av3s_Trac3S
</pre>
