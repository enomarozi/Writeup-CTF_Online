<h1>Find the cat</h1>
<h3>Description</h3>
<label>The president’s cat was kidnapped by separatists. A suspect carrying a USB key has been arrested. Berthier, once again you have to save the Republic! Analyze this key and find out in which city the cat is retained!

The md5sum of the archive is edf2f1aaef605c308561888079e7f7f7. Input the city name in lowercase.</label>
<a href='https://static.root-me.org/forensic/ch9/ch9.gz'>File</a>
<h3>Solution</h3>
<label>Analisa file</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# mmls ch9              
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Win95 FAT32 (0x0b)
                                                                                
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# fls -o 2048 ch9                     
d/d 5:	Documentations
d/d 7:	Files
d/d 9:	WebSites
v/v 4096995:	$MBR
v/v 4096996:	$FAT1
v/v 4096997:	$FAT2
V/V 4096998:	$OrphanFiles
                                                                                
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# fls -o 2048 ch9 9
d/d 365610:	Apple - iPhone - iPhone 4 Technical Specifications_files
d/d * 365617:	Exchangeable image file format - Wikipedia, the free encyclopedia_files
d/d 413159:	RÃ©publique d'Alsace-Lorraine (1918-1918) - Lorraine CafÃ©_files
d/d 413167:	sept facons de tuer un chat  Nespolo Matias Lar  9782364740754  Amazon.com  Books_files
r/r 452693:	Apple - iPhone - iPhone 4 Technical Specifications.html
r/r * 452700:	Exchangeable image file format - Wikipedia, the free encyclopedia.html
r/r 460964:	sept facons de tuer un chat  Nespolo Matias Lar  9782364740754  Amazon.com  Books.html
r/r 460970:	RÃ©publique d'Alsace-Lorraine (1918-1918) - Lorraine CafÃ©.html
d/d 460974:	L'autonomie de l'Alsace_files
d/d 460977:	Voyager avec un chat_files
r/r 548757:	L'autonomie de l'Alsace.html
                                                                                
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# foremost ch9               
Processing: ch9
|foundat=mimetypeapplication/vnd.oasis.opendocument.textPK
foundat=Thumbnails/thumbnail.png�PNG
␦

��undat=Pictures/1000000000000CC000000990038D2A62.jpg�eP���-ڸCp���%���	.���&4�'�7޸���-@p����w������[�׭;�W�Q�s�sͧ����A/
foundat=mimetypeapplication/vnd.oasis.opendocument.textPK
foundat=layout-cachecd`d(������� d�q8X�a�c&L�b c##TtLzL�
                                                        ��ƹ2��y�D3B9_���0S�`
                                                                            ��)�R
**|
                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# cd output/zip 
                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads/output/zip]
└─# ls
00021506.zip  00028695.zip
                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads/output/zip]
└─# unzip 00021506.zip 
Archive:  00021506.zip
 extracting: mimetype                
 extracting: Thumbnails/thumbnail.png  
  inflating: Pictures/1000000000000CC000000990038D2A62.jpg  
  inflating: content.xml             
  inflating: styles.xml              
  inflating: settings.xml            
  inflating: meta.xml                
  inflating: manifest.rdf            
  inflating: Configurations2/accelerator/current.xml  
   creating: Configurations2/toolpanel/
   creating: Configurations2/statusbar/
   creating: Configurations2/progressbar/
   creating: Configurations2/toolbar/
   creating: Configurations2/images/Bitmaps/
   creating: Configurations2/popupmenu/
   creating: Configurations2/floater/
   creating: Configurations2/menubar/
  inflating: META-INF/manifest.xml   
                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads/output/zip]
└─# eog Pictures/1000000000000CC000000990038D2A62.jpg                                                                                                                             
                                                                                                                                 
┌──(root㉿Venom)-[/home/venom/Downloads/output/zip]
└─# exiftool -n -p '+$GPSlatitude+00$GPSlongitude' Pictures/1000000000000CC000000990038D2A62.jpg 
+47.604485+007.414579
```
<label>Cari lokasi sesuai koordinat</label>

```python3
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Chrome")
location = geolocator.reverse("+47.604485,+007.414579")
print(location)
```
<pre>
1, Rue Principale, Helfrantzkirch, Mulhouse, Haut-Rhin, Grand Est, France métropolitaine, 68510, France 
</pre>
<h3>Flag</h3>
<pre>
helfrantzkirch
</pre>
