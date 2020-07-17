<h1><b>Dr Pouce</h1></b>
<pre>
Find in which city DR Pouce is keeped ! Then find who is the evil man?

answer format : cityfirstnamelastname
<a href="https://ringzer0ctf.com/files/6a613824f82f8be411884a09e4689e84.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Ekstrak file zip, maka didapatkan file image JPG dan PDF, sesuai format flag yaitu city+firstname+lastname. Untuk mencari city eksekusi exiftool pada file image, 
maka didapatkan koordinat latitude dan longitude</p>

```console
root@Python:/home/venom/Downloads# exiftool -n -p '+$GPSlatitude+00$GPSlongitude' DR_Pouce.jpg 
+44.646231+00-63.573287
root@Python:/home/venom/Downloads# 
```
<p>Cari nama city pada koordinta tersebut,</p>

```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="xvenom")
location = geolocator.reverse("+44.646231,-63.573287")
print(location,"\n")
print("nama city --> "+location.raw["address"]["city"].lower())
```
<p>Hasilnya</p>
<pre>
Sackville Street, Downtown Halifax, Halifax, Halifax Regional Municipality, Halifax County, Nova Scotia, B3J 1K5, Canada 

nama city --> halifax
</pre>
<p>Didapatkan nama city yaitu <b>halifax</b>, selanjutnya cari firstname dan lastname. itu terdapat pada file pdf, dengan eksekusi exiftool pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool -author DR_Pouce.pdf 
Author                          : Steve Finger
root@Python:/home/venom/Downloads# 
```
<p>Dan didapatkan firstname yaitu <b>steve</b> dan lastname <b>finger</b>, jadi flag yaitu <b>halifaxstevefinger</b> lowercase</p>

</b><h3>Flag</h3></b>
<pre>
halifaxstevefinger
</pre>
