<h1>CanYouSee</h1>
<h3>Description</h3>
<p>How about some hide and seek?
Download this file </p>
<a href='https://artifacts.picoctf.net/c_titan/131/unknown.zip'>File</a>
<h3>Solution</h3>
<p>Check encode base64 meta data image</p>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# exiftool ukn_reality.jpg | grep 'Attribution URL' | awk '{print $4}' | base64 -d
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```
<h3>Flag</h3>
<pre>picoCTF{ME74D47A_HIDD3N_d8c381fd}</pre>
