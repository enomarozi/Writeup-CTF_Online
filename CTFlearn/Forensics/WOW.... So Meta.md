<h1><b>WOW.... So Meta</h1></b>
<pre>
This photo was taken by our target. See what you can find out about him from it. 
https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk
</pre>
</b><h3>Solution</h3></b>
<p>Diberikan 1 file image JPEG, eksekusi perintah exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# file 3UWLBAUCb9Z2.jpg 
3UWLBAUCb9Z2.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=8, orientation=upper-left, xresolution=2170, yresolution=2178, resolutionunit=2, software=Photos 1.5, datetime=2014:12:27 16:45:55], baseline, precision 8, 800x307, components 3
root@Python:/home/venom/Downloads# exiftool 3UWLBAUCb9Z2.jpg | grep -i flag
Camera Serial Number            : flag{EEe_x_I_FFf}
root@Python:/home/venom/Downloads# 

```
</b><h3>Flag</h3></b>
<pre>
flag{EEe_x_I_FFf}
</pre>
