<h1>Riddle Registry</h1>
<h3>Description</h3>
<label>Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here <a href='https://challenge-files.picoctf.net/c_amiable_citadel/3f00b89eeac6ac5242f747889ea4de24c804d9144cfa71e23d754e6a8e80e435/confidential.pdf'>Hidden Confidential Document</a> and uncover the flag within the metadata.</label>
<h3>Solution</h3>
<label>exiftool, grep, awk dan base64 decode</label>

```console
exiftool confidential.pdf | grep -i 'author' | awk -F': ' '{print $2}' | base64 -d
```
<h3>Flag</h3>
<pre>
picoCTF{puzzl3d_m3tadata_f0und!_c999e2a4}
</pre>
