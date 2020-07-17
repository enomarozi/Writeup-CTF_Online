<h1><b>ROFL</b></h1>
<pre>
dr3dd gave h3rcul35 a file and said ROFL. 
h3rcul35 immediately repaired the corrupted file and very soon extracted the flag. 
Can you do it too?

<a href="http://static.beast.sdslabs.co/static/ROFL/steg.zip">File</a>
</pre>
<h3><b>Solution</b></h3>
<p>Ekstrak file, maka didapatkan file PNG corrupt. Perbaiki corrupt pada header 52 4F 46 4C menjadi 89 50 4E 47</p>
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/final.png">
</p>
<p>Gunakan zsteg untuk medapatkan flag pada color space BGR LSB</p>

```console
root@Python:/home/venom/Downloads# zsteg final.png  | grep -i CTF
b1,bgr,lsb,xy       .. text: "%CTF{3ll10t_w0uld_b3_s0_pr0ud_0f_y0u}\nI6"
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
CTF{3ll10t_w0uld_b3_s0_pr0ud_0f_y0u}
</pre>
