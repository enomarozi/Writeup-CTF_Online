<h1><b>Tux!</h1></b>
<pre>
The flag is hidden inside the Penguin! 
Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.

<a href='https://ctflearn.com/challenge/download/973'>Tux.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Hanya dengan perintah sederhana, dan ikuti langkah console dibawah</p>

```console
root@Python:/home/venom/Downloads# exiftool Tux.jpg | grep -i comment
Comment                         : ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK.
root@Python:/home/venom/Downloads# echo "ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK" | base64 -d
      Password: Linux12345
root@Python:/home/venom/Downloads# foremost Tux.jpg 
Processing: Tux.jpg
|foundat=flagUT	
*|
root@Python:/home/venom/Downloads# cd output/zip/
root@Python:/home/venom/Downloads/output/zip# unzip 00000010.zip 
Archive:  00000010.zip
[00000010.zip] flag password: Linux12345
 extracting: flag                    
root@Python:/home/venom/Downloads/output/zip# cat flag 
CTFlearn{Linux_Is_Awesome}
root@Python:/home/venom/Downloads/output/zip# 
```
</b><h3>Flag</h3></b>
<pre>
CTFlearn{Linux_Is_Awesome}
</pre>
