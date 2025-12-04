<h1>Oh My Grub</h1>
<h3>Description</h3>
<label>Your company has lost access to an old server, unfortunately it contains important files, it is up to you to find them.</label>
<a href='https://static.root-me.org/forensic/ch33/ch33.zip'></a>
<h3>Solution</h3>
<label>Tool TSK</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# mmls root-disk001.vmdk                   
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0015988735   0015986688   Linux (0x83)
003:  -------   0015988736   0015990783   0000002048   Unallocated
004:  Meta      0015990782   0016775167   0000784386   DOS Extended (0x05)
005:  Meta      0015990782   0015990782   0000000001   Extended Table (#1)
006:  001:000   0015990784   0016775167   0000784384   Linux Swap / Solaris x86 (0x82)
007:  -------   0016775168   0016777215   0000002048   Unallocated
                                                                                                    
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# fls -o 2048 root-disk001.vmdk        
d/d 262311:	home
d/d 11:	lost+found
d/d 262145:	etc
d/d 262147:	media
l/l 896:	vmlinuz
d/d 13:	var
d/d 131073:	usr
d/d 262151:	lib
d/d 262204:	bin
d/d 262215:	sbin
d/d * 262306:	tmp
d/d 262307:	sys
d/d 262308:	run
d/d 262309:	root
d/d 262310:	proc
d/d 262312:	dev
d/d 203:	boot
d/d * 247:	mnt
d/d * 248:	srv
d/d 249:	opt
l/l 904:	initrd.img
V/V 499713:	$OrphanFiles
                                                                                                    
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# fls -o 2048 root-disk001.vmdk 262309 
r/r 263157:	.profile
r/r 263158:	.bashrc
r/r 269358:	.passwd
r/r 269360:	.bash_history
r/r 262378:	.lesshst
r/r * 263164:	.passwd~

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# icat -o 2048 root-disk001.vmdk 269358
Bravo voici le flag :

F1aG-M3_PlEas3:)

Congratulation ! You may validate using this flag 

F1aG-M3_PlEas3:)
```
<h3>Flag</h3>
<pre>
F1aG-M3_PlEas3:)
</pre>
