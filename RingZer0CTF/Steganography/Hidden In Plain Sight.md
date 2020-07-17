<h1><b>Hidden In Plain Sight</h1></b>
<pre>
<a href="https://ringzer0ctf.com/files/7607cb574e040fec38cec54ac37b40e8.zip">file</a>
</pre>
</b><h3>Solution</h3></b>
<p>Kita diberikan 1 file text yang isinya hacker manifesto, jika diperhatikan kita diminta untuk melihat perbedaan hex-dump dari text soal yang diberikan dengan manifesto yang original pada http://phrack.org/issues/7/3.html</p>
<p>Salin original manifesto hacker dan convert ke hex-dump lalu simpan ke file text pada terminal</p>

```console
root@Python:/home/venom/Downloads# xxd -p real.txt | fold -w 2 > real.hex
root@Python:/home/venom/Downloads# 
```
<p>Lakukan hal yang sama dengan manifesto text yang diberikan</p>

```console
root@Python:/home/venom/Downloads# cat 618d0e51213fa164d93bd92ca5e099c3.txt | cut -d ' ' -f -16 | tr -d ' ' | fold -w 2 > fake.hex
root@Python:/home/venom/Downloads# 
```
<p>Kemudian lihat seluruh perbedaan pada hex-dump, dan ambil nilai hexa yang berbeda pada file fake manifesto lalu convert ke ascii</p>

```python
file1 = open("fake.hex")
file2 = open("real.hex")
for i,j in zip(file1,file2):
    if i != j:
        print(chr(int(i,16)),end="")
```
</b><h3>Flag</h3></b>
<pre>
FLAG-NothingIsEverWhatItSeems
</pre>
