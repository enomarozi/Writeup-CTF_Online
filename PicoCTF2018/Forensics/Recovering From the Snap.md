<h1><b>Recovering From the Snap</h1></b>
<pre>
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file, dan ekstrak data dengan foremost lalu buka seluruh file image yang didapatkan</p>

```console
root@Python:/home/venom/Downloads# file animals.dd 
animals.dd: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, root entries 512, sectors 20480 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 20, sectors/track 32, heads 64, serial number 0x9b664dde, unlabeled, FAT (16 bit)
root@Python:/home/venom/Downloads# binwalk animals.dd 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
39424         0x9A00          JPEG image data, JFIF standard 1.01
39454         0x9A1E          TIFF image data, big-endian, offset of first image directory: 8
672256        0xA4200         JPEG image data, JFIF standard 1.01
1165824       0x11CA00        JPEG image data, JFIF standard 1.01
1556992       0x17C200        JPEG image data, JFIF standard 1.01
1812992       0x1BAA00        JPEG image data, JFIF standard 1.01
1813022       0x1BAA1E        TIFF image data, big-endian, offset of first image directory: 8
2136576       0x209A00        JPEG image data, JFIF standard 1.01
2136606       0x209A1E        TIFF image data, big-endian, offset of first image directory: 8
2607616       0x27CA00        JPEG image data, JFIF standard 1.01
2607646       0x27CA1E        TIFF image data, big-endian, offset of first image directory: 8
3000832       0x2DCA00        JPEG image data, JFIF standard 1.01
3000862       0x2DCA1E        TIFF image data, big-endian, offset of first image directory: 8

root@Python:/home/venom/Downloads# foremost animals.dd 
Processing: animals.dd
|*|
root@Python:/home/venom/Downloads# cd output/
root@Python:/home/venom/Downloads/output# cd jpg/
root@Python:/home/venom/Downloads/output/jpg# eog *
```
<p align='center'>
  <img src="https://github.com/enomarozi/PicoCTF2018/blob/master/Images/Recovering%20From%20the%20Snap.jpg">
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{th3_5n4p_happ3n3d}
</pre>
