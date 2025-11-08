<h1>Hidden in plainsight</h1>
<h3>Description</h3>
<label>You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag. Download the jpg image <a href='https://challenge-files.picoctf.net/c_amiable_citadel/5123e48e549ac5d8abb421627478aaf17d88b8e57b72ae5163183c55a693cc57/img.jpg'>here.</a></label>
<h3>Solution</h3>
<label>Command pipeline exiftool, grep, awk, base64 -d, awk dan base64-d</label>

```console
exiftool img.jpg | grep -i 'comment' | awk -F ': ' '{print $2}' | base64 -d | awk -F ':' '{print $2}' | base64 -d
```
<label>Extract flag dengan password</label>

```console
steghide -sf extract img.jpg -p pAzzword
```
<h3>Flag</h3>
<pre>
picoCTF{h1dd3n_1n_1m4g3_656e4d79}
</pre>
