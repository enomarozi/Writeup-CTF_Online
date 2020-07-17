<h1><b>FIND-THE-BABY</b></h1>
<pre>
President's baby was kidnapped by underworld. 
A suspect carrying a USB key has been arrested. 
Once again, it is up to you to analyze this key and find out in which city the baby is retained!
<a href="http://static.beast.sdslabs.co/static/FIND-THE-BABY/usb.dd">usb</a>

Flag = CTF{city_name_in_lowercase}
</pre>
<h3><b>Solution</b></h3>
<p>Kita diminta untuk mencari kota dari gambar bayi yang didapatkan, ekstrak semua file dengan binwalk lalu cari foto bayi dan lokasi koordinat GPS-nya</p>

```console
root@Python:/home/venom/Downloads# binwalk -e usb.dd 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ISO 9660 Primary Volume,

root@Python:/home/venom/Downloads# cd _usb.dd.extracted/iso-root/private/
root@Python:/home/venom/Downloads/_usb.dd.extracted/iso-root/private#  exiftool -n -p '+$GPSlatitude+00$GPSlongitude' baby*
Warning: [Minor] Tag 'GPSlatitude' not defined - baby1.jpeg
Warning: [Minor] Tag 'GPSlatitude' not defined - baby2.jpeg
+23.16697+0079.95006
Warning: [Minor] Tag 'GPSlatitude' not defined - baby4.jpeg
Warning: [Minor] Tag 'GPSlatitude' not defined - baby5.jpg
    5 image files read
root@Python:/home/venom/Downloads/_usb.dd.extracted/iso-root/private# 
```
<p>Kita mendapatkan koordinat GPS pada file image baby3.jpg

```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="xvenom")
location = geolocator.reverse("23.16697, 0079.95006")
print("CTF{"+location.raw["address"]["city"].lower()+"}")
```
<h3><b>Flag</b></h3>
<pre>
CTF{jabalpur}
</pre>
