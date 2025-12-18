<h1>Yellow dots</h1>
<h3>Description</h3>
<label>You attend an interview for a forensic investigator job and they give you a challenge to solve as quickly as possible (having the Internet).
They ask you to find the date of printing as well as the serial number of the printer in this document.
You remain dubitative and accept the challenge.

The answer is in the form:
hh:mm dd/mm/yyyy SSSSSSSS
with
 hh: the hour of the event
 mm: the minutes of the event
 dd: the day of the event
 MM: the month of the event
 yyyy: the year of the event
 SSSSSSSS: the serial number</label><a href='https://static.root-me.org/steganographie/ch18/ch18.png'>File</a>
<h3>Solution</h3>
<label>Analisa file ch18.png, judul dan resource mengenai yellow dots printer</label>

```console
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# convert -channel RG -fx 0 ch18.png blue.png
                                                                                                             
┌──(root㉿Venom)-[/home/venom/Downloads]
└─# eog blue.png  
```
<label>Check semua dots yang berada di bagian atas kanan gambar, decode di link https://yellow-dots-decoder.mathieurenaud.fr, sesuaikan dots dengan matrix</label>
<h3>Flag</h3>
<pre>
11:05 27/07/2014 06922930
</pre>
