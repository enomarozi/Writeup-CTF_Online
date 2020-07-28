<h1><b>Seeing is believing</h1></b>
<pre>
My colleague's an astronaut who's currently on a mission orbiting in space. 
Just a few hours ago, unfortunately, his communication device caught fire so he's unable to report back to base. 
I did, however, receive a strange file that I can't seem to open. 
I think it may shed some light on his situation. Can you help me save poor boy Johnny? 
File: https://mega.nz/#!LTRUTaZb!9Nh0NwDONJQiOThif3G62evP8H_W9eIJSu0PdBQWKyg
</pre>
</b><h3>Solution</h3></b>
<p>Identifikasi file, dan ternyata itu merupakan file audio OGG, ganti format ke OGG dan buka dengan tool sonic-visualizer</p>

```console
root@Python:/home/venom/Downloads/seeingisbelieving# ls
help.me
root@Python:/home/venom/Downloads/seeingisbelieving# file help.me 
help.me: Ogg data, Vorbis audio, mono, 44100 Hz, ~110000 bps, created by: Xiph.Org libVorbis I (1.3.3)
root@Python:/home/venom/Downloads/seeingisbelieving# mv help.me help.ogg
root@Python:/home/venom/Downloads/seeingisbelieving# sonic-visualiser help.ogg 
```
<p>Add spectogram pada <b>Tab layers --> Add Spectograms</b>, maka didapatkan QR-code terbalik seperti pada gambar dibawah</p> 
<p align='center'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Seeing.jpg'>
</p>
<p>Ganti setting spegtogram supaya QR-Code lebih mudah di decode/dibaca oleh scanner</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF/blob/master/RingZer0CTF/Steganography/Images/SigID%20Level%2012.jpg'>
</p>
<p align='left'>
  <img src='https://github.com/enomarozi/Writeup-CTF_Online/blob/master/CTFlearn/Forensics/Images/Seeing1.jpg'>
</p>
<p>Decode QR-Code maka didapatkan --> https://pastebin.com/zhEhyp3G, flag terdapat pada link</p>
</b><h3>Flag</h3></b>
<pre>
the_flag_is{A_sP3c7r0grAm?!}
</pre>
