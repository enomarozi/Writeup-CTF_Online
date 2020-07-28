<h1><b>PikesPeak</h1></b>
<pre>
Pay attention to those strings!

<a href='https://ctflearn.com/challenge/download/935'>PikesPeak.jpg</a> 
</pre>
</b><h3>Solution</h3></b>
<p>Eksekusi exiftool dan grep pada file</p>

```console
root@Python:/home/venom/Downloads# exiftool PikesPeak.jpg -a | grep -i comment
Comment                         : CTFLEARN{PikesPeak}.
Comment                         : CTFLearn{Colorado}.
Comment                         : ctflearn{MountainMountainMountain}.
Comment                         : cTfLeArN{CTFMountainCTFmOUNTAIN}.
Comment                         : CTF{AsPEN.Vail}.
Comment                         : CTFlearn{Gandalf}.
Comment                         : ctflearning{AUCKLAND}.
Comment                         : ctfLEARN{MtDoom}.
Comment                         : ctflearninglearning{Mordor.TongariroAlpineCrossing}.
Comment                         : CTFLEARN{MountGedePangrangoNationalPark}.
Comment                         : ctflearncTfLeARN{MountKosciuszko}.
root@Python:/home/venom/Downloads# 
```
<p>Disana terdapat banyak flag, sesuai format flag yaitu CTFlearn{ dan perhatikan lowercase dan uppercase disetiap string</p>
</b><h3>Flag</h3></b>
<pre>
CTFlearn{Gandalf}
</pre>
