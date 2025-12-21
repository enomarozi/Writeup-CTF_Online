<h1>EXIF - Metadata</h1>
<h3>Description</h3>
<label>Our sad friend pepo got lost! Can you find where he is ?

The password is the city where pepo is located.</label><a href='https://static.root-me.org/steganographie/ch1/ch1.png'>File</a>
<h3>Solution</h3>
<label>Tool exiftool mendapatkan koordinat</label>

```console
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# exiftool -a ch1.png     
ExifTool Version Number         : 13.36
File Name                       : ch1.png
Directory                       : .
File Size                       : 13 kB
File Modification Date/Time     : 2025:12:21 09:31:50-05:00
File Access Date/Time           : 2025:12:21 09:31:50-05:00
File Inode Change Date/Time     : 2025:12:21 09:31:52-05:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 96
Image Height                    : 96
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 3779
Pixels Per Unit Y               : 3779
Pixel Units                     : meters
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : S0rry_N0_Gu3ss1ng_Gh1zm0!
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0232
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : ISISTM
GPS Latitude Ref                : North
GPS Latitude                    : 43 deg 17' 56.27"
GPS Longitude Ref               : East
GPS Longitude                   : 5 deg 22' 49.38"
Image Size                      : 96x96
Megapixels                      : 0.009
GPS Latitude                    : 43 deg 17' 56.27" N
GPS Longitude                   : 5 deg 22' 49.38" E
GPS Position                    : 43 deg 17' 56.27" N, 5 deg 22' 49.38" E
                                                                                                     
┌──(root㉿Kali)-[/home/venom/Downloads]
└─# exiftool -n -p '+$GPSlatitude+00$GPSlongitude' ch1.png     
+43.2989640793278+005.38038253781111
```

<label>get location dari koordinat</label>

```python3
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="rootme")
location = geolocator.reverse("+43.2989640793278,+005.38038253781111")
print(location,"\n")
print("nama city --> "+location.raw["address"]["city"])
```

<h3>Flag</h3>
<pre>
Marseille
</pre>
