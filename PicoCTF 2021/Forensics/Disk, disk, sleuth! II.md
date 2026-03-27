<h1>Disk, disk, sleuth! II</h1>
<h3>Description</h3>
<pre>
All we know is the file with the flag is named down-at-the-bottom.txt...
<a href='https://challenge-files.picoctf.net/c_wily_courier/faf30bf494c9feae75263f7006b2042ecbbdd211e5d096ffcfff72b123396a19/dds2-alpine.flag.img.gz'>dds2-alpine.flag.img.gz</a>
</pre>
<h3>Solution</h3>
<label>Check TSK (mmls, fls dan icat)</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# mmls dds2-alpine.flag.img                              
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# fls -r -p -o 2048 dds2-alpine.flag.img | grep -i '.txt'
r/r 18291:	root/down-at-the-bottom.txt
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# icat -o 2048 dds2-alpine.flag.img 18291
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( 4 ) ( b ) ( d ) ( 7 ) ( 2 ) ( 1 ) ( f ) ( 2 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
                                                                                
┌──(root㉿Kali)-[/home/venom/Downloads]
```
<h3>Flag</h3>
<pre>
picoCTF{f0r3ns1c4t0r_n0v1c3_4bd721f2}
</pre>
