<h1>DISKO 2</h1>
<h3>Description</h3>
<label>Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image <a href='https://artifacts.picoctf.net/c/541/disko-2.dd.gz'>here.</a></label>
<h3>Solution</h3>
<label>Cek File dan Partisi</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/PicoCTF]
└─# mmls disko-2.dd 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000053247   0000051200   Linux (0x83)
003:  000:001   0000053248   0000118783   0000065536   Win95 FAT32 (0x0b)
004:  -------   0000118784   0000204799   0000086016   Unallocated
```
<label>ada 2 partisi (Linux dan FAT32) dan cek flag</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads/PicoCTF]
└─# strings -a disko-2.dd| grep -i picoCTF{
picoCTF{4_P4Rt_1t_i5_5d70d515}
picoCTF{4_P4Rt_1t_i5_17d555d0}
picoCTF{4_P4Rt_1t_i5_157d50d5}
picoCTF{4_P4Rt_1t_i5_5dd07515}
picoCTF{4_P4Rt_1t_i5_d055d175}
picoCTF{4_P4Rt_1t_i5_dd150575}
picoCTF{4_P4Rt_1t_i5_5d570d51}
picoCTF{4_P4Rt_1t_i5_55175dd0}
picoCTF{4_P4Rt_1t_i5_75505d1d}
picoCTF{4_P4Rt_1t_i5_70d1555d}
picoCTF{4_P4Rt_1t_i5_1507dd55}
picoCTF{4_P4Rt_1t_i5_05dd1755}
picoCTF{4_P4Rt_1t_i5_51705dd5}
picoCTF{4_P4Rt_1t_i5_01d755d5}
picoCTF{4_P4Rt_1t_i5_10d55d75}
picoCTF{4_P4Rt_1t_i5_d05d5751}
picoCTF{4_P4Rt_1t_i5_755015dd}
picoCTF{4_P4Rt_1t_i5_d057515d}
picoCTF{4_P4Rt_1t_i5_55517dd0}
picoCTF{4_P4Rt_1t_i5_517dd550}
picoCTF{4_P4Rt_1t_i5_7d55501d}
picoCTF{4_P4Rt_1t_i5_510d5d57}
picoCTF{4_P4Rt_1t_i5_d5057d51}
picoCTF{4_P4Rt_1t_i5_05d7d551}
picoCTF{4_P4Rt_1t_i5_5155d7d0}
picoCTF{4_P4Rt_1t_i5_055dd175}
picoCTF{4_P4Rt_1t_i5_055dd175} <-- FLAG
picoCTF{4_P4Rt_1t_i5_5dd15750}se: 
Description-id.UTF-8: Tidak ada medpicoCTF{4_P4Rt_1t_i5_1d5055d7}
Description-nl.UTF-8: Uw ethernetpicoCTF{4_P4Rt_1t_i5_5710d55d}d_description-nl.UTF-8: Er is op dit systeem geen ethernetkaart gevonden.
Extended_description-pt.UTF-8: NecessitpicoCTF{4_P4Rt_1t_i5_d50d5751}
r din computer starter, vipicoCTF{4_P4Rt_1t_i5_570d5d15}l
```

<h3>Flag</h3>
<pre>
picoCTF{4_P4Rt_1t_i5_055dd175}
</pre>
