<h1>information</h1>
<h3>Description</h3>
<p>Files can always be changed in a secret way. Can you find the flag? <a href='https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg'>cat.jpg</a></p>
<h3>Solution</h3>
<p>Decode base64 dari metadata</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# exiftool cat.jpg | grep "License" | awk -F': ' '{print $2}' | base64 -d
picoCTF{the_m3tadata_1s_modified}
```
<h3>Flag</h3>
<pre>
picoCTF{the_m3tadata_1s_modified}
</pre>
