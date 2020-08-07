<h1><b>m00nwalk</h1></b>
<pre>
Decode this <a href='https://2019shell1.picoctf.com/static/6a6fc4f706d31d0c1fd30d35fb77d124/message.wav'>message</a> from the moon. You can also find the 
file in /problems/m00nwalk_3_03dab5f4d1deab675e80ee603fb02236.
</pre>
</b><h3>Solution</h3></b>
<p>Decode SSTV Signal dengan tool QSSTV, sebelumnya pilih pengaturan Tab Sound --> From sound card</p>
<p>Dan aktifkan pulseaudio pada terminal lalu buka QSSTV</p>

```console
venom@Python:~$ pulseaudio --start
venom@Python:~$ qsstv 
```
<p>Biarkan proses berjalan, dan jika selesai Save image hasil decoder, dan buka</p>
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/PicoCTF2019/Forensics/Images/qsstv_flag.png'>
</p>
</b><h3>Flag</h3></b>
<pre>
picoCTF{beep_boop_im_in_space}
</pre>
