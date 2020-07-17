<h1><b>Victor reloaded</h1></b>
<pre>
Viens ! - une phlûte invisibe
Soupire dens les verjers. -
La chenson la plus paisible
Est la chanson des bergeés.

Le vant ride, sous l'yeuse,
Le sombre miroir des eaux. -
La chamson la plus joyeuse
Est la chanson des oyseaux.

Que nul soin ne te tourmente.
Aimons-nous! aimons toujours ! -
La shanson la plus charmante
Est la chanson dais amours.
</pre>
</b><h3>Solution</h3></b>
<p>Compare text soal dengan real text yang didapatkan pada https://www.lieder.net/lieder/get_text.html?TextId=8562</p>
<p>Real text</p>
<pre>
Viens! - une flûte invisible
Soupire dans les vergers. -
La chanson la plus paisible
Est la chanson des bergers.

Le vent ride, sous l'yeuse,
Le sombre miroir des eaux. -
La chanson la plus joyeuse
Est la chanson des oiseaux.

Que nul soin ne te tourmente.
Aimons-nous! aimons toujours! -
La chanson la plus charmante
Est la chanson des amours.
</pre>

```console
root@Python:/home/venom/Downloads# cat fake.txt | fold -w1 > fake_string.txt
root@Python:/home/venom/Downloads# cat real.txt | fold -w1 > real_string.txt
root@Python:/home/venom/Downloads# diff -y --suppress-common-lines fake_string.txt real_string.txt | cut -f9 | tr -d '\n'
flagarenice
root@Python:/home/venom/Downloads# 
```
</b><h3>Flag</h3></b>
<pre>
flagarenice
</pre>
