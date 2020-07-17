<h1><b>The Sloth</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/844f1be303f0c458200e8f5e9942ff92.zip">File</a>
</pre>
</b><h3>Solution</h3></b>
<p>Perhatikan setiap 1 index string sebelum chunk IDAT</p>

```console
root@Python:/home/venom/Downloads# strings hey.png | head -n 10
IHDR
FIDATx
	F0	
"	F0
LIDAT~
AIDAT
GIDAT
G[gG
-IDAT
zz6<
root@Python:/home/venom/Downloads# strings hey.png > flag_dat.txt 
root@Python:/home/venom/Downloads#
```

```python
with open("flag_dat.txt") as f:
    for i in f:
        i = i.strip('\n')
        if "IDAT" in i and len(i) > 4:
            print(i[:1],end="")
```

</b><h3>Flag</h3></b>
<pre>
FLAG-g77miF1E1awTS8t9TkY2hEMw2sqeXGt
</pre>
