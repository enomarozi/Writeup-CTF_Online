<b><h1>Find Me</h1></b>
<pre>
Find the flag in 'flag.txt'.
static.beast.sdslabs.co/static/FINDME/find_me.tar.gz
</pre>
<h3><b>Solution</b></h3>
<p>Extract file, cari flag.txt disetiap tree direktori dengan cara perintah</p>

```console
root@Python:/home/venom/Downloads# tar xf find_me.tar.gz 
root@Python:/home/venom/Downloads# grep -iR ctf
100/99/98/97/96/95/94/93/92/91/90/89/88/87/86/85/84/83/82/81/80/79/78/77/76/75/74/73/72/71/70/69/68/67/66/65/64/63/62/61/60/59/58/57/56/55/54/53/52/51/50/49/48/47/46/45/44/43/42/41/40/39/38/37/36/35/34/33/32/31/30/29/28/27/26/25/24/23/22/21/20/19/18/17/16/15/14/13/12/11/10/9/8/7/6/5/4/3/2/1/flag.txt:CTF{th1s_wh4t_a_fl4g_l00ks_l1ke}
root@Python:/home/venom/Downloads# 
```
<h3><b>Flag</b></h3>
<pre>
CTF{th1s_wh4t_a_fl4g_l00ks_l1ke}
</pre>
