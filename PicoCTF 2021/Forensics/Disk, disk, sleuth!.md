<h1>Disk, disk, sleuth!</h1>
<h3>Description</h3>
<pre>
Use srch_strings from the sleuthkit and some terminal-fu to find a flag in this disk image.
<a href='https://challenge-files.picoctf.net/c_wily_courier/8643b47c3c19e52e891a4684258e1d1cbb65094afa9cf81317b563004a739653/dds1-alpine.flag.img.gz'>dds1-alpine.flag.img.gz</a>
</pre>
<h3>Solution</h3>
<label>Tool forensic binwalk dan TSK</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# binwalk -e dds1-alpine.flag.img --run-as=root

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1048576       0x100000        Linux EXT filesystem, blocks count: 130048, image size: 133169152, rev 1.0, ext3 filesystem data, UUID=655d1b59-b527-47f6-b78c-9828747e747e

                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# cd _dds1-alpine.flag.img.extracted 
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_dds1-alpine.flag.img.extracted]
└─# grep -iR 'picoCTF{'
grep: 100000.ext: binary file matches
ext-root/boot/syslinux.cfg:  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_dds1-alpine.flag.img.extracted]
└─# mmls ../dds1-alpine.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_dds1-alpine.flag.img.extracted]
└─# fls -r -p -o 2048 dds1-alpine.flag.img | grep -i 'syslinux'
Error stat(ing) image file (raw_open: image "dds1-alpine.flag.img" - No such file or directory)
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads/_dds1-alpine.flag.img.extracted]
└─# fls -r -p -o 2048 ../dds1-alpine.flag.img | grep -i 'syslinux'
r/r 8138:	boot/syslinux.cfg
                                                                                                             
┌──(root㉿Kali)-[/home/venom/Downloads/_dds1-alpine.flag.img.extracted]
└─# icat -o 2048 ../dds1-alpine.flag.img 8138                     
DEFAULT linux
  SAY Now booting the kernel from SYSLINUX...
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
 LABEL linux
  KERNEL /boot/vmlinuz-virt
  APPEND ro root=/dev/sda1 rootfstype=ext3 initrd=/boot/initramfs-virt

```
<label>Flag terletak di file syslinux.cfg folder /boot</label>
<h3>Flag</h3>
<pre>
picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
</pre>
