<h1>Deleted file</h1>
<h3>Description</h3>
<label>Your cousin found a USB drive in the library this morning. He’s not very good with computers, so he’s hoping you can find the owner of this stick!

The flag is the owner’s identity in the form firstname_lastname

sha256sum: cd9f4ada5e2a97ec6def6555476524712760e3d8ee99c26ec2f11682a1194778</label>
<a href='https://static.root-me.org/forensic/ch39/ch39.gz'>File</a>
<h3>Solution</h3>
<label>Identifikasi image</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# file usb.image 
usb.image: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, reserved sectors 4, root entries 512, sectors 63488 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 64, sectors/track 62, heads 124, hidden sectors 2048, reserved 0x1, serial number 0xc7ecde5b, label: "USB        ", FAT (16 bit)

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# fls -r usb.image                      
r/r 3:	USB         (Volume Label Entry)
r/r * 5:	anonyme.png
v/v 1013699:	$MBR
v/v 1013700:	$FAT1
v/v 1013701:	$FAT2
V/V 1013702:	$OrphanFiles

┌──(root㉿Venom)-[/home/venom/Downloads]
└─# icat usb.image 5 > image.png
                                                                                                                        
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# file image.png         
image.png: PNG image data, 400 x 300, 8-bit/color RGB, non-interlaced
                                                                                                                                                                                                                                         
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# exiftool image.png | grep -i 'Creator'
Creator                         : Javier Turcot

```
<h3>Flag</h3>
<pre>
javier_turcot
</pre>
