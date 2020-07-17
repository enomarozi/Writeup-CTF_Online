<h1><b>UNDISPUTED</h1></b>
<pre>
n00b found a file somewhere in the proland. 
Search this <a href="http://static.beast.sdslabs.co/static/UNDISPUTED/file.ext4">file</a> to find the flag. Submit SHA-256 of the flag obtained.
</pre>
<h3><b>Solution</b></h3>
<p>Eksekusi sederhana pada terminal</p>

```console
root@Python:/home/venom/Downloads# file file.ext4 
file.ext4: Linux rev 1.0 ext4 filesystem data, UUID=088c23fa-b15c-4439-b709-990571544124 (extents) (huge files)
root@Python:/home/venom/Downloads# binwalk -e file.ext4 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Linux EXT filesystem, blocks count: 3072, image size: 3145728, rev 1.0, ext4 filesystem data, UUID=088c23fa-b15c-4439-b709-990571547154

root@Python:/home/venom/Downloads# cd _file.ext4.extracted/ext-root/
root@Python:/home/venom/Downloads/_file.ext4.extracted/ext-root# 7z x n00b.7z 
7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,8 CPUs Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz (306A9),ASM,AES-NI)

Scanning the drive for archives:
1 file, 194 bytes (1 KiB)

Extracting archive: n00b.7z
--
Path = n00b.7z
Type = 7z
Physical Size = 194
Headers Size = 162
Method = LZMA:16
Solid = -
Blocks = 1

Everything is Ok

Folders: 1
Files: 1
Size:       28
Compressed: 194
root@Python:/home/venom/Downloads/_file.ext4.extracted/ext-root# cd n00b/
root@Python:/home/venom/Downloads/_file.ext4.extracted/ext-root/n00b# strings n00b.txt 
flag: like_a_walk_in_a_park
root@Python:/home/venom/Downloads/_file.ext4.extracted/ext-root/n00b# 
```
<h3><b>Flag</b></h3>
<pre>
like_a_walk_in_a_park
</pre>
