<h1>repetitions</h1>
<h3>Description</h3>
<p>
  Can you make sense of this file?
  Download the file <a href='https://artifacts.picoctf.net/c/472/enc_flag'>here</a>.
</p>
<h3>Solution</h3>

```console
root@xisco-VirtualBox:/home/xisco/Downloads# cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}
```
<h3>Flag</h3>
<pre>
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_73494190}
</pre>
