<b><h1>Moon Sound</h1></b>
<pre>
w1z4rd captured some sounds from the moon. Decode it.

http://static.beast.sdslabs.co/static/noob/some_audio.mpeg
</pre>
<h3><b>Solution</b></h3>
<p>Jika kita dengar audionya itu identik dengan encoding audio <a href="https://en.m.wikipedia.org/wiki/Slow-scan_television">SSTV</a>, decode audio dengan tools QSSTV</p>
<p>start pulseaudio pada terminal, dan buka QSSTV</p>

```console
venom@Python:~$ pulseaudio --start
venom@Python:~$ qsstv
```
<p>Dan hasilnya
<p align='center'>
  <img src="https://github.com/enomarozi/Writeup-CTF/blob/master/BackdoorCTF/Images/Moon%20Sound_solve.png">
</p>

<h3><b>Flag</b></h3>
<pre>
flag{sstv_moon_walk_1122}
</pre>
