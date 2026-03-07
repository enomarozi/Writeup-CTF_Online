<h1>Forensics</h1>
<h3>Description</h3>
<pre>
'Suspicious' is written all over this disk image.
Download <a href='https://challenge-files.picoctf.net/c_shape_facility/004d4e9345d26e6054e3971df0e1efcfbea71ef7bf659bdc30bfd8a78726c85b/suspicious.dd.sda1'>suspicious.dd.sda1</a>
</pre>
<h3>Solution</h3>
<label>Partition forensic, sesuai hint check slack space</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# fls -r -p suspicious.dd.sda1
d/d 11:	lost+found
d/d 2009:	boot
d/d 2010:	boot/grub
r/r 2013:	boot/grub/e2fs_stage1_5
r/r 2014:	boot/grub/fat_stage1_5
r/r 2015:	boot/grub/ffs_stage1_5
r/r 2016:	boot/grub/iso9660_stage1_5
r/r 2017:	boot/grub/jfs_stage1_5
r/r 2018:	boot/grub/minix_stage1_5
r/r 2019:	boot/grub/reiserfs_stage1_5
r/r 2020:	boot/grub/stage1
r/r 2021:	boot/grub/stage2
r/r 2022:	boot/grub/stage2_eltorito
r/r 2023:	boot/grub/ufs2_stage1_5
r/r 2024:	boot/grub/vstafs_stage1_5
r/r 2025:	boot/grub/xfs_stage1_5
r/r 2026:	boot/grub/menu.lst
r/r 2011:	boot/core.gz
r/r 2012:	boot/vmlinuz
d/d 4017:	tce
r/r 4018:	tce/mydata.tgz
d/d 4019:	tce/optional
r/r 4022:	tce/optional/openssh.tcz.dep
r/r 4023:	tce/optional/gcc_libs.tcz.md5.txt
r/r 4024:	tce/optional/gcc_libs.tcz
r/r 4025:	tce/optional/openssl-1.0.0.tcz.md5.txt
r/r 4026:	tce/optional/openssl-1.0.0.tcz
r/r 4027:	tce/optional/openssh.tcz.md5.txt
r/r 4028:	tce/optional/openssh.tcz
r/r 4029:	tce/optional/nano.tcz.dep
r/r 4030:	tce/optional/ncurses.tcz.dep
r/r 4031:	tce/optional/ncurses-common.tcz.md5.txt
r/r 4032:	tce/optional/ncurses-common.tcz
r/r 4033:	tce/optional/ncurses.tcz.md5.txt
r/r 4034:	tce/optional/ncurses.tcz
r/r 4035:	tce/optional/nano.tcz.md5.txt
r/r 4036:	tce/optional/nano.tcz
r/r 4037:	tce/optional/nginx.tcz.dep
r/r 4038:	tce/optional/pcre.tcz.dep
r/r 4039:	tce/optional/bzip2-lib.tcz.md5.txt
r/r 4040:	tce/optional/bzip2-lib.tcz
r/r 4041:	tce/optional/pcre.tcz.md5.txt
r/r 4042:	tce/optional/pcre.tcz
r/r 4043:	tce/optional/nginx.tcz.md5.txt
r/r 4044:	tce/optional/nginx.tcz
r/r 4045:	tce/optional/fuse.tcz.md5.txt
r/r 4046:	tce/optional/fuse.tcz
r/r 4047:	tce/optional/libdnet.tcz
r/r 4048:	tce/optional/open-vm-tools.tcz
r/r 4049:	tce/optional/open-vm-tools-modules-3.8.13-tinycore.tcz
r/r 4050:	tce/optional/libtirpc.tcz.md5.txt
r/r 4051:	tce/optional/libtirpc.tcz
r/r 4052:	tce/optional/glib2.tcz.dep
r/r 4053:	tce/optional/libffi.tcz.md5.txt
r/r 4054:	tce/optional/libffi.tcz
r/r 4055:	tce/optional/glib2.tcz.md5.txt
r/r 4056:	tce/optional/glib2.tcz
d/d 4020:	tce/ondemand
r/r 4021:	tce/onboot.lst
r/r 12:	suspicious-file.txt
V/V 8033:	$OrphanFiles
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# icat suspicious.dd.sda1 12       
Nothing to see here! But you may want to look here -->
```
<label>Check slack space per sector</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# strings -a -t x suspicious.dd.sda1 | grep "Nothing"
 200400 Nothing to see here! But you may want to look here -->
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# xxd -s 0x200400 -l 200 suspicious.dd.sda1
00200400: 4e6f 7468 696e 6720 746f 2073 6565 2068  Nothing to see h
00200410: 6572 6521 2042 7574 2079 6f75 206d 6179  ere! But you may
00200420: 2077 616e 7420 746f 206c 6f6f 6b20 6865   want to look he
00200430: 7265 202d 2d3e 0a7d 0033 0039 0038 0036  re -->.}.3.9.8.6
00200440: 0033 0031 0032 0066 005f 0033 003c 005f  .3.1.2.f._.3.<._
00200450: 007c 004c 006d 005f 0031 0031 0031 0074  .|.L.m._.1.1.1.t
00200460: 0035 005f 0033 0062 007b 0046 0054 0043  .5._.3.b.{.F.T.C
00200470: 006f 0063 0069 0070 0000 0000 0000 0000  .o.c.i.p........
00200480: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00200490: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
002004c0: 0000 0000 0000 0000                      ........
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# xxd -s 0x200400 -l 200 suspicious.dd.sda1 | xxd -r | rev    
>-- ereh kool ot tnaw yam uoy tuB !ereh ees ot gnihtoN
picoCTF{b3_5t111_mL|_<3_f2136893} 
```

<h3>Flag</h3>
<pre>
picoCTF{b3_5t111_mL|_<3_f2136893} 
</pre>
